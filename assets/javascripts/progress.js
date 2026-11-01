/* 生物信息云 · 阅读进度条
 * 在页面顶部注入一条极光渐变细条，随阅读进度更新宽度。
 * 样式见 assets/stylesheets/premium.css 的 .bic-progress。
 */
(function () {
  "use strict";

  function init() {
    var bar = document.createElement("div");
    bar.className = "bic-progress";
    bar.setAttribute("role", "progressbar");
    bar.setAttribute("aria-label", "阅读进度");
    bar.setAttribute("aria-valuemin", "0");
    bar.setAttribute("aria-valuemax", "100");
    document.body.appendChild(bar);

    var raf = null;

    function update() {
      raf = null;
      var doc = document.documentElement;
      var scrollTop = doc.scrollTop || document.body.scrollTop || 0;
      var max = doc.scrollHeight - doc.clientHeight;
      var pct = max > 0 ? scrollTop / max : 0;
      if (pct < 0) pct = 0;
      if (pct > 1) pct = 1;
      var value = (pct * 100).toFixed(2);
      bar.style.width = value + "%";
      bar.setAttribute("aria-valuenow", value);
    }

    function onScroll() {
      if (raf === null && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        raf = window.requestAnimationFrame(update);
      } else {
        update();
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
