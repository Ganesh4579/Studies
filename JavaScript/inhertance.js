//parent constructor
const Vehicle = function (val) {
  this.wheelcount = val;
  this.getwheelcount = () => {
    console.log(this.wheelcount);
  };
};

//child constructor
const Car = function (val) {
  this.brand = val;
};

let v=new Vehicle(4);
Car.prototype=v;
let c=new Car("audi");
console.log(c.wheelcount);
