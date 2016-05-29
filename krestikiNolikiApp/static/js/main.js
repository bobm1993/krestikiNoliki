/**
 * Created by Bob on 28-May-16.
 */
$(document).ready(function() {

    $('select#size').change(function () {
        var $option = $(this);

        $('#row').val($option.val());
        $('.row, .row option').show();
        $('select#row option:nth-child(n+' + (+$option.val() - 1) + ')').hide()
    });

    $('form#game button').click(function (event) {
        var icon = $('#icon').val();
        $(event.currentTarget).next().val(icon === 'X' ? 1 : 2);
    })

});
