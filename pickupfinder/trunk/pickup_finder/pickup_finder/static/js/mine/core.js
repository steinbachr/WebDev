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


