/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 1/24/13
 * Time: 12:58 PM
 * To change this template use File | Settings | File Templates.
 */
Graphs.rsvpGraph = function(event_id) {
    var eventSummary = attendeeInfo[event_id]['summary'];
    var notReplied = eventSummary.noreply_count;
    var maybe = eventSummary.maybe_count;
    var attending = eventSummary.attending_count;
    var declined = eventSummary.declined_count;
    
    // Create our data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Rsvp');
    data.addColumn('number', 'Attendees');
    data.addRows([
        ['Not Replied', notReplied],
        ['Attending', attending],
        ['Maybe', maybe],
        ['Not Attending', declined]
    ]);
        
    // Set chart options
    var options = {
        title : 'Breakdown by RSVP',
        width : 300,
        height: 300,
        colors: ['#2B15C9', '#00B303', '#F9AF00', '#F92A00'],
        is3D  : true
    };
    
    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('rsvp_graph_'+event_id));
    chart.draw(data, options);
}

Graphs.guyGirlRatio = function(event_id) {     
    var attendance = attendeeInfo[event_id]['attendance'];    
    var noReplyGirls = girlsCount(attendance.noreply),
        maybeGirls = girlsCount(attendance.maybe),
        attendingGirls = girlsCount(attendance.attending),
        declinedGirls = girlsCount(attendance.declined)
    
    var data = google.visualization.arrayToDataTable([
        ['RSVP Status', 'Guys', 'Girls'],
        ['Not Replied', attendance.noreply.length - noReplyGirls , noReplyGirls],
        ['Maybe',  attendance.maybe.length - maybeGirls , maybeGirls],
        ['Attending', attendance.attending.length - attendingGirls , attendingGirls],
        ['Declined', attendance.declined.length - declinedGirls , declinedGirls]
    ]);
    var options = {
        title: 'Guy to Girl Ratio',
        width:400, height:400,
        hAxis: {title: 'RSVP Status', titleTextStyle: {color: 'red'}},
        colors : ['#00B303', '#65047F']
    };
    var chart = new google.visualization.ColumnChart(document.getElementById('guy_girl_graph_'+event_id));
    
    chart.draw(data, options);
    
    function girlsCount(bucket) {
        var count = 0;
        
        for (userObj in bucket) {
            if (bucket[userObj].sex == 'female') {
                count++;
            }
        }
        
        return count;
    }
}

Graphs.friendsInvited = function(event_id) {
    var numberFriendsInvited = attendeeInfo[event_id]['friends_invited'];
    var totalNumberInvited = attendeeInfo[event_id]['summary'].count;

    // Create our data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Friend');
    data.addColumn('number', 'Invites');
    data.addRows([
        ['Current Friend', numberFriendsInvited],
        ['Friend To Be', totalNumberInvited - numberFriendsInvited]
    ]);

    // Set chart options
    var options = {
        title : 'Current Friends Invited',
        width : 300,
        height: 300,
        colors: ['#00B303', '#2B15C9'],
        is3D  : true
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('friends_invited_graph_'+event_id));
    chart.draw(data, options);
}
