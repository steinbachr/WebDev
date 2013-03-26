function initialize() {    
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

        var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
        
        //add the games to the map        
        for (var i = 0 ; i < games.length ; i++) {
            var latlng = new google.maps.LatLng(games[i].fields.latitude, games[i].fields.longitude);
            var marker = new google.maps.Marker({
                position: latlng,
                map: map,
                title: "games marker",
                id: games[i].pk
            });            

            //give the marker the games' id so we can use it if the marker is clicked
            google.maps.event.addListener(marker, 'click', function() {                
                populate_lineup(this.id);           
            });
        }               
    }
}

google.maps.event.addDomListener(window, 'load', initialize);
