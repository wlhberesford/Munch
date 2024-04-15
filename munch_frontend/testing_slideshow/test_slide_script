function nextSlide() {
  const slides = document.querySelectorAll('.slide');
  let activeIndex = -1;
  slides.forEach((slide, index) => {
    if (slide.classList.contains('active')) {
      slide.classList.remove('active');
      activeIndex = index;
    }
  });

  const nextIndex = (activeIndex + 1) % slides.length;
  slides[nextIndex].classList.add('active');
}
