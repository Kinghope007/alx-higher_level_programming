$(document).ready(function() {
    // wait for DOM to fully load
    $('#toggle_header').click(function() {
        // click even
        $('header').toggleClass('red green');
    });
});