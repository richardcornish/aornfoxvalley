var AORNFV = window.AORNFV || {};

AORNFV = (function ($) {

    'use strict';

    // Private members
    

    return {

        // Hide mobile device URL bar
        scrollAddressBar: function () {
            if ((/(iPhone|iPod|BlackBerry|Android)/.test(window.navigator.userAgent)) && (!window.location.hash)) {
                setTimeout(function () {
                    if (!window.pageYOffset) {
                        window.scrollTo(0, 0);
                    }
                }, 100);
            }
        },

        // Show/hide responsive nav
        showHideMobileNav: function () {
            $('.nav-toggler').append('<div class="nav-bar" /><div class="nav-bar" /><div class="nav-bar" />').click(function () {
                var $nav = $('body').find('.nav-responsive');
                if ($nav.attr('data-behavior') == 'nav-hide') {
                    $nav.slideDown().attr('data-behavior', 'nav-show');
                } else {
                    $nav.slideUp().attr('data-behavior', 'nav-hide');
                }
            });
        },
        
        init: function () {
            var self = this;
            self.scrollAddressBar();
            self.showHideMobileNav();
        }

    }

}(jQuery));

jQuery(function () {
    'use strict';
    AORNFV.init();
});