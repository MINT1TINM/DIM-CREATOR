'use strict';

window.onload = function() {
    /*---------------------------------------------------------
     Page Loader
     - Using javascript to reduce jquery lib loading time
     ----------------------------------------------------------*/
    function fade(element) {
        var op = 1;  // initial opacity
        var timer = setInterval(function () {
            if (op <= 0.1){
                clearInterval(timer);
                element.style.display = 'none';
            }

        }, 10);
    }

    if(! /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        setTimeout (function () {
            fade (document.getElementById ('page-loader'));
        }, 200);
    }
};