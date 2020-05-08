// Timer stuff---------------------------
const startTimer = document.querySelector(".startTime");

startTimer.addEventListener("click", function () {
  let time = Number(document.querySelector("#countdown").innerText);
  let durationValue = document.querySelector("durations");
  console.log(durationValue);

  setInterval(function () {
    document.getElementById("countdown").innerHTML = time;
    time -= 1;
    if (time <= -1) {
      clearInterval(startTimer);
      document.getElementById("countdown").innerHTML = "massage done!";
    }
  }, 1000);
});

// Drag and drop stuff==================================
// ondrag, ondragend, ondragenter, ondragexit, ondragleave, ondragover, ondragstart, and ondrop.

// function onDragStart(event) {
//   event.dataTransfer.setData("text/plain", event.target.id);

//   event.currentTarget.style.backgroundColor = "yellow";
// }

// function onDragOver(event) {
//   event.preventDefault();
// }

// function onDrop(event) {
//   const id = event.dataTransfer.getData("text");

//   const draggableElement = document.getElementById(id);
//   const dropzone = event.target;

//   dropzone.appendChild(draggableElement);

//   event.dataTransfer.clearData();
// }
