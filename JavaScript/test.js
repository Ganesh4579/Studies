console.log("Hi");

var a;
console.log(a);
console.log(typeof a);

var b = 12.545454545;
console.log(typeof b);

console.log(typeof console);

console.log("\n\n");

var q = "false";
if (q) {
  console.log(q);
}

console.log(typeof 2 / 0);
console.log(typeof {});

for (var i = 0; i < 10; i++) {
  //console.log(i);
}

var i = 0;
while (i < 10) {
  //console.log(i);
  i++;
}

i = 0;
do {
  //console.log(i);
  i++;
} while (i < 10);

i = 0;
while (i <= 10) {
  //if(i%2!=0) console.log(i);
  i++;
}
i = 0;
console.log(i);
console.log(i++);
console.log(i);

console.log("\n\n");

let arr = [1, 6, 2, 8, 9, 0]; //new Array();
console.log(arr.toString());
for (let i in arr) console.log(i);
for (let i of arr) console.log(i);

console.log("\n\n\n");

let fu = function () {
  console.log(arguments);
};
fu(1, 2, 3, 4, 5);
