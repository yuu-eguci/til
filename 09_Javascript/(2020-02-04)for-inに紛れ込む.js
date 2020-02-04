const obj = {
    a: 1,
    b: 2,
}

Object.prototype._e = 5;

for (let item in obj) {
    console.log(item+" - "+obj[item]);
}

/*

Output ↓
a - 1
b - 2
e - 5
e:5 が出てやがる!

*/


// こうすると紛れ込まない。
for (let item in obj) {
    if (obj.hasOwnProperty(item)) {
        console.log(item+" - "+obj[item]);
    }
}

/*


Output ↓
c - 3
d - 4

*/


// あるいはこうやって追加すれば紛れ込まない。
Object.defineProperty(Object.prototype, 'e', {
    value: 5
});
// function なら
Object.defineProperty(Array.prototype, 'insert', {
    value: function(x) { console.log(x); }
});
