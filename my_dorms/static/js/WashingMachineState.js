$(document).ready(function() {
    console.log("length: " + $('.wm-container-error-message').length);
    if($('.wm-container-error-message').length){
        console.log("error message");
        window.setTimeout(function() {
            $(".wm-container-error-message").fadeTo(500, 0).slideUp(500, function(){
                $(this).remove();
            });
        }, 2000);
    }

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

        // machine ended. display ok
        if(current_machine_time < 0){
            $(target_elem + ' .wm-time-washingmachine').text('OK');
            $(target_elem + ' .wm-time-washingmachine').css('color', 'black');
            $(target_elem + ' .wm-circular-progress-time').toggleClass('ok');
            UpdateTimeBar(target_elem, 0, 1);
            $(target_elem + ' .wm-button-washingmachine-reservation').attr('disabled', true);
            $(target_elem + ' .wm-button-washingmachine-reservation').css('opacity', '0.6');
        }
        // machine not ended.
        else{
            var current_machine_time_minutes = Math.floor(current_machine_time / 60);
            $(target_elem + ' .wm-time-washingmachine').text(current_machine_time_minutes + "분");
            UpdateTimeBar(target_elem, current_machine_time, duration_machine_time);
            $(target_elem + ' .wm-button-washingmachine').css('opacity', '0.6');
        }
    }
});

function UpdateTimeBar(target, current_machine_time, duration_machine_time){
    var degree = Math.floor(current_machine_time / duration_machine_time * 360);
    $(target + ' .wm-circular-progress-time').css('background',
        'conic-gradient(rgb(28, 103, 88) ' + degree + 'deg, rgb(237, 237, 237) 0deg)');
}

function UseButtonClicked(){
    location.href = wm_cameraPage_url;
}

function UseTestButtonClicked(){
    location.href = wm_test_cameraPage_url;
}

function ReservationButtonClicked(){
    location.href = wm_cameraPage_url;
}