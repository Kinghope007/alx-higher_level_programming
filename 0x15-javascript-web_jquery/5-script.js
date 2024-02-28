$(document).ready(function() {
    // wait for the DOm to load
    $('#add_item').click(function() {
        // click event
        $('<li>Item</li>').appendTo('UL.my_list');
    });
});