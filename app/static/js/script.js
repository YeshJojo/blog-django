// FADE IN SMALL LOGO AND FAB ON SCROLL
$(window).scroll(function() {
  var scrollPosition = $(this).scrollTop();
  var $fadeInLogo = $('.fadeInLogo');
  var $growInFab = $('.halfway-fab');
  if (scrollPosition > 128) {
    // Fade in logo & bring in FAB
    $fadeInLogo.fadeIn(200);
    $growInFab.removeClass("scale-out");
  } else {
    // Fade out logo & remove FAB
    $fadeInLogo.fadeOut(200);
    $growInFab.addClass("scale-out");
  }
});


// MODAL
$(document).ready(function(){
  $('.modal').modal();
});

// DROPDOWNS
$(document).ready(function(){
  $(".dropdown-button").dropdown(
    {
      belowOrigin: true
    }
  );
});

//TABS
$(document).ready(function(){
  $('ul.tabs').tabs();
});

//SCROLLSPY
$(document).ready(function(){
    $('.scrollspy').scrollSpy();
});

// SIDEBAR
$(document).ready(function(){
  $('.button-collapse').sideNav({
      menuWidth: 300, // Default is 300
      edge: 'left', // Choose the horizontal origin
      closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    }
  );
});
