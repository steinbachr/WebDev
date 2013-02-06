<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/5/13
 * Time: 1:43 PM
 * To change this template use File | Settings | File Templates.
 */
class UsersController extends AppController {
    public $helpers = array('Html', 'Form');
    public $components = array(
                            'Session',
                            'Auth'=>array('redirect'=>array('controller' => 'time_requests', 'action' => 'index'))
                            );

    public function beforeFilter() { 
        parent::beforeFilter(); 
        $this->Auth->allow('create');
    }
    
    public function login() {
        if ($this->request->is('post')) {            
            if ($this->Auth->login()) {                
                $this->redirect($this->Auth->redirectUrl());
            } else {
                $this->Session->setFlash(__('Sorry, that seems to be a bad combo'));
            }
        }
    }
    
    public function logout() {
        $this->redirect($this->Auth->logout());        
    }
    
    public function create() {
        if ($this->request->is('post')) {
            $this->User->create();
            if ($this->User->save($this->request->data)) {
                $this->request->data['User']['id'] = $this->User->id;
                $this->Auth->login($this->request->data['User']);   //login the user after they've signed up                
                $this->Session->setFlash(__('You\'re all set!'));
                $this->redirect($this->Auth->redirectUrl());
            } else {
                $this->Session->setFlash(__('Failure :('));
            }
        }
    }
}
