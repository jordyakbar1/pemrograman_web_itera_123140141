from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest
from sqlalchemy.orm import Session
from .database import get_session
from .models import Matakuliah
import json


# GET semua matakuliah
@view_config(route_name="get_all_mk", request_method="GET", renderer="json")
def get_all_mk(request):
    session = get_session()
    data = session.query(Matakuliah).all()
    return [mk.to_dict() for mk in data]


# GET satu matakuliah by id
@view_config(route_name="get_mk", request_method="GET", renderer="json")
def get_mk(request):
    session = get_session()
    mk_id = request.matchdict.get("id")
    try:
        mk_id = int(mk_id)
    except (TypeError, ValueError):
        return HTTPBadRequest(json_body={"error": "ID tidak valid"})

    mk = session.query(Matakuliah).filter_by(id=mk_id).first()

    if not mk:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan"})

    return mk.to_dict()


# POST tambah matakuliah
@view_config(route_name="add_mk", request_method="POST", renderer="json")
def add_mk(request):
    session = get_session()
    data = request.json_body

    try:
        # validate required fields
        for f in ("kode_mk", "nama_mk", "sks", "semester"):
            if f not in data:
                return HTTPBadRequest(json_body={"error": f"Field '{f}' diperlukan"})

        # check uniqueness kode_mk
        exists = session.query(Matakuliah).filter_by(kode_mk=data["kode_mk"]).first()
        if exists:
            return HTTPBadRequest(json_body={"error": "kode_mk sudah ada"})

        mk = Matakuliah(
            kode_mk=data["kode_mk"],
            nama_mk=data["nama_mk"],
            sks=int(data["sks"]),
            semester=int(data["semester"])
        )
        session.add(mk)
        session.commit()
        return mk.to_dict()
    except Exception:
        session.rollback()
        return HTTPBadRequest(json_body={"error": "Input tidak valid"})


# PUT update matakuliah
@view_config(route_name="update_mk", request_method="PUT", renderer="json")
def update_mk(request):
    session = get_session()
    mk_id = request.matchdict.get("id")
    try:
        mk_id = int(mk_id)
    except (TypeError, ValueError):
        return HTTPBadRequest(json_body={"error": "ID tidak valid"})

    mk = session.query(Matakuliah).filter_by(id=mk_id).first()

    if not mk:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan"})

    data = request.json_body

    # If kode_mk is changed, ensure uniqueness
    if "kode_mk" in data and data["kode_mk"] != mk.kode_mk:
        exists = session.query(Matakuliah).filter_by(kode_mk=data["kode_mk"]).first()
        if exists:
            return HTTPBadRequest(json_body={"error": "kode_mk sudah ada"})

    mk.kode_mk = data.get("kode_mk", mk.kode_mk)
    mk.nama_mk = data.get("nama_mk", mk.nama_mk)
    if "sks" in data:
        try:
            mk.sks = int(data.get("sks"))
        except Exception:
            return HTTPBadRequest(json_body={"error": "sks tidak valid"})
    if "semester" in data:
        try:
            mk.semester = int(data.get("semester"))
        except Exception:
            return HTTPBadRequest(json_body={"error": "semester tidak valid"})

    session.commit()
    return mk.to_dict()


# DELETE matakuliah
@view_config(route_name="delete_mk", request_method="DELETE", renderer="json")
def delete_mk(request):
    session = get_session()
    mk_id = request.matchdict.get("id")
    try:
        mk_id = int(mk_id)
    except (TypeError, ValueError):
        return HTTPBadRequest(json_body={"error": "ID tidak valid"})

    mk = session.query(Matakuliah).filter_by(id=mk_id).first()
    if not mk:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan"})

    session.delete(mk)
    session.commit()
    return {"status": "deleted"}


@view_config(route_name="home", request_method="GET")
def home(request):
    # Interactive single-file front-end: list, add, delete, update
    body = """
<html>
  <head>
    <meta charset="utf-8" />
    <title>Matakuliah API - UI</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 24px }
      table { border-collapse: collapse; width: 100%; max-width: 900px }
      th, td { border: 1px solid #ddd; padding: 8px }
      th { background: #f4f4f4 }
      form { margin-top: 16px }
      input[type=text], input[type=number] { padding:6px; margin-right:8px }
      button { padding:6px 10px }
    </style>
  </head>
  <body>
    <h1>Matakuliah API — Simple UI</h1>
    <p id="status">Loading...</p>

    <table id="mk-table">
      <thead><tr><th>ID</th><th>Kode</th><th>Nama</th><th>SKS</th><th>Semester</th><th>Aksi</th></tr></thead>
      <tbody></tbody>
    </table>

    <h2>Tambah Matakuliah</h2>
    <form id="add-form">
      <input id="kode_mk" placeholder="kode_mk" required />
      <input id="nama_mk" placeholder="nama_mk" required />
      <input id="sks" type="number" placeholder="sks" required />
      <input id="semester" type="number" placeholder="semester" required />
      <button type="submit">Tambah</button>
    </form>

    <script>
      const status = document.getElementById('status')
      const tbody = document.querySelector('#mk-table tbody')

      async function loadAll(){
        try{
          const res = await fetch('/api/matakuliah')
          const data = await res.json()
          tbody.innerHTML = ''
          data.forEach(mk => {
            const tr = document.createElement('tr')
            tr.innerHTML = `
              <td>${mk.id ?? ''}</td>
              <td>${mk.kode_mk ?? ''}</td>
              <td>${mk.nama_mk ?? ''}</td>
              <td>${mk.sks ?? ''}</td>
              <td>${mk.semester ?? ''}</td>
              <td>
                <button data-id="${mk.id}" class="del">Hapus</button>
                <button data-id="${mk.id}" class="edit">Edit</button>
              </td>`
            tbody.appendChild(tr)
          })
          status.textContent = 'Loaded ' + data.length + ' items.'
        }catch(err){
          status.textContent = 'Error loading data: '+err
        }
      }

      document.getElementById('add-form').addEventListener('submit', async e => {
        e.preventDefault()
        const payload = {
          kode_mk: document.getElementById('kode_mk').value,
          nama_mk: document.getElementById('nama_mk').value,
          sks: Number(document.getElementById('sks').value),
          semester: Number(document.getElementById('semester').value)
        }
        try{
          const res = await fetch('/api/matakuliah', {
            method: 'POST', headers: {'Content-Type':'application/json'},
            body: JSON.stringify(payload)
          })
          if(!res.ok) throw new Error('HTTP '+res.status)
          await loadAll()
          e.target.reset()
        }catch(err){ alert('Tambah gagal: '+err) }
      })

      // Delegate delete/edit buttons
      tbody.addEventListener('click', async (ev) => {
        const btn = ev.target
        if(btn.classList.contains('del')){
          const id = btn.dataset.id
          if(!confirm('Hapus id='+id+' ?')) return
          await fetch('/api/matakuliah/'+id, {method:'DELETE'})
          await loadAll()
        }else if(btn.classList.contains('edit')){
          const id = btn.dataset.id
          const kode = prompt('kode_mk:')
          if(kode===null) return
          const nama = prompt('nama_mk:')
          if(nama===null) return
          const sks = prompt('sks:')
          if(sks===null) return
          const semester = prompt('semester:')
          if(semester===null) return
          const payload = { kode_mk: kode, nama_mk: nama, sks: Number(sks), semester: Number(semester) }
          await fetch('/api/matakuliah/'+id, {method:'PUT', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)})
          await loadAll()
        }
      })

      // initial load
      loadAll()
    </script>
  </body>
</html>
    """

    return Response(body, content_type='text/html')
