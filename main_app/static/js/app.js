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

// Sorting ---------------------------------------

const saveOrderingButton = document.querySelector(".saveOrdering");
const orderingForm = document.querySelector("#orderingForm");
const formInput = orderingForm.querySelector("#orderingInput");

saveOrderingButton.addEventListener("click", saveOrdering);
const nodes = document.querySelectorAll(".sortable-moves[data-lookup]");

function saveOrdering() {
  console.log("clicked");

  const cards = document.querySelectorAll("[data-lookup]");
  let dataIds = [];
  for (let card of cards) {
    dataIds.push(card.dataset.lookup);
  }
  console.log(card.dataset);

  // formInput.value = dataIds.join(",");
  console.log(formInput);
  orderingForm.submit();
}

new Sortable(sortablelist, {
  animation: 150,
  ghostClass: "sortable-ghost",
  onSort: () => {
    $.ajax({
      url: "save-group-ordering",
      success: function () {
        console.log("clicked");
      },
    });
  },
});
