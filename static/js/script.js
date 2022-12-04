const hamButton = document.getElementById("ham_button");
const sidebar = document.getElementById("sidebar");

let show = true;

hamButton.addEventListener("click", () => {
  sidebar.classList.toggle("sidebar--show", show);
  show = !show;
});
