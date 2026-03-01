// const cards = document.querySelectorAll('.card');
// const nextBtn = document.getElementById('next');

// nextBtn.addEventListener('click', () => {
//     const carousel = document.querySelector('.carousel');
//     carousel.appendChild(carousel.firstElementChild);
// });

// const track = document.querySelector('.rs-review-track');
// const dots = document.querySelectorAll('.rs-review-dots span');

// let currentIndex = 0;
// const totalSlides = dots.length;

// function updateSlider(index) {
//     track.style.transform = `translateX(-${index * 500}px)`;

//     dots.forEach(dot => dot.classList.remove('active'));
//     dots[index].classList.add('active');

//     currentIndex = index;
// }

// // Dot Click
// dots.forEach(dot => {
//     dot.addEventListener('click', () => {
//         const index = dot.getAttribute('data-index');
//         updateSlider(index);
//     });
// });

// // Auto Slide
// setInterval(() => {
//     currentIndex++;
//     if (currentIndex >= totalSlides) {
//         currentIndex = 0;
//     }
//     updateSlider(currentIndex);
// }, 3000);

document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    const nextBtn = document.getElementById('next');

    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            const carousel = document.querySelector('.carousel');
            if (carousel) {
                carousel.appendChild(carousel.firstElementChild);
            }
        });
    }

    const track = document.querySelector('.rs-review-track');

    if (track) {
        // Dynamically generate dots based on number of review cards
        const reviewCards = document.querySelectorAll('.rs-review-card');
        const totalSlides = reviewCards.length;
        track.style.width = `${totalSlides * 500}px`; // Set track width for proper sliding
        const dotsContainer = document.querySelector('.rs-review-dots');
        if (dotsContainer) {
            dotsContainer.innerHTML = ''; // Clear existing dots

            for (let i = 0; i < totalSlides; i++) {
                const dot = document.createElement('span');
                dot.setAttribute('data-index', i);
                if (i === 0) dot.classList.add('active');
                dotsContainer.appendChild(dot);
            }

            const dots = document.querySelectorAll('.rs-review-dots span');

            let currentIndex = 0;

            function updateSlider(index) {
                track.style.transform = `translateX(-${index * 500}px)`;

                dots.forEach(dot => dot.classList.remove('active'));
                if (dots[index]) dots[index].classList.add('active');

                currentIndex = index;
            }

            // Dot Click
            dots.forEach(dot => {
                dot.addEventListener('click', () => {
                    const index = parseInt(dot.getAttribute('data-index'));
                    updateSlider(index);
                });
            });

            // Auto Slide
            if (totalSlides > 0) {
                setInterval(() => {
                    currentIndex++;
                    if (currentIndex >= totalSlides) {
                        currentIndex = 0;
                    }
                    updateSlider(currentIndex);
                }, 3000);
            }
        }
    }
});





