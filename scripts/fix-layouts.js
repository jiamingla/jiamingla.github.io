/* global hexo */
// This script fixes a Hexo theme path resolution bug where files in source/css/layout/
// (e.g. source/css/layout/_partial/progress-bar.styl) are incorrectly registered as 
// layout views with a `.styl` extension, overriding the actual `.ejs` layouts.
hexo.on('generateBefore', () => {
  const views = hexo.theme.views;
  Object.keys(views).forEach(key => {
    const view = views[key];
    if (view && typeof view === 'object') {
      if (view['.styl']) {
        hexo.log.info(`[fix-layouts] Deleting incorrect .styl view for ${key}`);
        delete view['.styl'];
      }
      if (view['.stylus']) {
        hexo.log.info(`[fix-layouts] Deleting incorrect .stylus view for ${key}`);
        delete view['.stylus'];
      }
    }
  });
});
