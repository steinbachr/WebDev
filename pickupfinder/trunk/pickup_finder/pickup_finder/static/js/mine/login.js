facebook.login = function login() {
    $('.btn').click(function(evt) {
        evt.preventDefault(); //we want to submit the form only after populating it
        FB.login(function(response) {
            if (response.authResponse) {
                populateForm();
            } else {
                // cancelled
            }
        }, {scope:'publish_stream'});                
    });
}

facebook.get_users_friends = function(cb) {
    FB.api('/me/friends?fields=picture,name,id', function(response) {
        cb(response);        
    });
}

function populateForm() {    
    FB.api('/me', function(response) {
        $('form input[name="name"]').val(response.name);            
        $('form input[name="fb_id"]').val(response.id);      
        $('form').submit();
    });
}
    
