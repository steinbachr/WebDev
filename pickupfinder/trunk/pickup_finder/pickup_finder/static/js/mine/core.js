var SEEN_NOTIFICATIONS_URL = "/ajax/seen-notifications/";

$(document).ready(function() {
    var $notifications_link = $('li.notifications a');
    var $popup_body = $('.notifications-popover');
    
    $notifications_link.popover({ title: 'Your notifications:', content: $popup_body.html(), html:true, placement: 'bottom' });
    $notifications_link.click(function() {
        $.post(SEEN_NOTIFICATIONS_URL);
        $(this).parent().find('span.notifs-count').html(0);
    });       
});

/**datatables**/
function create_datatables() {
    $('table.datatable').dataTable( {
        "sDom": 't<"bottom"pi><"clear">',
        "iDisplayLength": 10,
        "aoColumns": [
            { "bSortable": false },
            null,
            null,
            null,
            null,
            null,
            { "sType": "datetime-us" }
        ]
    });
    
    $('table th').click(function(evt) {
        $('table th').find('i').css('display', 'none');
        $('table th').find('i.icon-sort').css('display', 'inline');
        $(this).find('i').css('display', 'none');
        $('table th').find('i.icon-question-sign').css('display', 'inline');

        if ($(this).hasClass('sorting_asc')) {
            $(this).find('i.icon-sort-up').css('display', 'inline');
        } else if ($(this).hasClass('sorting_desc')) {
            $(this).find('i.icon-sort-down').css('display', 'inline');
        }
    });
}


