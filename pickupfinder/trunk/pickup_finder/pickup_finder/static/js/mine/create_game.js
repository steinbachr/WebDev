$(document).ready(function() {
    var $droppable = $('.player-drag-box').droppable();
    var $draggable = $('.draggable').draggable({opacity : .7});
    
    $droppable.on('drop', function(evt, ui) {
        add_player($(evt.target), ui.draggable);        
    });
    
    function add_player(player_box, player) {                
        player_box.find('ul').append(player);
        //remove the weird css on the dragged item
        player.css('position', 'static');
    }
});
