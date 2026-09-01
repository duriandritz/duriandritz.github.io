const CACHE_NAME = 'statisticaltestselector-v1';
// Include the repository name in the asset paths
const ASSETS = [
  '/duriandritz.github.io/',
  '/duriandritz.github.io/index.html',
  '/duriandritz.github.io/style.css',
  '/duriandritz.github.io/app.js',
  '/duriandritz.github.io/manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
