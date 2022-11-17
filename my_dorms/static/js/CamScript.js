window.onload = function() {
    $('body').css('background-color', 'black');
    var video = document.createElement("video");
    var canvasElement = document.getElementById("wm-canvas");
    var canvas = canvasElement.getContext("2d");
    var loadingMessage = document.getElementById("wm-loadingMessage");
    var outputContainer = document.getElementById("wm-output");
    var outputMessage = document.getElementById("wm-outputMessage");
    var outputData = document.getElementById("wm-outputData");

    function drawLine(begin, end, color) {
        canvas.beginPath();
        canvas.moveTo(begin.x, begin.y);
        canvas.lineTo(end.x, end.y);
        canvas.lineWidth = 4;
        canvas.strokeStyle = color;
        canvas.stroke();
    }

    // Use facingMode: environment to attemt to get the front camera on phones
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } }).then(function(stream) {
        video.srcObject = stream;
        video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
        video.play();
        requestAnimationFrame(tick);
    });

    function tick() {
        loadingMessage.innerText = "⌛ Loading video..."
        // video ready
        if (video.readyState === video.HAVE_ENOUGH_DATA) {
            loadingMessage.hidden = true;
            canvasElement.hidden = false;
            outputContainer.hidden = false;

            canvasElement.height = video.videoHeight * (document.body.clientWidth / video.videoWidth);
            canvasElement.width = video.videoWidth * (document.body.clientWidth / video.videoWidth);

            // draw cam canvas
            canvas.filter = 'brightness(40%)';
            canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
            // draw QR canvas
            canvas.filter = 'brightness(100%)';
            canvas.drawImage(video, video.videoWidth * 0.25, video.videoHeight * 0.1, video.videoWidth * 0.5, video.videoWidth * 0.5, canvasElement.width * 0.25, canvasElement.height * 0.1, canvasElement.width * 0.5, canvasElement.width * 0.5);
            canvas.lineWidth = 5;
            canvas.strokeRect(canvasElement.width * 0.25, canvasElement.height * 0.1, canvasElement.width * 0.5, canvasElement.width * 0.5);
            canvas.strokeRect(canvasElement.width * 0.3, canvasElement.height * 0.17, canvasElement.width * 0.4, canvasElement.width * 0.4);

            var imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
            var code = jsQR(imageData.data, imageData.width, imageData.height, {
            inversionAttempts: "dontInvert",
            });
            if (code
                && code.location.topLeftCorner.x > (canvasElement.width * 0.25) && code.location.topLeftCorner.y > (canvasElement.height * 0.1)
                && code.location.bottomRightCorner.x < (canvasElement.width * 0.75) && code.location.bottomRightCorner.y < (canvasElement.height * 0.1 + canvasElement.width * 0.5)
                ) {
                drawLine(code.location.topLeftCorner, code.location.topRightCorner, "#FF3B58");
                drawLine(code.location.topRightCorner, code.location.bottomRightCorner, "#FF3B58");
                drawLine(code.location.bottomRightCorner, code.location.bottomLeftCorner, "#FF3B58");
                drawLine(code.location.bottomLeftCorner, code.location.topLeftCorner, "#FF3B58");

                canvas.clearRect(0, 0, canvasElement.width, canvasElement.height);
                canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
                var editImage = canvasElement.toDataURL("image/jpeg");
                document.getElementById("wm-ocr-image").value = editImage;
                var ocrPosition = [(0, code.location.bottomRightCorner.y), (canvasElement.width, canvasElement.height)];
                document.getElementById("wm-ocr-position").value = ocrPosition;
                var codeData = code.data;
                document.getElementById("wm-code-data").value = codeData;
                document.getElementById("wm-camera-info").submit();

                outputMessage.hidden = true;
                outputData.parentElement.hidden = false;
                outputData.innerText = code.data;
            } else {
                outputMessage.hidden = false;
                outputData.parentElement.hidden = true;
            }
        }
        requestAnimationFrame(tick);
    }
}