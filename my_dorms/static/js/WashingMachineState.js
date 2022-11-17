$(document).ready(function() {
    $('body').css('background-color', '');
    var date = new Date();
    var date_utc = Date.UTC(date.getUTCFullYear(), date.getUTCMonth(),
                            date.getUTCDate(), date.getUTCHours(),
                            date.getUTCMinutes(), date.getUTCSeconds());

    var date_sec = date_utc / 1000;

    var machineNum = document.getElementById('wm-container-machine').childElementCount;
    
    for (var i = 1; i <= machineNum; i++){
        var target_elem = '.wm-container-washingmachine-element:nth-child(' + i + ')';
        var end_time = $(target_elem + ' .wm-time-washingmachine').text();
        var start_time = $(target_elem + ' .wm-starttime-washingmachine').text();
        var current_machine_time = end_time - date_sec;
        var duration_machine_time = end_time - start_time;

        var duration_machine_time_minutes = Math.floor(duration_machine_time / 60);
        $(target_elem + ' .wm-time-washingmachine').text(duration_machine_time_minutes + "분");

        // machine ended
        if(current_machine_time <= 0){
            
        }

        UpdateTimeBar(target_elem, current_machine_time, duration_machine_time);
    }
});

function UpdateTimeBar(target, current_machine_time, duration_machine_time){
    // var degree = current_machine_time / duration_machine_time
    var degree = 180;
    $(target + ' .wm-circular-progress-time').css('background',
        'conic-gradient(rgb(28, 103, 88) ' + degree + 'deg, rgb(237, 237, 237) 0deg)');
}

function UseButtonClicked(){
    location.href = wm_cameraPage_url;
}

function ReservationButtonClicked(){
    location.href = wm_cameraPage_url;
}