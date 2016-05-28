/**
 * Created by Bob on 28-May-16.
 */
$(document).ready(function() {

    var icon = $('#icon').val();

    $('form button').click(function (event) {
        $(event.currentTarget).next().val(icon === 'X' ? 1 : 2);
    })

});
