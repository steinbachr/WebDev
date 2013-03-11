<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/7/13
 * Time: 10:17 AM
 * To change this template use File | Settings | File Templates.
 */
class Duration extends Model {
    public $hasMany = 'TimeRequest';
}
