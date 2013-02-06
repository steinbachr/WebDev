<?php echo $this->Html->css('users', null, array('inline' => false)); ?>

<h3>Create an account! Do it nowww!</h3>
<?php 
echo $this->Form->create(); 
echo $this->Form->input('username'); 
echo $this->Form->input('password');
echo $this->Form->input('email');
?>
<div class="login-buttons">
    <?php echo $this->Form->button('start renting', array('type'=>'submit', 'class'=>'btn btn-success')); ?>    
</div>
</form>
