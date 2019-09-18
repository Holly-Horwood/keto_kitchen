const imageMinSize = 10000;
const imageMaxSize = 20000000;
//Preview selected recipe image when adding or editing. Original code courtesy of nkon on Stack Overflow https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
  const previewFile = function(event) {
    let output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
  };

//Checks file size  
const checkImageSize = function(event) {
  let input = document.getElementById('image_file');
  let file = input.files[0];
  if (file.size >= imageMinSize && file.size <= imageMaxSize) {
    document.getElementById('size-warning').style.visibility = "hidden";
  }
  else {
    document.getElementById('size-warning').style.visibility = "visible";
  } 
};

//Bootstrap autofocus for modal 
$('#loginModal').on('shown.bs.modal', function () {
  $('#loginModal').trigger('focus')
});

// Change nav colour on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w
$(window).scroll(function() {
$('nav').toggleClass('scroll', $(this).scrollTop() > 10);
});