document.addEventListener("DOMContentLoaded", () => {
    const heroBg = document.getElementById('hero-bg');
    const slider = document.getElementById('slider');
    const items = document.querySelectorAll('.item');
    const totalItems = items.length;
    
    let currentIndex = 0;

    function updateSlider() {
        // Shokol item theke active class remove kora
        items.forEach(item => {
            item.classList.remove('active');
            item.style.opacity = "0.5";
            item.style.transform = "scale(0.8)";
        });

        // Current item-ke active kora ebong boro kora (Mobile Size)
        const currentItem = items[currentIndex];
        currentItem.classList.add('active');
        currentItem.style.opacity = "1";
        currentItem.style.transform = "scale(1.1)";

        // Background change (Desktop Version) sync sequential vabe
        const desktopImg = currentItem.getAttribute('data-desktop');
        if (desktopImg) {
            heroBg.style.backgroundImage = `url('${desktopImg}')`;
        }

        // Slider-ke left side-e move kora
        // 220px holo item width + gap
        const offset = currentIndex * -220; 
        slider.style.transform = `translateX(${offset}px)`;

        // Index barano ebong loop set kora
        currentIndex++;
        if (currentIndex >= totalItems) {
            currentIndex = 0; // Shesh hole abar prothome chole ashbe
        }
    }

    // Initial load
    updateSlider();

    // Auto loop slide protit 5 second por por
    setInterval(updateSlider, 5000);
});