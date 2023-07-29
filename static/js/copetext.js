
function copyText() {
  var text = document.getElementById("text-to-copy").innerText;
  navigator.clipboard.writeText(text);
  console.log($encryption);
  alert("Done ");
}
