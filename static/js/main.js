const imageMinSize = 10000;
const imageMaxSize = 1000000;
const warning = document.getElementById('size-warning');

function showWarning() {
  warning.style.visibility = "visible";
}

function hideWarning() {
  warning.style.visibility = "hidden";
}

//Checks file size for uploaded images Original code courtesy of nkon https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
const checkImageSize = function(event) {
  let input = document.getElementById('image_file');
  let file = input.files[0];
  hideWarning();
  if (file.size >= imageMinSize && file.size <= imageMaxSize) {
    previewFile(event);
  }
  else {
    showWarning();
  } 
};

//Preview selected recipe image when adding or editing. Original code courtesy of nkon on Stack Overflow https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
const previewFile = function(event) {
  let output = document.getElementById('output');
  output.src = URL.createObjectURL(event.target.files[0]);
};


// Change nav colour on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w
$(window).scroll(function() {
  $('nav').toggleClass('scroll', $(this).scrollTop() > 10);
  });


