console.time("Start")

console.log(`hello """ world`);
console.error("this is error")
console.warn("this is warning")

age = 233

console.assert( age<100, {number:age, errorMsg:"This is not a valid age"})
var name = "abhi"
let num = parseFloat(23.34345)
console.log(num.toFixed(21), (typeof num))

const var_lit = {abhi:3432, anil:32, dada:45}


console.table(var_lit)
console.timeEnd('Start')

let  _$b = false
console.log(_$b.toString(), typeof _$b)

let arr = [32,34,5,32,43,3]
let abc = arr.toString()
console.log(arr.length, typeof abc)


let s = "He1llo I am Abhishek Nice to Meet YOUa4"
ss = s.replace(1," this ")
console.log(ss)


let myHtml = `
<h1> This is heading</h1>
${ss+" "+arr} bas ho gaya <br>${s}`

document.body.innerHTML = myHtml



