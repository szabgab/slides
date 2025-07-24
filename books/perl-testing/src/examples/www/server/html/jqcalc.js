$(document).ready(function(){
        $("#result").append("Result:");

        $("#addstr").click(function() {
            $("#result").html("Result: " + $("#a").val() + $("#b").val());
            return false;
        });
        $("#addnum").click(function() {
            $("#result").html("Result: " + String(parseInt($("#a").val()) + parseInt($("#b").val())));
            return false;
        });
});

