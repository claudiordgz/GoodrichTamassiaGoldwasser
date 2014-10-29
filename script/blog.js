// var bt = $('.tableofcontents').position().top;

// $(window).scroll(function() {
        // var wst = $(window).scrollTop();

        // (wst >= bt) ?
        // $('.tableofcontents').css({position: 'fixed', top: 15+'px' }) :  
        // $('.tableofcontents').css({position: 'absolute', top: bt+'px' })

//});

/* swap open/close side menu icons */
$('[data-toggle=collapse]').click(function(){
  	// toggle icon
  	$(this).find("i").toggleClass("glyphicon-chevron-right glyphicon-chevron-down");
});

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-35752941-1', 'auto');
ga('require', 'displayfeatures');
ga('send', 'pageview');
