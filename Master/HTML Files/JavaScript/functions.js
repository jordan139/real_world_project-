// Any time an element with the class of "tagline" is clicked
$(function(){
    $("div").mouseenter(function(){
        $("div").fadeTo("fast",0.5);
    });
    $("div").mouseleave(function(){
        $("div").fadeTo("fast",1);
    });    
});
/* sample statement for modifying css in Jquery
$(document).ready(function(){
   $(".HeaderBox").css("background-color", "#"); 
});

*/


$(document).ready(function(){
    $(".Header").mouseenter(function(){
       $(".Header").animate({
           fontSize:"+=20pt"
       },2000, "linear"); 
    });
});

/* hiding function
$(".Header").animate({
    fontSize: "+=20pt"
    }
    , 2000);
    
*/