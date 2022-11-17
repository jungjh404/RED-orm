$(document).ready(function() {
    $('body').css('background-color', '');
    let date = new Date();
    let hour = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();

    let machineNum = document.getElementById('wm-container-machine').childElementCount;
    
    for (var i = 1; i <= machineNum; i++){
        var timeElem = $('.wm-container-washingmachine-element:nth-child(' + i + ') .wm-time-washingmachine');
        var endTime = timeElem.var();
        console.log("end time of " + i + "'th machine: " + endTime);
    }
});

function UseButtonClicked(){
    location.href = wm_cameraPage_url;
}

function ReservationButtonClicked(){
    location.href = wm_cameraPage_url;
}