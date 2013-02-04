<head>
    <?php echo $this->Html->charset(); ?>
    <?php echo $this->Html->css(array('bootstrap-responsive.min', 'bootstrap.min'), 'stylesheet', array('inline' => false)); ?>    
    <?php echo $this->Html->css('font-awesome', 'stylesheet', array('inline' => false)); ?>        
    <?php echo $this->Html->css('stylesheet.less?', 'stylesheet/less', array('inline' => false)); ?>        
    
    <?php echo $this->Html->script('libraries/jquery-1.8.3.min'); ?>    
    <?php echo $this->Html->script('libraries/bootstrap.min'); ?>    
    <?php echo $this->Html->script('libraries/mustache'); ?>    
    <?php echo $this->Html->script('libraries/less-1.3.1.min'); ?>    
    <?php echo $this->Html->script('scripts'); ?>       
    <title>Rent My Time</title>
</head>
<body>
<div class="container">
    <div class="row header">
        <div class="top-links">
            <a href="http://www.iambob.me/blog/">My Blog |</a>
            <a href="http://www.iambob.me">My Homepage</a>
        </div>       
        <h1 style="clear: right;">Rent My Time</h1>
    </div>
    <div class="row">
        <div class="span12 rent-button">
            <button class="btn-large btn-block btn-primary" type="button">Rent Time Now</button>
        </div>
    </div>
    <div class="row">
        <div class="span12 past-rentals">
            <h4>Past Rented Time Exploits</h4>
            <div class="overflow-container">
                <ul>
                    <li>
                        Here is something
                    </li>
                    <li>
                        Here is another something
                    </li>
                    <li>
                        Here is something else
                    </li>
                    <li>
                        Yay exploits
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div id="row footer">
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
<!-- RENT TIME POPUP -->
<div id="rent_time_holder"></div>
<script type="text/template" id="modal_temp">
    <div id="rent_time_popup" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-header">            
            <h3>Complete the steps</h3>                            
            <ul>
            {{#steps}}
            <li class="progress-indicator empty"></li>
            {{/steps}}
            </ul>      
            <div class="clearfix"></div>
        </div>
        <div class="modal-body">
            <form id="submission" method="post">            
            {{#steps}}                                                                                              
            <div class="step {{number}} unreached">
                <div class="step-body">
                <h4>{{body}}</h4>
                </div>
                <div class="step-input">
                {{{input}}}    
                </div>
                <button type="button" class="btn btn-primary btn-large">{{button}}</button>
            </div>            
            {{/steps}}            
            </form>
        </div>
    </div>
</script>
</body>
