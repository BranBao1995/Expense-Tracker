const items = document.querySelectorAll(".result");
const titles = document.querySelectorAll(".result_title");
const dates = document.querySelectorAll(".result_date");
const amounts = document.querySelectorAll(".result_amount");
const descriptions = document.querySelectorAll(".result_description");

const detail_box = document.querySelector(".detail");
const detail_title = document.querySelector(".detail_title");
const detail_date = document.querySelector(".detail_date");
const detail_amount = document.querySelector(".detail_amount");
const detail_description = document.querySelector(".detail_description");
const button_edit = document.querySelector(".button_edit");

const getTitle = (id) => {
  for (let i = 0; i < titles.length; i++) {
    if (titles[i].getAttribute("data-id") === id) {
      return titles[i].innerHTML;
    }
  }
};

const getDate = (id) => {
  for (let i = 0; i < dates.length; i++) {
    if (dates[i].getAttribute("data-id") === id) {
      return dates[i].innerHTML;
    }
  }
};

const getAmount = (id) => {
  for (let i = 0; i < amounts.length; i++) {
    if (amounts[i].getAttribute("data-id") === id) {
      return amounts[i].innerHTML;
    }
  }
};

const getDescription = (id) => {
  for (let i = 0; i < descriptions.length; i++) {
    if (descriptions[i].getAttribute("data-id") === id) {
      return descriptions[i].innerHTML;
    }
  }
};

const renderDetail = (event) => {
  event.preventDefault();

  const target = event.target;

  const id = target.getAttribute("data-id");

  const title = getTitle(id);

  const date = getDate(id);

  const amount = getAmount(id);

  const description = getDescription(id);

  detail_box.style.display = "flex";
  detail_title.innerHTML = title;
  detail_date.innerHTML = date;
  detail_amount.innerHTML = amount;
  detail_description.innerHTML = description;
  button_edit.setAttribute("id", id);
};

const redirect = (event) => {
  const id = event.target.getAttribute("id");
  document.location.replace(`/edit/${id}`);
};

for (let i = 0; i < items.length; i++) {
  items[i].addEventListener("click", renderDetail);
}

if (button_edit) {
  button_edit.addEventListener("click", redirect);
}
