/*
var min = function (a, b) {
  return a > b ? b : a;
};
console.log("The Minimum value is " + min(23, 85));

/////////////

var checkValid = function (n) {
  return n >= 100 || n <= 1000; 
};
var isPrime = function (n) {
  if (n <= 1) return false;

  for (let i = 2; i < n; i++) {
    if (n % i == 0) return false;
  }

  return true;
};
var isEndsWith3 = function (n) {
  let n1 = String(n);
  return n1[n1.length - 1] == 3;
};

var num = 183;

if (!checkValid(num)) console.log(`${num} is not valid`) ;
if (isEndsWith3(num)) console.log(`${num} should not end with 3`);
if (isPrime(num)) console.log(`${num} You shouldn"t enter prime number`);

//else console.log(`${num} is valid');
*/

///////

var checkValid = function (n) {
  return n.length >= 10 && n.length <= 20;
};
var Mix = function (n) {
  return (
    String(n).toLowerCase == String(n) && String(n).toUpperCase == String(n)
  );
};
var notchar = function (n) {
  return String(n).includes("(") || String(n).includes(")");
};
var fullstop = function (n) {
  return String(n)[String(n).length - 1] == ".";
  //return n.includes(".");
};

var num = "JavaScript is good.";
if (!checkValid(num)) console.log(`${num} should between 10 to 20`);
if (!Mix) console.log(`${num} should be mixed with uppercase and lowercase letters`);
if (notchar) console.log(`${num} should not contain (or) characters`);
if (fullstop) console.log(`${num} should not end with "."`);

///////
/*

function tables(x) {
  function innertable() {
    for (var i = 1; i <= 10; i++) {
      console.log(`${x}   x   ${i}  = ${ (x * i)}`);
    }
  }
  return innertable;
}
var m = tables(5);
m();
*/

///////
