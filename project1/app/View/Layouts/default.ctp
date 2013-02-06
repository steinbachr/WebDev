<?php
/**
 *
 * PHP 5
 *
 * CakePHP(tm) : Rapid Development Framework (http://cakephp.org)
 * Copyright 2005-2012, Cake Software Foundation, Inc. (http://cakefoundation.org)
 *
 * Licensed under The MIT License
 * Redistributions of files must retain the above copyright notice.
 *
 * @copyright     Copyright 2005-2012, Cake Software Foundation, Inc. (http://cakefoundation.org)
 * @link          http://cakephp.org CakePHP(tm) Project
 * @package       Cake.View.Layouts
 * @since         CakePHP(tm) v 0.10.0.1076
 * @license       MIT License (http://www.opensource.org/licenses/mit-license.php)
 */
?>
<!DOCTYPE html>
<html>
<head>
    <?php echo $this->Html->charset(); ?>
    <?php echo $this->Html->css(array('bootstrap-responsive.min', 'bootstrap.min')); ?>    
    <?php echo $this->Html->css('font-awesome'); ?>        
    <?php echo $this->Html->css('stylesheet'); ?>     
    <?php echo $this->fetch('css'); ?>
    
    <?php echo $this->Html->script('libraries/jquery-1.8.3.min'); ?>    
    <?php echo $this->Html->script('libraries/bootstrap.min'); ?>    
    <?php echo $this->Html->script('libraries/mustache'); ?>            
    <?php echo $this->Html->script('scripts'); ?>    
    <?php echo $this->fetch('script'); ?>
            
    <title>Rent My Time</title>
</head>
<body>    
    <div class="container <?php if($show_login) { echo "disabled"; } ?>">
        <div class="row header">  
            <?php if ($user): ?>
            <div class="logout">
                You are logged in as <b><?php echo $user['username'] ?></b><br />
                <?php echo $this->Html->link('logout', array('controller'=>'users', 'action'=>'logout')); ?>
            </div>
            <?php endif ?>
            <div class="top-links">
                <a href="http://www.iambob.me/blog/">My Blog |</a>
                <a href="http://www.iambob.me">My Homepage</a>
            </div>       
            <h1 style="clear: both;">Rent My Time</h1>
        </div>
        <?php
            echo $this->Html->meta('icon');		
        
            echo $this->fetch('meta');                        
            echo $this->Session->flash();
            echo $this->fetch('content');            
        ?>
        <div id="row" class="footer">
            <?php 
                $cakeDescription = __d('cake_dev', 'CakePHP: the rapid development php framework');
                echo $this->Html->link(
                    $this->Html->image('cake.power.gif', array('alt' => $cakeDescription, 'border' => '0')),
                    'http://www.cakephp.org/',
                    array('target' => '_blank', 'escape' => false)
                );
            ?>
        </div>
    </div>
    <?php if($show_login): ?>
    <div class="login-overlay" style="<?php if(!$show_login) { echo $this->Html->style(array('display' => 'none')); } ?>">
        <span>            
            You are not currently logged in. Click 
            <?php echo $this->Html->link('here', array('controller' => 'users', 'action' => 'login')); ?>
            to continue.
        </span>
    </div>     
    <?php endif ?>
</body>
</html>
