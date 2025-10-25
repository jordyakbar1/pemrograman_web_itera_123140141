const form = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const pendingCount = document.getElementById('pendingCount');
const searchInput = document.getElementById('searchInput');
const filterStatus = document.getElementById('filterStatus');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

function displayTasks() {
  taskList.innerHTML = '';
  const searchTerm = searchInput.value.toLowerCase();
  const filter = filterStatus.value;

  const filteredTasks = tasks.filter(task => {
    const matchSearch = task.name.toLowerCase().includes(searchTerm) || task.course.toLowerCase().includes(searchTerm);
    const matchFilter = filter === 'all' ||
                        (filter === 'completed' && task.completed) ||
                        (filter === 'pending' && !task.completed);
    return matchSearch && matchFilter;
  });

  filteredTasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.className = `task ${task.completed ? 'completed' : ''}`;
    li.innerHTML = `
      <div>
        <strong>${task.name}</strong> (${task.course})<br>
        Deadline: ${task.deadline}
      </div>
      <div class="actions">
        <button class="done" onclick="toggleTask(${index})">${task.completed ? '↩️' : '✔️'}</button>
        <button class="edit" onclick="editTask(${index})">✏️</button>
        <button class="delete" onclick="deleteTask(${index})">🗑️</button>
      </div>
    `;
    taskList.appendChild(li);
  });

  const count = tasks.filter(t => !t.completed).length;
  pendingCount.textContent = count;
  localStorage.setItem('tasks', JSON.stringify(tasks));
}

form.addEventListener('submit', e => {
  e.preventDefault();

  const name = document.getElementById('taskName').value.trim();
  const course = document.getElementById('courseName').value.trim();
  const deadline = document.getElementById('deadline').value;

  if (!name || !course || !deadline) {
    alert('Semua field harus diisi!');
    return;
  }

  if (new Date(deadline) < new Date()) {
    alert('Deadline harus tanggal yang akan datang!');
    return;
  }

  tasks.push({ name, course, deadline, completed: false });
  form.reset();
  displayTasks();
});

function toggleTask(index) {
  tasks[index].completed = !tasks[index].completed;
  displayTasks();
}

function editTask(index) {
  const newName = prompt('Ubah nama tugas:', tasks[index].name);
  const newCourse = prompt('Ubah mata kuliah:', tasks[index].course);
  const newDeadline = prompt('Ubah deadline (YYYY-MM-DD):', tasks[index].deadline);

  if (newName && newCourse && newDeadline) {
    tasks[index].name = newName.trim();
    tasks[index].course = newCourse.trim();
    tasks[index].deadline = newDeadline;
    displayTasks();
  } else {
    alert('Semua field harus diisi!');
  }
}

function deleteTask(index) {
  if (confirm('Yakin ingin menghapus tugas ini?')) {
    tasks.splice(index, 1);
    displayTasks();
  }
}

searchInput.addEventListener('input', displayTasks);
filterStatus.addEventListener('change', displayTasks);

displayTasks();
