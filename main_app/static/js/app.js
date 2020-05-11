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


function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');


new Sortable(sortablelist, {
  animation: 150,
  ghostClass: "sortable-ghost",
  onSort: () => {
    const cards = Array.from(document.querySelectorAll("[data-lookup]"));
    const cardIds = cards.map((cardId) => {
      return cardId.dataset.lookup
    })
    console.log(cardIds)
    console.log(JSON.stringify(cardIds))
    $.ajax({
      type: "POST",
      dataType: 'json',
      contentType: 'application/json',
      headers: { "X-CSRFToken": csrftoken },
      url: "/save-group-ordering",
      data: JSON.stringify(cardIds),
      success: function (result) {
        console.log("success")
      }
    });
  },
});
