// ==UserScript==
// @name         Portugal Overlay
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Orgulho tuga!
// @author       Some anon
// @match        https://hot-potato.reddit.com/embed*
// @icon         https://i.pinimg.com/originals/bb/28/f0/bb28f08db88265208c7329474998d8a5.png
// @grant        none
// ==/UserScript==
if (window.top !== window.self) {
    window.addEventListener('load', () => {
            document.getElementsByTagName("mona-lisa-embed")[0].shadowRoot.children[0].getElementsByTagName("mona-lisa-canvas")[0].shadowRoot.children[0].appendChild(
        (function () {
            const i = document.createElement("img");
            i.src = "https://raw.githubusercontent.com/AsumaPT/draconBot/main/canvas_pt.png";
            i.style = "position: absolute;left: 0;top: 0;image-rendering: pixelated;width: 1000px;height: 1000px; opacity: 0.85";
            console.log(i);
            return i;
        })())

    }, false);

}
