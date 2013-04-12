var GET_LINEUP_URL = "/ajax/get-lineup/";

function fetch_lineup(game_id) {
    $('.game-lineup').find('.accordion-inner ul').html('<img src="'+STATIC_URL+'images/lineup_loader.gif" />') //put loader as placeholder
    $.get(GET_LINEUP_URL, {'game_id' : game_id}, function(data) {
        populate_lineup(data);
    });    
}

function populate_lineup(data) {
    var players = $.parseJSON(data);
    var $lineup_list = $('.game-lineup').find('.accordion-inner ul');    
    var $lineup_list_header = $('.game-lineup').find('.accordion-inner h4');
    
    //clear the lineup list in case it had stuff from a previous click    
    $lineup_list_header.remove();
    $lineup_list.html('');

    for (var i = 0 ; i < players.length - 1 ; i++) {
        $lineup_list.append('<li>Player: '+players[i].name+'<br />Status: '+players[i].status+'</li>');    
    }
}
