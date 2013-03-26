function populate_lineup(game_id) {
    var $lineup_list = $('.game-lineup').find('.accordion-inner ul');
    var $lineup_list_header = $('.game-lineup').find('.accordion-inner h4');
    //clear the lineup list in case it had stuff from a previous click
    $lineup_list.html('');
    $lineup_list_header.remove();

    for (var i = 0 ; i < player_games.length ; i++) {
        if (player_games[i].fields.game == game_id) {
            for (var j = 0 ; j < players.length ; j++) {
                //if the current player_game is in the clicked game, get the player that matches that player game
                if (players[j].pk == player_games[i].fields.player) {
                    $lineup_list.append('<li>'+players[j].fields.name+'</li>');
                    break;
                }
            }
        }
    }
}
