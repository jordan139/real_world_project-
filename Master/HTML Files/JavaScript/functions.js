// Any time an element with the class of "tagline" is clicked

/* sample statement for modifying css in Jquery
$(document).ready(function(){
   $(".HeaderBox").css("background-color", "#"); 
});

*/

/* increasing font size 
$(document).ready(function(){
    $(".Header").mouseenter(function(){
       $(".Header").animate({
           fontSize:"+=20pt"
       },2000, "linear"); 
    });
});


*/ 
/*hiding function
$("#Overlay").hide()
    */

/*$(document).ready(function(){
    $("div").click(function(){
        $(this).slideUp(2000).slideDown(2000).fadeOut("slow");    
    });
    
});
*/

$(document).ready(function(){
    $("#help").click(function(){
        $("#Overlay2").fadeIn()    
    });   
    $("#help").click(function(){
        $("#Overlay2").fadeOut()
    });
});