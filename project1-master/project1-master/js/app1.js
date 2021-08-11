$(document).ready(function(){
    $(window).on('scroll',function(){
        var scroll = $(window).scrollTop();
        if(scroll>=50){
            $(".sticky").addClass("stickyadd");

        }else{
            $(".sticky").removeClass("stickyadd");

        }
    })
});

$(document).ready(function() {             
    $('#loginModal').modal('show');
      $(function () {
        $('[data-toggle="tooltip"]').tooltip()
      })
});
const typedTextSpan = document.querySelector(".typed-text");


const textar = ["Welcome" ,"To","Adoptpet"];
const typingDelay = 200;
const erasingDelay = 100;
const newTestDelay = 2000;
let textArrayIndex = 0;
let charIndex = 0;
function type(){
    if(charIndex <textar[textArrayIndex].length){
        typedTextSpan.textContent += textar[textArrayIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, typingDelay);
    }
    else{
        setTimeout(erase, typingDelay);
    }
}
function erase(){
    if(charIndex>0){
        typedTextSpan.textContent = textar[textArrayIndex].substring(0,charIndex-1);
        charIndex--
        setTimeout(erase, erasingDelay);
    }
    else{
        textArrayIndex++
        if(textArrayIndex>=textar.length) textArrayIndex=0;
        setTimeout(type, typingDelay + 1000);


    }
}
document.addEventListener("DOMContentLoaded" , function(){
    setTimeout(type, newTestDela = 250 );
})
