<?php
/**
 * Created by IntelliJ IDEA.
 * User: Bobby
 * Date: 2/7/13
 * Time: 10:02 AM
 * To change this template use File | Settings | File Templates.
 */
class Category extends Model {
    public $hasMany = 'TimeRequest';
}
