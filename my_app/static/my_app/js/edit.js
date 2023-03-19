const title = document.querySelector(".expense_title").innerHTML;
const date = document.querySelector(".expense_date").innerHTML;
const amount = document.querySelector(".expense_amount").innerHTML;
const description = document.querySelector(".expense_description").innerHTML;

const titleField = document.querySelector(".edit_title");
const yearField = document.querySelector("#id_date_year");
const monthField = document.querySelector("#id_date_month");
const dayField = document.querySelector("#id_date_day");
const amountField = document.querySelector(".edit_amount");
const descriptionField = document.querySelector(".edit_description");

const months = {
  Jan: "1",
  Feb: "2",
  Mar: "3",
  Apr: "4",
  May: "5",
  Jun: "6",
  Jul: "7",
  Aug: "8",
  Sep: "9",
  Oct: "10",
  Nov: "11",
  Dec: "12",
};

const dateArray = date.replace(",", "").split(" ");
const year = dateArray[2];
const month = months[dateArray[0].slice(0, 3)];
const day = dateArray[1];

console.log(year);
console.log(month);
console.log(day);

const setInitialValues = (title, year, month, day, amount, description) => {
  titleField.value = title;
  yearField.value = year;
  monthField.value = month;
  dayField.value = day;
  (amountField.value = amount), (descriptionField.value = description);
};

setInitialValues(title, year, month, day, amount, description);

console.log(title);
console.log(date);
console.log(amount);
console.log(description);
