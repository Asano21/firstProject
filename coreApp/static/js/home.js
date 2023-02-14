const icon = document.querySelector(".icon");
const nav = document.querySelector(".mobile-menu-inside");

icon.addEventListener("click", () => {
    icon.classList.toggle("close");
    nav.classList.toggle("show");
});
