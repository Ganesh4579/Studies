function sq() {
  return (x) => {
    return x;
  };
}
var t = sq();
console.log(t(12));

let q = "asajhds";
let v = "hi  ${q}";
console.log(v);

var func = function (n) {
  if (n > 0) {
    console.log(n);
    n--;
    return func(n);
  }
};
func(10);

