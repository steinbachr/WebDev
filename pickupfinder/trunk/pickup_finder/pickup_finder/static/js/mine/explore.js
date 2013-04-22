$(document).ready(function() {
    $('.icon-question-sign').tooltip({container : 'body', trigger : 'click', title : 'If the game was created by one of your friends, it will have a check in this column'});    
})

function mark_friends_games() {
    facebook.get_users_friends(function(response) {
        var $game_rows = $('table tr');
        var friends = response.data;

        for (var i = 0 ; i < friends.length ; i++) {
            $game_rows.each(function() {
                if ($(this).attr('id') == friends[i].id) {
                    $(this).find('td.friends-game i.icon-check').css('display', 'inline-block');//this game was created by a friend
                    $(this).find('td.friends-game i.icon-check-empty').css('display', 'none');
                }                
            });            
        }
    });  
}
