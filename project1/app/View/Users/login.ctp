<?php echo $this->Html->css('users', null, array('inline' => false)); ?>

<h3>Get to the choppah!</h3>
<?php 
echo $this->Form->create(); 
echo $this->Form->input('username'); 
echo $this->Form->input('password');
?>
<div class="login-buttons">
    <?php echo $this->Form->button('It\'s a me', array('type'=>'submit', 'class'=>'btn btn-success')); ?>
    <?php echo $this->Html->link('oops I don\'t have an account', array('controller' => 'users', 'action' => 'create'), array('class' => 'btn btn-link small')); ?>
</div>
</form>
