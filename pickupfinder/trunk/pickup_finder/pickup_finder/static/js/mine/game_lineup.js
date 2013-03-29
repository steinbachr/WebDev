function populate_lineup(game_id) {
    var $lineup_list = $('.game-lineup').find('.accordion-inner ul');
    var $lineup_list_header = $('.game-lineup').find('.accordion-inner h4');
    //clear the lineup list in case it had stuff from a previous click    
    $lineup_list_header.remove();

    $lineup_list.find('li').css('display', 'none');
    $lineup_list.find('li.'+game_id).css('display', 'block');
}
