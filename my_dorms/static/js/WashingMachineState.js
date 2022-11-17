$(document).ready(function() {
    $('body').css('background-color', '');
    let date = new Date();
    let date_utc = Date.UTC(date.getUTCFullYear(), date.getUTCMonth(),
                            date.getUTCDate(), date.getUTCHours(),
                            date.getUTCMinutes(), date.getUTCSeconds());
    let hour = date.getHours();
    let minutes = date.getMinutes();
    let seconds = date.getSeconds();

    console.log("date: " + date_utc);

    let machineNum = document.getElementById('wm-container-machine').childElementCount;
    
    for (var i = 1; i <= machineNum; i++){
        var endTime = $('.wm-container-washingmachine-element:nth-child(' + i + ') .wm-time-washingmachine').text();
        console.log("endTime: " + endTime);
        var diffTime = endTime - date_utc;
        console.log("diffTime: " + diffTime);
    }
});

function UseButtonClicked(){
    location.href = wm_cameraPage_url;
}

function ReservationButtonClicked(){
    location.href = wm_cameraPage_url;
}