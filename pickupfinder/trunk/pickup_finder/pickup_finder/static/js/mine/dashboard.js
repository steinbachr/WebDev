function initialize() {    
    var map;
    var $map_filter = $('#map-search')
    var options = {types: ['geocode']};
    autocomplete = new google.maps.places.Autocomplete($map_filter.get(0), options);    
    
    //the filter bar behavior for the map
    $('.map-search-div .btn').click(function() {       
        var geocoder = new google.maps.Geocoder();
        geocoder.geocode({address : $map_filter.val()}, function(results, status) {
            map.setCenter(results[0].geometry.location);
        });
    });    
    
    if (navigator.geolocation)
    {        
        navigator.geolocation.getCurrentPosition(add_map, function() {add_map(false);});        
    } else {
        add_map(false);
    }    
    
    /**add the google map to the window. If the user has geolocation set, given the users location, otherwise false**/
    function add_map(position) {                       
        var mapOptions = {            
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        if (position) {
            mapOptions.center = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
            mapOptions.zoom = 12;
        } else {
            mapOptions.center = new google.maps.LatLng(42.3583, -71.0603); //boston coords
            mapOptions.zoom = 8;
        }

        map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
        
        //add the games to the map        
        for (var i = 0 ; i < games.length ; i++) {
            var latlng = new google.maps.LatLng(games[i].fields.latitude, games[i].fields.longitude);
            var marker = new google.maps.Marker({
                position: latlng,
                map: map,
                title: "games marker",
                id: games[i].pk
            });   
            if (games[i].fields.public) {
                marker.setIcon(STATIC_URL+"images/public_game_marker.png");
            } else {
                marker.setIcon(STATIC_URL+"images/my_game_marker.png");
            }

            //give the marker the games' id so we can use it if the marker is clicked
            google.maps.event.addListener(marker, 'click', function() {   
                fetch_lineup(this.id)                
                populate_details(this.id);
            });
        }      
    }
    
    function populate_details(game_id) {
        var $details = $('.game-details');
        var $details_header = $('.game-details').find('.accordion-inner h4');         
        $details_header.remove();

        $details.find('li').css('display', 'none');
        $details.find('li.'+game_id).css('display', 'block');
    }
}

google.maps.event.addDomListener(window, 'load', initialize);
