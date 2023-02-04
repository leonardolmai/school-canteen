const hamButton = document.getElementById("ham_button");
const sidebar = document.getElementById("sidebar");

let show = true;

let currentWidth = Math.min(window.innerWidth || Infinity, screen.width);

if (currentWidth > 992) {
  sidebar.classList.add('sidebar--show');
}

hamButton.addEventListener("click", () => {
  sidebar.classList.toggle("sidebar--show", show);
  show = !show;
});

window.addEventListener('resize', () => {
  currentWidth = Math.min(window.innerWidth || Infinity, screen.width);
  if (currentWidth > 992) {
    sidebar.classList.add('sidebar--show');
  } else {
    sidebar.classList.remove('sidebar--show');
  };
});
