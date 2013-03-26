$(document).ready(function() {
    var $roster_click = $('td.roster a');
    
    $roster_click.click(function(evt) {
        populate_lineup($(evt.target).attr('class'));
    })
})
