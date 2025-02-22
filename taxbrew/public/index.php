<?php
define('BASE_PATH', dirname(__DIR__));
require_once BASE_PATH . '/vendor/autoload.php';

// Load configuration
$config = require_once BASE_PATH . '/config/config.php';

// Initialize the application
require_once BASE_PATH . '/app/Core/Bootstrap.php';

// Run the application
$app = new App\Core\Application($config);
$app->run();
