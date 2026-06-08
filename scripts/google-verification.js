/* global hexo */
// Google Search Console 驗證：用 HTML meta tag 注入 <head>。
// 改用 injector 而非上傳檔案，避開 Hexo 檔名/副檔名/skip_render 與 CDN 快取的地雷。
// 此檔進 git、npm install 也洗不掉，不依賴主題檔。
hexo.extend.injector.register(
  'head_end',
  '<meta name="google-site-verification" content="Itek7fGpjqLPCmu3m_5P7VafFpgfJ2VOtRIQ2IanFKc" />',
  'default'
);
