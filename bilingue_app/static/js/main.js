const toggle = document.querySelector(".toggle");
const menu = document.querySelector(".menu");
 
/* Toggle mobile menu */
function toggleMenu() {
        submenu.classList.add("active");
    } 
/* Event Listener */
toggle.addEventListener("click", toggleMenu, false);