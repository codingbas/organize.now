// Stack Overflow back to top button functionality and Luigi van der Pal 
// When the user scrolls down 75px from the top of the document, show the button
function scrollFunction() {
  if (document.body.scrollTop > 75 || document.documentElement.scrollTop > 75) {
    backToTopButton.classList.remove("hidden");
  } else {
    backToTopButton.classList.add("hidden");
  }
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

var backToTopButton = document.getElementById("js-back-to-top");

scrollFunction();
window.onscroll = scrollFunction;
backToTopButton.addEventListener('click', topFunction);