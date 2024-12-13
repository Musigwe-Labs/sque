$('.navbar-nav .nav-item').click(function() {
    $('.navbar-nav .nav-item.active').removeClass('active'); // Just remove class from all folder
    $(this).addClass('active'); // add onto current
})


$(".navbar .navbar-toggler").click(function(){
  $(".sandwitch").toggleClass("open");
});


var header = document.querySelector('.header-area');


onScroll = () => {
  var scrolledPage = Math.round(window.pageYOffset);
  if(scrolledPage > 60) {
    header.classList.add('sticky');
  } else {
    header.classList.remove('sticky');
  }
}


document.addEventListener('scroll', onScroll);


// jQuery Library has already been added to this pen
jQuery(document).ready(function(){
  jQuery(window).scroll(function() {    
    // edit this based on the scroll height you want it to appear
    if (jQuery(window).scrollTop() >= 500) {
      jQuery("#to-top").css("opacity", "1");
    } else {
      jQuery("#to-top").css("opacity", "0");
    }
  });
  jQuery("#to-top").click(function(){
    jQuery('html, body').animate({
      scrollTop: jQuery("body").offset().top
    }, 300); 
  });
});