jQuery(document).ready(function() {
    $("#orderedlist").addClass("red");
    $("#orderedlist > li").addClass("blue");

    $("#orderedlist li:last").hover(function() {
        $(this).addClass("green");
    },function(){
        $(this).removeClass("green");
    });
});

