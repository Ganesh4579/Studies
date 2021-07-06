let y = new Object();
y.op = "HI";
y.oq = "WELCOME";
let h = {
  get: function (obj, name) {
    if (name in obj) return "jdkjfkjfkdf";
    else return "Error";
  },
};
let pro = new Proxy(y, h);

console.log(pro.ohp);

//////////////

