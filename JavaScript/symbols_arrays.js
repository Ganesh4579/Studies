let l = Symbol("to");
let k = Symbol("to");
console.log(l === k);
console.log("to" == k);
console.log(Symbol("M").valueOf().toString());

let arr = [1, 2, 3, 4, 5];
console.log(arr);
arr1 = arr.concat([6, 7]);
console.log(arr1);
console.log(arr.join(":"));
console.log(arr.slice(2, 4));
arr.push(6);
arr.push([7, 8]);
arr.push(9);
arr.pop(9);
arr.forEach((v, i) => {
  console.log(`${i}  ${v}`);
});
console.log(arr[6][1]);
console.log(arr1.splice(1, 4, 1000, 10000, 1000));
console.log(arr1);

for (let i = 0; i < arr.length; i++) console.log(arr[i]);
for (let i of arr) console.log(i);
for (let i in arr) console.log(arr[i]);

console.log("\n\n" + arr);
arr.splice(0, 1);
console.log(arr);

var arr2 = new Array(3);
arr2[2] = 4;
console.log(arr2);

gss = [1, 2, 3, 4, 5, 6];
console.log("\n\n" + gss);
console.log(
  gss.filter((v, i, a) => {
    if (v % 2 == 0) return true;
    else return false;
  })
);
