let obj = {};
console.log(obj);
obj.name = "Ganesh";
obj.num = "10001";
obj["num"] = "1023";
console.log(obj);
let obj1 = new Object();
obj1.name = "Ganesh";
obj1.func = function () {
  console.log(this.name);
};
console.log(obj1);
obj1.func();
var f = (g) => {
  console.log("f : " + g.name);
};
f(obj1);
console.log("\n");
var f1 = (g) => {
  console.log("f : " + g);
};
f1.call(null, "kl");
f.call(obj1, obj1);
console.log(...[1, 2, 3]);

console.log(Math.max.apply(null, [1, 2, 3]));

let b = new Array(2);
var f1 = (g) => {
  console.log("f : " + g);
};
console.log("\n");
f1(b);
for (let i of Object.entries(obj1)) {
  console.log(i);
}
for (let [i, j] of Object.entries(obj1)) {
  console.log(i + j);
}
console.log(obj1.func);
console.log(Object.is("ww", "ww"));
