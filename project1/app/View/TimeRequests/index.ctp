<div class="row">
    <div class="span12 rent-button">
        <button class="btn-large btn-block btn-primary" type="button">Rent Time Now</button>
    </div>
</div>
<div class="row">
    <div class="span12 past-rentals">
        <h4>Your Previous Requests</h4>
        <div class="overflow-container">
            <ul>
                <?php foreach ($past_requests as $request): ?>
                <li>
                    <?php echo $request['TimeRequest']['description'] ?>
                </li>
                <?php endforeach; ?>
                <?php unset($request); ?>
            </ul>
        </div>
    </div>
</div>
<!-- RENT TIME POPUP -->
<div id="rent_time_popup" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-header">            
        <h3>Complete the steps</h3>                            
        <ul>
        <?php foreach ($steps as $step): ?>
        <li class="progress-indicator empty"></li>
        <?php endforeach; ?>
        </ul>      
        <div class="clearfix"></div>
    </div>
    <div class="modal-body">
        <?php echo $this->Form->create(array('action' => 'add')); ?>
        <form id="submission" method="post">            
        <?php foreach ($steps as $step): ?>                                                                                             
        <div class="step unreached">
            <div class="step-body">
            <h4><?php echo $step['body']; ?></h4>
            </div>
            <div class="step-input"> 
               <?php if($step['input'] != '') { echo $this->Form->input($step['input']); } ?>
            </div>
            <button type="button" class="btn btn-primary btn-large"><?php echo $step['button']; ?></button>
        </div>            
        <?php endforeach; ?>      
        <?php echo $this->Form->input('uid', array('value'=>$user['id'], 'type'=>'hidden')); ?>
        </form>
    </div>
</div>
