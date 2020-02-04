const obj = {
    a: 1,
    b: 2,
}

const obj2 = {
    c: 3,
    d: 4,
}

Object.prototype.e = 5;

for (let item in obj) {
    console.log(item+" - "+obj[item]);
}

for (let item in obj2) {
    console.log(item+" - "+obj2[item]);
}

/*

Output ↓
a - 1
b - 2
e - 5
c - 3
d - 4
e - 5
毎回、 e:5 が出てやがる!

*/
