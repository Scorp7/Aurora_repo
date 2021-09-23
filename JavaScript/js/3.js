console.log("test");
// Variables in Js
// var, let, const
var names = `a"'bhi`;
var channel;
channel = "channel value"
console.log(typeof names)

// Rules for creating Javascript variables
var _a = 'a';
var $b = 'b';
console.log(_a,$b)
var city = "delhi"
var work = "this"
{
    let city = undefined
    console.log(typeof city)
}
console.log(city)

const arr1 = [323,3,43,342]
// arr1 = [544,4,4]
arr1.push(1);
console.log(typeof arr1)

/*
CASE TYPES
1. camelCase
2. kebab-case
3. snake_case
4. PascalCase
*/

let obj ={
    abhi: 99,
    aksh: 32
}
console.log(typeof obj)


function andd(){
    
}

 let date = new Date();
 console.log(date);
 
 console.log("abhi","how","are"+"you"+" hope you are fine"); 
 
 
 let myHtml = `Hello ${date}
 is very important . And "you are in city ${city}"`
 
 
 document.body.innerHTML = myHtml