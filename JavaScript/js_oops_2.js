const objfunc = function (fname, lname) {
  //private members
  fname = fname;
  lname = lname;
  objfunc.prototype.grade = "good";

  Object.defineProperty(this, "fname", {
    get: () => {
      return fname + "\t";
    },
    set: (val) => {
      if (typeof val == "string") fname = val;
      else throw new Error("Not string type value");
    },
  });
  Object.defineProperty(this, "lname", {
    get: () => {
      return lname + "\t";
    },
    set: (val) => {
      if (typeof val == "string") lname = val;
      else throw new Error("Not string type value ");
    },
  });
};

let obj1 = new objfunc();
obj1.fname = "prakash";
obj1.lname = "S";
console.log(obj1.fname);
console.log(obj1.lname);
console.log(obj1.grade);
