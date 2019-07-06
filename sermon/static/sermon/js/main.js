// sidenav
const sideNav = document.querySelector('.sidenav');
M.Sidenav.init(sideNav, {});
//slider
const slider = document.querySelector('.slider');
M.Slider.init(slider, {
    indicators: false,
    height: 550,
    transition: 500,
    interval: 5000

});
const parallax = document.querySelector('.parallax');
M.Parallax.init(parallax, {

});

// owl carousel
$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    responsive: {
        0: {
            items: 1
        },
        300:{
            items: 1
        },
        350:{
            items: 2
        },
        650: {
            items: 3

        },
        1000: {
            items: 4,
            margin: 10
        }
    }
});

// audio player

var playing = false;
function playAudio(audio) {
    if (playing == false) {
        sermon = new Audio(audio);
        sermon.play();
        playing = true;
    } else {
        sermon.pause();
        playing = false;
    }

}

