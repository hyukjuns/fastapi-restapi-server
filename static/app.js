document.getElementById("todo-form").addEventListener("submit", (event) => {
    event.preventDefault(); // 폼 기본 동작 방지

    const taskInput = document.getElementById("task");
    const task = taskInput.value;

    if (task.trim() === "") {
        alert("Task cannot be empty!");
        return;
    }

    const taskList = document.getElementById("task-list");

    // 체크박스와 텍스트를 포함하는 새로운 할 일 항목 추가
    const taskItem = document.createElement("div");
    taskItem.style.display = "flex";
    taskItem.style.alignItems = "center";
    taskItem.style.marginBottom = "10px";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.style.marginRight = "10px";

    const label = document.createElement("label");
    label.textContent = task;

    // 할 일 항목 구성
    taskItem.appendChild(checkbox);
    taskItem.appendChild(label);

    // 할 일 목록에 추가
    taskList.appendChild(taskItem);

    // 입력 필드 초기화
    taskInput.value = "";
});
