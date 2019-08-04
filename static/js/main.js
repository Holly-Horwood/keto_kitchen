//Code courtesy of nkon on Stack Overflow https://stackoverflow.com/questions/4459379/preview-an-image-before-it-is-uploaded
//put first part into html and get rid of where it says script
<input type="file" accept="image/*" onchange="loadFile(event)">
<img id="output"/>
<script>
  var loadFile = function(event) {
    var output = document.getElementById('output');
    output.src = URL.createObjectURL(event.target.files[0]);
  };
</script>
