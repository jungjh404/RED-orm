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
    +   '<img src="./assets/washingmachine.png" alt="washingmachine">'
    +   '<span class="wm-time-washingmachine">0분</span>'
    + '</button>'
    + '<button type="button" class="wm-button-washingmachine-reservation" onclick="ReservationButtonClicked()"><img src="./assets/button_reservation.png" alt="button_reservation"></button>'
    + '</div>');

    $('.wm-container-washingmachine').append('<div class="wm-container-washingmachine-element">'
        + '<button type="button" class="wm-button-washingmachine">'
        +   '<span class="wm-name-washingmachine">지관 9-2</span>'
        +   '<div class="wm-circular-progress-time"></div>'
        +   '<img src="./assets/washingmachine.png" alt="washingmachine">'
        +   '<span class="wm-time-washingmachine">0분</span>'
        + '</button>'
        + '<button type="button" class="wm-button-washingmachine-reservation" onclick="ReservationButtonClicked()"><img src="./assets/button_reservation.png" alt="button_reservation"></button>'
        + '</div>');
}

function UseButtonClicked(){
    location.href = 'machine_camera.html';
}

function ReservationButtonClicked(){
    location.href = 'machine_camera.html';
}