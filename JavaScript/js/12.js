// console.log("tut 12")
// let a = document;
// a = document.all;
// a = document.body;
// a = document.forms[0];
// Array.from(a).forEach(function(element){
//     console.log(element);
// })
// a = document.links[0].href;
//  a = document.images[0].alt;
//  a = document.scripts[0].src;
// console.log(a);
 
 
 
//  THIS IS TUTORIAL 13

// console.log(`tut 13`)
// st = 'code'
// a = document.links;
// for (let i=0; i<a.length; i++){
//     h = a[i].href;
//     if (h.includes(st)){
//         console.log(h);
//     }
    
// }



// THIS IS  TUTORIAL 14
console.log(`tut 14`);

// let e = document.getElementById(`first`);

// e = e.className
// e = e.childNodes
// e = e.parentNode
// e.style.color = 'blue';
// e.innerText = `Abhishek`
// e.innerHTML = `<b> First child </b>`
// console.log(e);


let sel = document.querySelector(`#first`);
sel = document.querySelector(`.child1`);
sel = document.querySelector('div')
sel.style.color = 'green'
console.log(sel)


let msel = document.getElementsByClassName('child1');
msel = document.getElementsByTagName('div');
console.log(msel);