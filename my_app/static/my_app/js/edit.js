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
  January: "1",
  February: "2",
  March: "3",
  April: "4",
  May: "5",
  June: "6",
  July: "7",
  August: "8",
  September: "9",
  October: "10",
  November: "11",
  December: "12",
};

const dateArray = date.replace(",", "").split(" ");
const year = dateArray[2];
const month = months[dateArray[0]];
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
