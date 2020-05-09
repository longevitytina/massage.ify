// Timer stuff---------------------------
const startTimer = document.querySelector(".startTime");

startTimer.addEventListener("click", function () {
  let maxTime = Number(document.querySelector("#countdown").innerText);
  let seconds = 0;
  setInterval(function () {
    seconds++;
    let timeRemaining = maxTime - seconds,
      hours = parseInt(timeRemaining / 3600),
      mins = parseInt((timeRemaining % 3600) / 60),
      sec = parseInt((timeRemaining % 3600) % 60);
    let timeDisplay = `${hours}hr: ${mins}min: ${sec}sec`;
    document.getElementById("countdown").innerHTML = timeDisplay;

    if (seconds === maxTime) {
      clearInterval(startTimer);
      document.getElementById("countdown").innerHTML = "massage done!";
    }
  }, 1000);
});

new Sortable(sortablelist, {
  animation: 150,
  ghostClass: "sortable-ghost",
});
