console.log("tutorial no 10")
function greet(name){
    console.log(`Hello ${name}, Welcom here on this page`)
}
 let na = 'abhi'
 let name = 'anil'
 
greet(na)
 
let fun = function(name){
    let a = `mssg is that ..This is your name ${name}`;
    return a;
}

let ret = fun(name)
// console.log(ret)



let obj = {
    name : "Abhi",
    "funct" : function(n){
                return "This is a function defined inside a object"
             }
}

console.log(obj.name)