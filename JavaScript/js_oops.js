//obj creation using constructor
const objfunc = function (fname, lname) {
  this.fname = fname;
  this.lname = lname;
};

let obj = new objfunc("Ganesh", "S");
console.log(obj);

//obj creation using literal notation

let obj1 = {
  fname: "Ganesh",
  lname: "S",
};
console.log(obj1);

//scope private,privileged and public function
const cust = function (fname, lname) {
  this.fname = fname;
  this.lname = lname;

  //private function
  var getName = () => {
    console.log(this.fname + " " + this.lname);
  };

  //privileged function
  this.getNameOfCust = () => {
    return getName();
  };

  //public function
  cust.prototype.getSalary = () => {
    console.log(10000);
  };
};

let cust1 = new cust("pacha", "ma");
cust1.getNameOfCust();
cust1.getSalary();
