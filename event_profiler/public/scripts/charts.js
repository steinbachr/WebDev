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
    var options = {'title':'Breakdown by RSVP',
        'width':500,
        'height':300};
    
    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.PieChart(document.getElementById('rsvp_graph_'+event_id));
    chart.draw(data, null);
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
        hAxis: {title: 'RSVP Status', titleTextStyle: {color: 'red'}}
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

