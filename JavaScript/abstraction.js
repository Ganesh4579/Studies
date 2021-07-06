//abstract constructor
class Vehicle {
    constructor() {
        this.wheelcount = "none";
        Vehicle.prototype.getwheelcount = function () {
            console.log(this.wheelcount);
        };
        throw new Error("can't create obj of abstract constructor");
    }
}

//child constructor
class Car {
    constructor(val) {
        this.wheelcount = val;
    }
}

Car.prototype = Object.create(Vehicle.prototype);
let c = new Car(4);
c.getwheelcount();
