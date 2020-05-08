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
