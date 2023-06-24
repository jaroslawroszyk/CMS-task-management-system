let draggedTask = null;

document.addEventListener('dragstart', dragStart);
document.addEventListener('dragover', dragOver);
document.addEventListener('drop', drop);

function dragStart(event) {
    if (event.target.classList.contains('task')) {
        draggedTask = event.target;
        event.dataTransfer.setData('text/plain', 'dummy');
    }
}

function dragOver(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    if (event.target.classList.contains('task_list')) {
        const targetColumn = event.target;
        targetColumn.appendChild(draggedTask);

        const taskId = draggedTask.getAttribute('id');
        const columnId = targetColumn.getAttribute('id');
        console.log(taskId)
        console.log(columnId)

        updateTaskState(taskId, columnId);
    }
}









function updateTaskState(taskId, columnId) {

    if (columnId === "task_todo_list") {
        columnId = 0
    } else if (columnId === "task_inprog_list") {
        columnId = 1
    } else if (columnId === "task_done_list") {
        columnId = 2
    }

    columnId
    const url = '/update-task-state/';

    const csrftoken = getCookie('csrftoken');

    const formData = new FormData();
    formData.append('task_id', taskId);
    formData.append('column_id', columnId);


    fetch(url, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
      },
      body: formData,
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
  }

  function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
  }