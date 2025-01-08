const burger = document.querySelector("#burger");
const list = document.querySelector(".menu ol");

burger.addEventListener("click", openList);

function openList() {
  list.setAttribute("class", "open");
}

const cross = document.querySelector("#cross");

cross.addEventListener("click", closeList);

function closeList() {
  list.setAttribute("class", "");
}