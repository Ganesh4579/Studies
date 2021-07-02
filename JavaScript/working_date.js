console.log(new Date());
console.log(new Date("January 23"));

function func() {
  console.log("HI");
}
let int = setInterval(func, 1000);
clearInterval(int);
