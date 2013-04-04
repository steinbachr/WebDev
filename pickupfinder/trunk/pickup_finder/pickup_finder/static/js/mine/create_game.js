$(document).ready(function() {        
    var $is_public = $('input[name="public"]');    
    var location_input = document.getElementById('id_location');    

    $(".datepicker" ).datepicker();    
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
    
    $is_public.on('load click', function(evt) {
        var $player_cap = $('input[name="player_cap"]');
        
        if ($(evt.target).is(':checked')) {
            $player_cap.removeAttr('disabled');                     
        } else {
            $player_cap.attr('disabled', 'disabled');
        }
    });
    
    $('form').submit(function() {        
        publish_to_feed();
        $("form").find('.error').each(function() {
            //add error class to the parent control group
            $(this).parent().parent('.control-group').addClass('error');            
        })
    });        

    //when the user has submitted the form, publish the confirmation link to each invited players' profile
    function publish_to_feed() {                    
        FB.api('/me/instapickup_test:create', 'post', {game: window.location, message : "Come play with me! @["+added_users[0]+"]"}, function(response) {
            if (!response || response.error) {                
            } else {                
            }
        });
    }
});

var added_users = [];   //the users added to the box
//add the dragged player to the box
function add_player(player_box, player) {
    var $player_names = $('input[name="player_names"]');;
    var $player_ids = $('input[name="player_ids"]');
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

function get_users_friends(is_mobile) {
    FB.api('/me/friends?fields=picture,name,id', function(response) {
        var $friends_list = $('.friends-list ul');
        var friends = response.data;
        
        for (var i = 0 ; i < friends.length ;  i++) {
            if (is_mobile) {
                $friends_list.append('<li class="draggable" id="'+friends[i].id+'"><img class="ui-li-icon" src="'
                                      +friends[i].picture.data.url+'" />'+friends[i].name+'</li>');
            } else {
                $friends_list.append('<li class="draggable" id="'+friends[i].id+'">'+friends[i].name+'</li>');
            }
            
        }
        
        //we only use the draggable if its not being used as mobile
        if (!is_mobile) {
            var $draggable = $('.draggable').draggable({opacity : .7});    
        } else {
            $friends_list.listview("refresh");
        }
        
        //remove spinner
        $('.spinner').remove();
    });
}
