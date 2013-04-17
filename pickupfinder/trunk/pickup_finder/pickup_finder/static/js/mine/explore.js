$(document).ready(function() {
    $('.icon-question-sign').tooltip({container : 'body', trigger : 'click', title : 'If the game was created by one of your friends, it will have a check in this column'});
    $('table').dataTable( {
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
    })
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
