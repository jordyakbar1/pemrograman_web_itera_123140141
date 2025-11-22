try:
    # when run as module
    from .database import get_session, init_db
    from .models import Matakuliah
except Exception:
    # when executed directly from package root using -m, fallback to absolute
    from database import get_session, init_db
    from models import Matakuliah


def seed():
    init_db()
    session = get_session()
    # insert 3 default matakuliah if table is empty
    existing = session.query(Matakuliah).count()
    if existing == 0:
        mks = [
            Matakuliah(kode_mk='MK001', nama_mk='Algoritma dan Pemrograman', sks=3, semester=1),
            Matakuliah(kode_mk='MK002', nama_mk='Basis Data', sks=3, semester=2),
            Matakuliah(kode_mk='MK003', nama_mk='Sistem Operasi', sks=3, semester=3),
        ]
        session.add_all(mks)
        session.commit()
        print('Seeded 3 matakuliah')
    else:
        print(f'{existing} matakuliah sudah ada, tidak melakukan seed')


if __name__ == '__main__':
    # recommend running as module from parent directory:
    # python -m jordy_123140141_pertemuan6.seed_db
    seed()
