/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 1/17/13
 * Time: 4:10 PM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function() {   
    var $popup = $('#rent_time_popup');
    var $popup_errors = $popup.find('.modal-body .errors');
    
    /**** EVENTS ****/
    $('.rent-button button').click(function() {
        $('.modal').modal();        
    });
    $('.rent-button button, .modal-body .step .btn').click(function() {
        moveStep();
    });
            
    function moveStep() {
        var $progress_bar = $('#rent_time_popup .modal-header ul');
        var $nav_el = $progress_bar.find('li.empty').first();                        
        
        //if the step is required, stop user from moving on
        if (($popup.find('.modal-body .step.active').find('textarea').attr('required') == "required") &&
            ($popup.find('.modal-body .step.active').find('textarea').val() == '')) 
        {
            $popup_errors.html('you need to enter a task for me');
            return;
        } 
        else 
        {
            $popup_errors.html('');
            $nav_el.removeClass('empty').addClass('full');

            if ($popup.find('.step').last().hasClass('active')) {
                $('form').submit(); //if all the elements have been reached, we can submit the form 
            } else {
                $popup.find('.modal-body .step.active').removeClass('active');
                $popup.find('.modal-body .step.unreached').first().removeClass('unreached').addClass('active');
            }
        }
    }
});

