/**
 * Created with IntelliJ IDEA.
 * User: Bobby
 * Date: 1/17/13
 * Time: 4:10 PM
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function() {
    var modal_renderer = {
        modalTemplate : $('#modal_temp').html(),
        steps : function() {
                    return {steps : [modal_renderer.singleStep(1, 'How long do you need?', '<select name="time"><option>1</option><option>2</option><option>3</option><option>Much Longer</option></select>', 'Next'),
                                     modal_renderer.singleStep(2, 'What type of task?', '<select name="type"><option>Web Development</option><option>Discussion</option><option>Other</option></select>', 'Last one'),
                                     modal_renderer.singleStep(3, 'Please provide a brief description', '<textarea name="description" rows="5"></textarea>', 'Finish up'),
                                     modal_renderer.singleStep(4, 'All done! You will be contacted within the next 24 hours', '', 'Finished')]};
        },                
        singleStep : function (num, body, input, button) {
                        return {number : num, body : body, input : input, button : button};
        },        
        render : function() {
            var html = Mustache.to_html(modal_renderer.modalTemplate, modal_renderer.steps());  
            $('#rent_time_holder').html(html);    
            $('.modal').modal();
        }   
    }     
    var $popup;
    
    /**** EVENTS ****/
    $('.rent-button button').click(function() {
        modal_renderer.render();
        $popup = $('#rent_time_popup');
        
        moveStep();
    });   
    
    $('#rent_time_holder').on('click', '#rent_time_popup .modal-body .step .btn', function() {                 
        moveStep();
    });
    
    function moveStep() {
        var $progress_bar = $('#rent_time_popup .modal-header ul');
        var $nav_el = $progress_bar.find('li.empty').first();

        $nav_el.removeClass('empty').addClass('full');
        
        if ($popup.find('.step').last().hasClass('active')) {
            $('form').submit(); //if all the elements have been reached, we can submit the form 
        } else {
            $popup.find('.modal-body .step.active').removeClass('active');
            $popup.find('.modal-body .step.unreached').first().removeClass('unreached').addClass('active');
        }  
    }
})

