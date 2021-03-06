/*jslint white:false, onevar:true, undef:true, nomen:true, eqeqeq:true, plusplus:true, bitwise:true, regexp:true, newcap:true, immed:true, strict:false, browser:true */
/*global jQuery:false, document:false, window:false, location:false */

(function ($) {
    $(document).ready(function () {
        if (jQuery.browser.msie && parseInt(jQuery.browser.version, 10) < 7) {
            // it's not realistic to think we can deal with all the bugs
            // of IE 6 and lower. Fortunately, all this is just progressive
            // enhancement.
            return;
        }
        $(function () {
            $('a[rel=tooltip]').tooltip();
            $('span[rel=twipsy]').tooltip();
        });
        // $('#gallery').carousel();
        $("#gallerytabs").tabs('.items > div.item', {
            effect: 'fade',
            fadeOutSpeed: 1000,
            rotate: true
        }).slideshow({
            autoplay: true,
            interval: 6000
        });
        $("div#viewlet-social-like").each(function () {
            $(this).fadeIn(3000);
            $(this).removeAttr("style");
        });
    });
}(jQuery));
