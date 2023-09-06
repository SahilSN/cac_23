// Function to handle the scroll event
function handleScroll() {
    const container3 = document.getElementById('container3');
    const container4 = document.getElementById('container4');
    const filler = document.getElementById('filler');
    const scrollY = window.scrollY || window.pageYOffset;
  
    const offset = 00; // Adjust this value as needed
    const offset2 = 600;
  
    if (scrollY > offset) {
      container3.classList.add('fade-in');
    }
    else{
        container3.classList.remove("fade-in");
    }
    if (scrollY > offset2){
        container4.classList.add('fade-in');
        filler.classList.remove('filler');
    }
    else{
        container4.classList.remove("fade-in");
        filler.classList.add('filler');
    }

  }
  
  // Attach the handleScroll function to the scroll event
  window.addEventListener('scroll', handleScroll);
  
