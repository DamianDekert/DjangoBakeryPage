const mediaLGMaxQuery = window.matchMedia('(max-width: 1920px)');
const mediaSMMaxQuery = window.matchMedia('(max-width: 576px)');


function ScreenSlideControl(mediaLGMaxQuery, mediaSMMaxQuery) {
  // Check if the media query is true
  if (mediaLGMaxQuery.matches && !(mediaSMMaxQuery.matches))  {
    // Then log the following message to the console
    $('.products-carousel').slick({
      lazyLoad: 'ondemand',
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      infinite: true,
      autoplaySpeed: 1500,
      arrows: true,
    });
  } else if (mediaLGMaxQuery.matches && mediaSMMaxQuery.matches) {
    $('.products-carousel').slick({
      lazyLoad: 'ondemand',
      slidesToShow: 1,
      slidesToScroll: 1,
      autoplay: true,
      infinite: true,
      autoplaySpeed: 1500,
      arrows: true,
    });
  } else {
    $('.products-carousel').slick({
      lazyLoad: 'ondemand',
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      infinite: true,
      autoplaySpeed: 1500,
      arrows: true,
    });
  }
}

// Register event listener
mediaLGMaxQuery.addListener(ScreenSlideControl)
mediaSMMaxQuery.addListener(ScreenSlideControl)

// Initial check
ScreenSlideControl(mediaLGMaxQuery, mediaSMMaxQuery)

