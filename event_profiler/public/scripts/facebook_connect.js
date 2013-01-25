/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 1/15/13
 * Time: 2:58 PM
 * To change this template use File | Settings | File Templates.
 */
var events = {'data' : new Array()};    
var attendeeInfo = {};   //the attendees information containing data we'll use for graphing

Facebook.getLoginStatus = function() {    
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            Facebook.access_token = response.authResponse.accessToken;
            Facebook.getEvents(Client.renderTemplate);
        } else if (response.status === 'not_authorized') {
            // not_authorized
            Facebook.login();
        } else {
            // not_logged_in
            Facebook.login(function() {Facebook.getEvents(Client.renderTemplate)});
        }
    });
}

Facebook.login = function(cb) {    
    FB.login(function(response) {
        if (response.authResponse) {
            // connected
            Facebook.access_token = response.authResponse.accessToken;    
            if (cb) {
                cb();
            }
        } else {
            // cancelled
        }        
    }, {scope: 'user_events, user_birthday, friends_birthday'});
}

Facebook.getEvents = function(renderer) {    
    FB.api('/me/events', function(response) {        
        $(response['data']).each(function() {
            var event = $(this).get(0);
            getEvent(event.id, renderer);            
        })        
    });        
    
    function getEvent(event_id, renderer) {
        FB.api('/'+event_id+'?fields=id,name,picture,location', function(response) {
            events['data'].push({'id' : response.id, 'name' : response.name, 'picture' : response.picture.data.url, 'location' : response.location});
            renderer(events, '#eventsTpl', '#events');
        }); 
    }   
}

Facebook.getEventAttendees = function(event_id) {     
    FB.api('/'+event_id+'/invited?summary=1', function(response) {
        attendeeInfo[event_id] = {};
        attendeeInfo[event_id]['summary'] = response.summary;                
        Graphs.rsvpGraph(event_id);      
        
        getDetailedUsersInfo();
    });
    
    function getDetailedUsersInfo() {                                       
        var QUERY1 = "SELECT uid,rsvp_status FROM event_member WHERE eid="+event_id;
        var QUERY2 = "SELECT uid,sex FROM user WHERE uid IN (SELECT uid FROM #query1)";
        var QUERY3 = "SELECT uid1 FROM friend WHERE uid2=me() AND uid1 IN (SELECT uid FROM #query2)";
        var queriesDict = {"query1":QUERY1, "query2" :QUERY2, "query3" :QUERY3};
                
        FB.api('/fql', {q : queriesDict}, function(response) {
            var notReplied = []
                , attending = []
                , maybe = []
                , notAttending = [];                        
            var reservationStatusArray = response.data[0].fql_result_set;
            var userInfoArray = response.data[1].fql_result_set
            var friendsInvitedSize = response.data[2].fql_result_set.length;             
            
            //reservation status array and userinfo array should be same size, if not we had a problem but well plow through
            for (var i=0 ; i<reservationStatusArray.length ; i++) {
                if(reservationStatusArray[i].rsvp_status == "attending") {                     
                    attending.push(userInfoArray[i]);                    
                } else if(reservationStatusArray[i].rsvp_status == "unsure") {
                    maybe.push(userInfoArray[i]);
                } else if(reservationStatusArray[i].rsvp_status == "declined") {
                    notAttending.push(userInfoArray[i]);
                } else {
                    notReplied.push(userInfoArray[i]);
                }              
            }
            attendeeInfo[event_id]['friends_invited'] = friendsInvitedSize  
            attendeeInfo[event_id]['attendance'] = {'noreply' : notReplied, 'attending' : attending, 'maybe' : maybe, 'declined' : notAttending};             
            
            Graphs.guyGirlRatio(event_id);
            Graphs.friendsInvited(event_id);
        });                 
    }
}
