"use strict";

function startApp(videoId) {
  const playerEl = document.getElementById('player');
  document.body.replaceChild(createIFrame(videoId), playerEl);
}

function createIFrame(videoId) {
  const iframeEl = document.createElement('iframe');
  const width = document.body.clientWidth;
  const height = document.body.clientHeight;

  iframeEl.setAttribute('id', 'player');
  iframeEl.setAttribute('type', 'text/html');
  iframeEl.setAttribute('src', 'https://www.youtube.com/embed/' + videoId + '?autoplay=0&origin=' + encodeURIComponent(document.location.origin));
  iframeEl.setAttribute('allowfullscreen', '1');
  iframeEl.setAttribute('controls', '0');
  iframeEl.setAttribute('frameborder', '0');

  return iframeEl;
}
