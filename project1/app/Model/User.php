<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/4/13
 * Time: 12:33 PM
 * To change this template use File | Settings | File Templates.
 */
App::uses('AuthComponent', 'Controller/Component');
class User extends Model {
    public $validate = array(
                        'username' => array('required' => array(
                                               'rule' => array('notEmpty'),
                                               'message' => 'A username is required'
                                                )
                                           ),
                        'password' => array('required' => array(
                                                'rule' => array('notEmpty'),
                                                'message' => 'A password is required'
                                                )
                                           ),
                        );

    public function beforeSave($options = array()) {
        if (isset($this->data[$this->alias]['password'])) {
            $this->data[$this->alias]['password'] = AuthComponent::password($this->data[$this->alias]['password']);
        }
        return true; 
    }
}
