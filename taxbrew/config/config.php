<?php
return [
    'app' => [
        'name' => 'TaxBrew',
        'env' => 'development',
        'debug' => true,
        'url' => 'http://localhost:8000',
        'timezone' => 'UTC',
    ],
    'session' => [
        'driver' => 'file',
        'lifetime' => 120,
        'expire_on_close' => false,
    ],
];
