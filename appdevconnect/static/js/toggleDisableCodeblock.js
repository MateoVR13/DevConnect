

document.getElementById("toggleButton").addEventListener("click", function() {
    var codeBlock = document.getElementById("codeBlock");
    if (codeBlock.style.display === "none") {
      codeBlock.style.display = "block";
    } else {
      codeBlock.style.display = "none";
    }
  });