//Preview selected recipe image when adding or editing. Original code courtesy of nkon on Stack Overflow https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
  const previewFile = function(event) {
    let output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
  };

/*Bootstrap autofocus for modal - not sure if needed??????????
$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
});