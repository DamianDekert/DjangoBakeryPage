const navbar = document.querySelector('#navbar-section');
const logoImg = document.querySelector('.logo-img');

const scrollHandleObserver = () => {

  if (window.pageYOffset > 100) {
    navbar.style.borderBottom = "solid 1px rgba(0, 0, 0, 0.25)";
  } else {
    navbar.style.borderBottom = "none";
  }
};

window.addEventListener("scroll", scrollHandleObserver);
