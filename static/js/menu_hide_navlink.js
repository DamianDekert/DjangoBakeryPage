const navlinks = document.querySelectorAll('.nav-link')
const navBarToggle = document.querySelector("#navbarNav")


const toggleMenu = () => {
    navBarToggle.classList.remove('show')
}


navlinks.forEach(navlink => {
    navlink.addEventListener('click', toggleMenu)
});