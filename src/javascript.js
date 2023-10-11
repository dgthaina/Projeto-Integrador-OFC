

window.onscroll = function() {myFunction()};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  var scrolled = (winScroll / height) * 100;
  document.getElementById("barra").style.width = scrolled + "%";
};


// navbar colorida
window.addEventListener("scroll", () => {
  var navbar2 = document.getElementById("navbar");
    if (window.scrollY > 0) {
        navbar2.style.backgroundColor = "#2facff";
    } else {
        navbar2.style.backgroundColor = "transparent";
    }
});





