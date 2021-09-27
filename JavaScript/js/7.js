console.log("Hello__7");

const marks=[1,543,65,3,4];
const mixed=['setr',3,34,34,[23,43,34]];

const arr = new Array(324,34,4,[35645,34]);
// console.log(arr);
// console.log(mixed);
// console.log(marks)


let obj = {
    'first name': "Abhishek",
    college: "Model College",
    marks: [34,34,324,32],
    'roll no': 323434,
    obj2: {
        first: 'a',
        second: 'b',
        third: {
            a: 2,
            b: "c",
            abc: [34,34,342,[342.345,435]]
        }
    }
};

console.table(obj.obj2.third.abc);