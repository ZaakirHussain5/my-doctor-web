// use a cacheName for cache versioning
var cacheName = 'v1:static';

// during the install phase you usually want to cache static assets
self.addEventListener('install', function(e) {
    // once the SW is installed, go ahead and fetch the resources to make this work offline
    e.waitUntil(
        caches.open(cacheName).then(function(cache) {
            return cache.addAll([
                './',
                './static/website/css/bootstrap.min.css',
                './static/website/css/responsive.css',
                './static/website/js/jquery-3.3.1.min.js',
                './static/website/js/plugin.js',
                './static/website/fonts/flaticon.css'
            ]).then(function() {
                self.skipWaiting();
            });
        })
    );
});