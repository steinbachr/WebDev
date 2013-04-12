$(document).ready(function() {
    var $roster_click = $('td.roster a');
    var $reservation_click = $('td.rsvp-link a');
    
    $roster_click.click(function(evt) {
        fetch_lineup($(evt.target).attr('class'));
    });
    
    $reservation_click.click(function(evt) {
        var game_id = $(evt.target).attr('class');
        var $rsvp_link = $('#rsvp-modal').find('span.rsvp-link');
        var new_link = $rsvp_link.text().replace(/\d+/, game_id);
        
        $rsvp_link.text(new_link);
        $('#rsvp-modal').modal();        
    })
})
