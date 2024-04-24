let slideIndex = 0;
showSlides(slideIndex);

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    if (n >= slides.length) {
        slideIndex = 0; // Loop back to the first slide
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex].style.display = "block";
}

document.querySelector('.next').addEventListener('click', function() {
    slideIndex++;
    showSlides(slideIndex);
});
