<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/4/13
 * Time: 11:04 AM
 * To change this template use File | Settings | File Templates.
 */
class TimeRequest extends Model {    
    public $belongsTo = array (
        'User' => array (
            'className' => 'User',
            'foreignKey' => 'uid'
        )
    );    
}
