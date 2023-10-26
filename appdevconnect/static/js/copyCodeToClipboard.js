function copyCodeToClipboard() {
    var codeElement = document.querySelector(".hljs code"); // Selecciona el elemento de código
    var codeText = codeElement.innerText; // Obtiene el texto del código

    // Crea un elemento de texto temporal y copia el contenido
    var tempTextArea = document.createElement("textarea");
    tempTextArea.value = codeText;
    document.body.appendChild(tempTextArea);
    tempTextArea.select();
    document.execCommand("copy");
    document.body.removeChild(tempTextArea);


}

// Agrega un evento de clic al botón para copiar el código
var copyButton = document.getElementById("copyButton");
copyButton.addEventListener("click", copyCodeToClipboard);
