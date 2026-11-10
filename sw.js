const BASE = new URL("./", self.location).pathname;
const BUILD = "mwa3h61c";
const PRECACHE = ["/assets/atkinson-hyperlegible-latin-400-normal-BbWidj28.woff","/assets/atkinson-hyperlegible-latin-400-normal-BrHNak5F.woff2","/assets/atkinson-hyperlegible-latin-700-normal-BK6Glc0m.woff","/assets/atkinson-hyperlegible-latin-700-normal-GZI4o3u0.woff2","/assets/atkinson-hyperlegible-latin-ext-400-normal-Bbz-b3yf.woff","/assets/atkinson-hyperlegible-latin-ext-400-normal-DRk46D-x.woff2","/assets/atkinson-hyperlegible-latin-ext-700-normal-BoVPHkS0.woff2","/assets/atkinson-hyperlegible-latin-ext-700-normal-CKkU2Dpt.woff","/assets/fraunces-latin-600-normal-BFCDtZfi.woff2","/assets/fraunces-latin-600-normal-DL5QCzvS.woff","/assets/fraunces-latin-700-normal-CEOla-zY.woff2","/assets/fraunces-latin-700-normal-DTjk5d1Q.woff","/assets/fraunces-latin-800-normal-5RM8DebB.woff2","/assets/fraunces-latin-800-normal-B3oGScaA.woff","/assets/fraunces-latin-ext-600-normal-B0Dy4lqi.woff","/assets/fraunces-latin-ext-600-normal-BtzmzP0X.woff2","/assets/fraunces-latin-ext-700-normal-CanUGppC.woff2","/assets/fraunces-latin-ext-700-normal-DuBstVeD.woff","/assets/fraunces-latin-ext-800-normal-DYQACqvw.woff2","/assets/fraunces-latin-ext-800-normal-pDzgxm9I.woff","/assets/fraunces-vietnamese-600-normal-BjlAJixd.woff2","/assets/fraunces-vietnamese-600-normal-DlAl5EAR.woff","/assets/fraunces-vietnamese-700-normal-DH94m5DZ.woff2","/assets/fraunces-vietnamese-700-normal-DxawQjq2.woff","/assets/fraunces-vietnamese-800-normal-B5-KC0PG.woff2","/assets/fraunces-vietnamese-800-normal-Ciifa4CI.woff","/assets/index-CHoiWnfw.js","/assets/index-VxYfDwb1.css","/assets/index.esm-CndyscTG.js","/assets/pdf.worker.min-CIqJB0yW.mjs","/church-banner.jpg","/firebase-config.js","/flyers/school.svg","/flyers/sermon-notes.pdf","/flyers/sunday.svg","/flyers/supper.svg","/flyers/wednesday.svg","/flyers/youth-night.svg","/icons/apple-touch-icon.png","/icons/favicon-32.png","/icons/icon-192.png","/icons/icon-512.png","/icons/icon-maskable-192.png","/icons/icon-maskable-512.png","/index.html","/logo.png","/manifest.webmanifest","/sanctuary-banner-800.jpg","/sanctuary-banner.jpg","/videos/christmas.jpg","/videos/dedication.jpg","/videos/vbs.jpg","/videos/youth.jpg"];
const SHELL = `plainview-shell-${BUILD}`;
const IMAGES = `plainview-images-${BUILD}`;
const IMAGE_CAP = 80;

try {
  importScripts(new URL("firebase-config.js", self.location).href);
} catch {
  // The app still opens when the config file cannot be fetched.
}

function appPath(href) {
  if (!href) return BASE;
  if (/^(https?:|data:|blob:)/i.test(href)) return href;
  if (href.startsWith(BASE)) return href;
  if (href.startsWith("/")) return BASE + href.slice(1);
  return BASE + href;
}

function isVideo(url) {
  return /\.(mp4|webm|mov|m4v)(\?|$)/i.test(url.pathname);
}

function isImage(url, request) {
  if (request.destination === "image") return true;
  return /\.(png|jpe?g|webp|gif|svg)(\?|$)/i.test(url.pathname);
}

function isHashedAsset(url) {
  return url.pathname.includes(`${BASE}assets/`);
}

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL).then(async (cache) => {
      await Promise.all(PRECACHE.map((url) => cache.add(url).catch(() => undefined)));
    }),
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((key) => key !== SHELL && key !== IMAGES && key.startsWith("plainview-")).map((key) => caches.delete(key)))),
  );
  self.clients.claim();
});

async function trimImages(cache) {
  const keys = await cache.keys();
  if (keys.length <= IMAGE_CAP) return;
  await Promise.all(keys.slice(0, keys.length - IMAGE_CAP).map((key) => cache.delete(key)));
}

async function fromNetwork(request) {
  const response = await fetch(request);
  return response;
}

self.addEventListener("fetch", (event) => {
  const request = event.request;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  if (!url.pathname.startsWith(BASE)) return;
  if (url.pathname.includes("/__/auth/") || url.pathname.includes("/__/firebase/")) return;
  if (isVideo(url) || request.headers.has("range")) return;

  if (request.mode === "navigate") {
    event.respondWith((async () => {
      try {
        const response = await fetch(request);
        if (response.ok) {
          const copy = response.clone();
          const cache = await caches.open(SHELL);
          await cache.put(new URL("index.html", self.location).href, copy);
        }
        return response;
      } catch {
        const cached = (await caches.match(new URL("index.html", self.location).href)) || (await caches.match(BASE));
        return cached || new Response("Offline", { status: 503, headers: { "Content-Type": "text/plain" } });
      }
    })());
    return;
  }

  if (isHashedAsset(url)) {
    event.respondWith((async () => {
      const cached = await caches.match(request);
      if (cached) return cached;
      const response = await fromNetwork(request);
      if (response.ok) {
        const cache = await caches.open(SHELL);
        await cache.put(request, response.clone());
      }
      return response;
    })());
    return;
  }

  if (isImage(url, request)) {
    event.respondWith((async () => {
      const cache = await caches.open(IMAGES);
      const cached = await cache.match(request);
      const refresh = fetch(request)
        .then(async (response) => {
          if (response.ok) {
            await cache.put(request, response.clone());
            await trimImages(cache);
          }
          return response;
        })
        .catch(() => cached);
      return cached || refresh;
    })());
    return;
  }

  event.respondWith((async () => {
    try {
      const response = await fetch(request);
      if (response.ok) {
        const cache = await caches.open(SHELL);
        await cache.put(request, response.clone());
      }
      return response;
    } catch {
      const cached = await caches.match(request);
      return cached || new Response("Offline", { status: 503, headers: { "Content-Type": "text/plain" } });
    }
  })());
});

self.addEventListener("push", (event) => {
  event.waitUntil((async () => {
    const fallback = {
      title: "Plainview Baptist Church",
      body: "Open the app for church news.",
      href: "/",
    };
    let title = fallback.title;
    let body = fallback.body;
    let href = fallback.href;
    try {
      let payload = {};
      if (event.data) {
        try {
          payload = event.data.json();
        } catch {
          const text = event.data.text();
          payload = text ? { body: text } : {};
        }
      }
      const data = payload.data || {};
      const note = payload.notification || {};
      title = note.title || data.title || payload.title || fallback.title;
      body = note.body || data.body || payload.body || fallback.body;
      href = data.url || data.href || payload.url || payload.href || (payload.fcmOptions && payload.fcmOptions.link) || fallback.href;
    } catch {
      title = fallback.title;
      body = fallback.body;
      href = fallback.href;
    }
    const target = new URL(appPath(href || "/"), self.location.origin).href;
    const options = {
      body: body || fallback.body,
      icon: new URL("icons/icon-192.png", self.location).href,
      data: { href: href || "/", url: target },
    };
    try {
      await self.registration.showNotification(title || fallback.title, options);
    } catch {
      await self.registration.showNotification(fallback.title, { body: fallback.body });
    }
  })());
});

function notificationHref(notification) {
  const data = notification.data || {};
  const nested = data.FCM_MSG && (data.FCM_MSG.data || {}) || {};
  return data.url || data.href || nested.url || nested.href || data.link || "/";
}

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const target = new URL(appPath(notificationHref(event.notification)), self.location.origin);
  if (target.origin !== self.location.origin) return;
  const href = `${target.pathname}${target.search}${target.hash}`;
  event.waitUntil((async () => {
    const windows = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
    const sameOrigin = windows.filter((client) => {
      try { return new URL(client.url).origin === self.location.origin; } catch { return false; }
    });
    const current = sameOrigin.find((client) => client.url.startsWith(self.registration.scope)) || sameOrigin[0];
    if (current) {
      await current.focus();
      if (typeof current.navigate === "function") {
        try {
          await current.navigate(target.href);
          return;
        } catch {
          // The page will open the route itself.
        }
      }
      current.postMessage({ type: "plainview-open", href });
      return;
    }
    await self.clients.openWindow(target.href);
  })());
});
