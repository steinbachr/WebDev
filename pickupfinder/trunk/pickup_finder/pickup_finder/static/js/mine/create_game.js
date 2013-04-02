$(document).ready(function() {    
    var $droppable = $('.player-drag-box').droppable();
    var $is_public = $('input[name="public"]');
    var $player_cap = $('input[name="player_cap"]');
    var location_input = document.getElementById('id_location');    
    var $player_names = $('input[name="player_names"]');;
    var $player_ids = $('input[name="player_ids"]');

    $(".datepicker" ).datepicker();
    $('.modal').modal();
    var options = {types: ['geocode']};
    autocomplete = new google.maps.places.Autocomplete(location_input, options);
    
    //form validation stuff
    $.validator.addMethod("time",function(value,element)
    {
        return this.optional(element) || /^\d+:\d\d(AM|PM)$/i.test(value);
    },"Please use a valid time");
    $("form").validate({rules : {
        'start_date' : {
            'required' : true, 
            'date' : true
        },
        'start_time' : {
            'required' : true,
            'time' : true
        }
    }});
    
    $droppable.on('drop', function(evt, ui) {
        add_player($(evt.target), ui.draggable);        
    });
    
    $is_public.on('load click', function(evt) {
        if ($(evt.target).is(':checked')) {
            $player_cap.removeAttr('disabled');                     
        } else {
            $player_cap.attr('disabled', 'true');
        }
    });
    
    $('form').submit(function() {        
        publish_to_feed();
        $("form").find('.error').each(function() {
            //add error class to the parent control group
            $(this).parent().parent('.control-group').addClass('error');            
        })
    });
    
    var added_users = [];   //the users added to the box
    //add the dragged player to the box
    function add_player(player_box, player) {
        var old_player_names = $player_names.val();
        var old_player_ids = $player_ids.val();;
        
        player_box.find('ul').append(player);
        added_users.push(player.attr('id'));
        
        //add the player to the player_names input and the player_ids input
        $player_names.val(old_player_names + ',' + player.text())
        $player_ids.val(old_player_ids + ',' + player.attr('id'));
        
        //remove the weird css on the dragged item        
        player.css('position', 'static');        
    }

    //when the user has submitted the form, publish the confirmation link to each invited players' profile
    function publish_to_feed() {                    
        FB.api('/me/instapickup_test:create', 'post', {game: window.location, message : "Come play with me! @["+added_users[0]+"]"}, function(response) {
            if (!response || response.error) {                
            } else {                
            }
        });
    }
});

function get_users_friends() {
    FB.api('/me/friends', function(response) {
        var $friends_list = $('.friends-list ul');
        var friends = response.data;
        
        for (var i = 0 ; i < friends.length ;  i++) {
            $friends_list.append('<li class="draggable" id="'+friends[i].id+'">'+friends[i].name+'</li>');
        }
        
        var $draggable = $('.draggable').draggable({opacity : .7});
        //remove spinner
        $('.spinner').remove();
    });
}
