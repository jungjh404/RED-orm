$(document).ready(function() {
    SetWashingMachine();
});

function SetWashingMachine(){
    // clear container
    $('.wm-container-washingmachine').empty();

    // get machineInfo and setMachines
    // getMachineInfo();
    // setMachines
    $('.wm-container-washingmachine').append('<div class="wm-container-washingmachine-element">'
    + '<button type="button" class="wm-button-washingmachine">'
    +   '<span class="wm-name-washingmachine">지관 9-1</span>'
    +   '<div class="wm-circular-progress-time"></div>'
    +   '<img src=' + wm_machineImage_url + ' alt="washingmachine">'
    +   '<span class="wm-time-washingmachine">0분</span>'
    + '</button>'
    + '<button type="button" class="wm-button-washingmachine-reservation" onclick="ReservationButtonClicked()"><img src=' + wm_buttonReservationImage_url + ' alt="button_reservation"></button>'
    + '</div>');

    $('.wm-container-washingmachine').append('<div class="wm-container-washingmachine-element">'
    + '<button type="button" class="wm-button-washingmachine">'
    +   '<span class="wm-name-washingmachine">지관 9-2</span>'
    +   '<div class="wm-circular-progress-time"></div>'
    +   '<img src=' + wm_machineImage_url + ' alt="washingmachine">'
    +   '<span class="wm-time-washingmachine">0분</span>'
    + '</button>'
    + '<button type="button" class="wm-button-washingmachine-reservation" onclick="ReservationButtonClicked()"><img src=' + wm_buttonReservationImage_url + ' alt="button_reservation"></button>'
    + '</div>');
}

function UseButtonClicked(){
    location.href = wm_cameraPage_url;
}

function ReservationButtonClicked(){
    location.href = wm_cameraPage_url;
}