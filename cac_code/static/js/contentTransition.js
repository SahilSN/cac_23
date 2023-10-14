function transition() {
    var content = document.getElementById("content");
    var a = document.getElementById("a");
  
    a.classList.add("fade-out");
  
    setTimeout(function() {
      a.remove();
      content.style.display = "inline-block";
  
      content.classList.add("fade-in");
    }, 500); 
  }
  