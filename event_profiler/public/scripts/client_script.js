/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 1/22/13
 * Time: 4:18 PM
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function() {
    $('#events').on('click', 'button', function() {
        var eventId = $(this).attr('id');
        var $div = $(this).parent('li').next('div');
        
        //if we've already fetched the attendees for this event from fb, no need to make duplicate call
        if (attendeeInfo[eventId]) {
            Graphs.rsvpGraph(eventId);
            Graphs.guyGirlRatio(eventId);
            Graphs.friendsInvited(eventId);
        } else {
            Facebook.getEventAttendees(eventId);            
        }        
        animateBox($div);                   
    });
    
    function animateBox($selector) {
        var NEW_BOX_HEIGHT = 400;
        var NEW_BOX_WIDTH = 1100;
        
        if (!$selector.hasClass('opened')) {
            $selector.addClass('opened');
            $selector.animate({
                height: '+='+NEW_BOX_HEIGHT,
                opacity: '1'
            }, 2000, function() {
                $selector.animate({
                    width: '+='+NEW_BOX_WIDTH
                }, 3000);
            });
        }
        else {
            $selector.removeClass('opened');
            $selector.find('.graph-holder').html('');
            $selector.animate({
                height: '-='+NEW_BOX_HEIGHT                
            }, 2000, function() {
                $selector.animate({
                    width: '-='+NEW_BOX_WIDTH,
                    opacity: '0'
                }, 3000);
            });
        } 
    }        
})

Client.renderTemplate = function(data, template_selector, destination_selector) {     
    var template = $(template_selector).html();
    var html = Mustache.to_html(template, data);

    $(destination_selector).html(html);
}
