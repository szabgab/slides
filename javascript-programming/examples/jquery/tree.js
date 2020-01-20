    $(document).ready(function(){
        $("#report > ul > li").find("li").hide();
        //alert("load");
        $("a").filter(".show").click(function() {
            $("#report > ul > li").find("li").show();
            return false;
        });
        $("a").filter(".hide").click(function() {
            $("#report > ul > li").find("li").hide();
            return false;
        });
        $("li").click(function(){
            //alert("clicked on " + $(this).attr("id"));
            //$(this).parent().parent().children().children().each(function() {
            $(this).children().children("li").each(function() {
                //alert($(this).css("display"));
                //alert($(this).attr("id"));
                if ($(this).css("display") == 'none') {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            });
            return false; // without this a further click on the parent element was received
        });

        $("a").click(function(){
            //alert("Thanks for visiting again!");

            //alert($(this).attr("class"));
            //if ($(this).attr("class") == 'test') {
            //    $("a").removeClass("test");
            //} else {
            //    $("a").addClass("test");
            //}

            //$(this).hide("slow");
     //       return false;
            });

        $("a")
            .filter(".clickme")
                .click(function(){
                    alert("You are now leaving the site.");
                })
                .end()
            .filter(".hideme")
                .click(function(){
                    $(this).hide();
                    return false;
                })
            .end();
    });

