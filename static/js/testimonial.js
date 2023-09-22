            // Slider=================================================
            const slider = function () {
              const slides = document.querySelectorAll('.slide2');
              const btnLeft = document.querySelector('.slider__btn--left');
              const btnRight = document.querySelector('.slider__btn--right');
          
              let curSlide = 0;
              const maxSlide = slides.length;
          
              const goToSlide = function (slide) {
                slides.forEach(
                  (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
                );
              };
          
              // Next slide
              const nextSlide = function () {
                if (curSlide === maxSlide - 1) {
                  curSlide = 0; // Loop back to the first slide
                } else {
                  curSlide++;
                }
          
                goToSlide(curSlide);
              };
        
              



              // Previous slide
              const prevSlide = function () {
                if (curSlide === 0) {
                  curSlide = maxSlide - 1; // Loop to the last slide
                } else {
                  curSlide--;
                }
                goToSlide(curSlide);
              };
          
              const init = function () {
                goToSlide(0);
              };
              init();
          
              // Event handlers
              btnRight.addEventListener('click', nextSlide);
              btnLeft.addEventListener('click', prevSlide);
          
              document.addEventListener('keydown', function (e) {
                if (e.key === 'ArrowLeft') prevSlide();
                e.key === 'ArrowRight' && nextSlide();
              });
          
              // Autoplay functionality
              let autoplayInterval; // Variable to store the interval ID
          
              // const startAutoplay = function () {
              //   autoplayInterval = setInterval(nextSlide, 1000); // Change slide every 3 seconds (adjust as needed)
              // };
          
              const stopAutoplay = function () {
                clearInterval(autoplayInterval); // Stop the autoplay timer
              };
          
              // Start autoplay when the page loads
              // startAutoplay();
          
              // Pause autoplay when mouse enters the slider area
              document.querySelector('.slider2').addEventListener('mouseenter', stopAutoplay);
          
              // Resume autoplay when mouse leaves the slider area
              // document.querySelector('.slider').addEventListener('mouseleave', startAutoplay);
            };
          
            slider();