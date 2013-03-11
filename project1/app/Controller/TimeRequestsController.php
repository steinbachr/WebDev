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
App::uses('CakeEmail', 'Network/Email');
class TimeRequestsController extends AppController {   
    public $helpers = array('Html', 'Form');
    public $components = array('Auth', 'Session');

    public function beforeFilter() {
        parent::beforeFilter();
        $this->Auth->allow('index');
    }

    public function index() {        
        $steps = array(
                    array('body'=>'What type of task?', 'input'=>'category_id', 'button'=>'continue'),
                    array('body'=>'What type of task?', 'input'=>'duration_id', 'button'=>'last step'),
                    array('body'=>'What type of task?', 'input'=>'description', 'button'=>'finish up'),
                    array('body'=>'All Done! Expect an email in the next 24 hours!', 'input'=>'', 'button'=>'close me')
                 );
        $logged_in = AuthComponent::user('id');
        
        if($logged_in) {
            $user = $this->Auth->user();
            
            $this->set('user', $user);
            $this->set('steps', $steps);
            $this->set('past_requests', $this->TimeRequest->find('all', array('conditions' => array('TimeRequest.user_id' => $user['id']))));
            $this->set('categories', $this->TimeRequest->Category->find('list'));
            $this->set('durations', $this->TimeRequest->Duration->find('list'));
        }        
        $this->set('show_login', !$logged_in);                
    }
    
    public function add() {        
        if ($this->request->is('post')) {
            $this->TimeRequest->create();                           
            if ($this->TimeRequest->save($this->request->data)) {
                $time_request = $this->TimeRequest->findById($this->TimeRequest->id); 
                
                #send email to user
                $email = new CakeEmail();
                $email->viewVars(array('name' => $time_request['User']['username'], 'time_request' => $time_request));
                $email->template('confirm_request')
                    ->emailFormat('both')
                    ->to($time_request['User']['email'])
                    ->from('bobby@incepted.us')
                    ->subject('Be a time hostage, take my time')
                    ->send();

                #send email to me
                $email = new CakeEmail();
                $email->viewVars(array('name' => $time_request['User']['username'], 'time_request' => $time_request, 'email' => $time_request['User']['email']));
                $email->template('my_request_confirmation')
                    ->emailFormat('html')
                    ->to('steinbach.rj@gmail.com')
                    ->from('bobby@incepted.us')
                    ->subject('Time Request Pending')
                    ->send();
                
                $this->Session->setFlash('Your submission has been received');
                $this->redirect(array('action' => 'index'));               
            } else {
                $this->Session->setFlash('Unable to add your post.');
            }
        }
    }
    
    public function view() {

    }
}
