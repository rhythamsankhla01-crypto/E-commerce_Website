const slider1 = document.getElementById("slider");
const leftBtn = document.getElementById("leftBtn");
const rightBtn = document.getElementById("rightBtn");

leftBtn.addEventListener("click", () => {
    slider1.scrollLeft -= 200;
});

rightBtn.addEventListener("click", () => {
    slider1.scrollLeft += 200;
});




//for bags

const uSliderRail = document.querySelector(".uProductSliderRail");
const uNavLeftBtn = document.querySelector(".uProductNavLeft");
const uNavRightBtn = document.querySelector(".uProductNavRight");

let uCurrentTranslateX = 0;
const uSingleCardWidth = 300;

uNavRightBtn.addEventListener("click", () => {
  uCurrentTranslateX -= uSingleCardWidth;
  uSliderRail.style.transform = `translateX(${uCurrentTranslateX}px)`;
});

uNavLeftBtn.addEventListener("click", () => {
  uCurrentTranslateX += uSingleCardWidth;
  if (uCurrentTranslateX > 0) uCurrentTranslateX = 0;
  uSliderRail.style.transform = `translateX(${uCurrentTranslateX}px)`;
});
