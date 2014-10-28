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

