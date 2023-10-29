// let slideIndex = 0;
// let numSlides = 0;

// // Function to add a new slide
// function addSlide() {
//   slideIndex++;
//   numSlides++;
//   let mySlide = document.createElement("div");
//   mySlide.className = "mySlides fade";
//   mySlide.id = numSlides;

//   let numbertext = document.createElement("div");
//   numbertext.className = "numbertext";
//   numbertext.innerText = numSlides;

//   let text = document.createElement("div");
//   text.className = "text";
//   text.innerText = "Caption Text " + numSlides;

//   let slideshowContainer = document.getElementById("slideshow-container");
//   slideshowContainer.appendChild(mySlide);
//   mySlide.appendChild(numbertext);
//   mySlide.appendChild(text);
//   showSlides(slideIndex);
// }

// // Next/previous controls
// function plusSlides() {
//   if(slideIndex == numSlides){
//     addSlide();
//   }
//   else{
//     slideIndex++;
//     showSlides(slideIndex);
//   }
// }

// function minusSlides(){
//   if(slideIndex == 1){
//     console.log("Slide -1");
//   }
//   else{
//     slideIndex--;
//     showSlides(slideIndex);
//   }
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(n);
// }

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   if (n > slides.length) {
//     slideIndex = 1;
//   }
//   if (n < 1) {
//     slideIndex = slides.length;
//   }
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   slides[slideIndex - 1].style.display = "block";
// }

// // Initial slide
// addSlide();

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides() {
  showSlides(slideIndex += 1);
}

function minusSlides() {
    showSlides(slideIndex -= 1);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  slides[slideIndex-1].style.display = "block";
}