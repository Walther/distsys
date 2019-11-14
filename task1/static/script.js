let waiting = false

function load_data() {
    let url = '/currenttemp'
    $.ajax({ url: url,
            success: function(data) {
                display_data(data);
                wait_for_update();
            },
    });
    return true
}

function wait_for_update() {
    if (!waiting) {
        waiting = true;
        $.ajax({ url: '/updated',
                success: load_data,
                complete: function() {
                    waiting = false;
                    wait_for_update();
                },
                timeout: 10000,
                });
    }
}

function display_data(data) {
    $('div#contents').html(data.contents);
}

$(document).ready(function() {
    $('div#contents').append('loading data');
    load_data();
});