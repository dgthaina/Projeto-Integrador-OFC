window.onscroll = function () { myFunction() };

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
        navbar2.style.backgroundColor = "#7be0ff";
    } else {
        navbar2.style.backgroundColor = "transparent";
    }
});

var t = window.scrollY;

window.onscroll = () => {
    document.querySelectorAll('.reveal').forEach(e => {
        if (e.getBoundingClientRect().top < window.innerHeight - 150) {
            e.classList.add('active');
        } else {
            e.classList.remove('active');
        }
    });
}