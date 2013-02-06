<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/4/13
 * Time: 11:03 AM
 * To change this template use File | Settings | File Templates.
 * 
 * //        Debugger::dump(AuthComponent::user('id'));
 */
class TimeRequestsController extends AppController {   
    public $helpers = array('Html', 'Form');
    public $components = array('Auth', 'Session');

    public function beforeFilter() {
        parent::beforeFilter();
        $this->Auth->allow('index');
    }

    public function index() {
        $steps = array(
                    array('body'=>'What type of task?', 'input'=>'category', 'button'=>'continue'),
                    array('body'=>'What type of task?', 'input'=>'duration', 'button'=>'last step'),
                    array('body'=>'What type of task?', 'input'=>'description', 'button'=>'finish up'),
                    array('body'=>'All Done! Expect an email in the next 24 hours!', 'input'=>'', 'button'=>'close me')
                 );
        $logged_in = AuthComponent::user('id');
        
        if($logged_in) {
            $this->set('user', $this->Auth->user());
            $this->set('steps', $steps);
            $this->set('past_requests', $this->TimeRequest->find('all') );
        }        
        $this->set('show_login', !$logged_in);                
    }
    
    public function add() {        
        if ($this->request->is('post')) {
            $this->TimeRequest->create();
            if ($this->TimeRequest->save($this->request->data)) {
                $this->Session->setFlash('Your submission has been received');
                $this->redirect(array('action' => 'index')); 
            } 
            else {
                $this->Session->setFlash('Unable to add your post.');
            }
        }
    }
}
