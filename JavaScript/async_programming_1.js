let operation = function fileDownload(f) {
  return new Promise((res, rej) => {
    if (f) res("Processed");
    else rej("Not processed");
  });
};

let pro = operation(false);

pro
  .then((str) => {
    console.log("The thing ", str);
  })
  .catch((str) => {
    console.error("The thing ", str);
  });

console.log("\n\n");

let pro1 = () => {
  return new Promise((res, rej) => {
     setTimeOut(() => {
      if(true) res("1 done");
    }, 2000);
  });
};
let pro2 = () => {
  return new Promise((res, rej) => {
     setTimeOut(() => {
      if(true) res("2 done");
    }, 1000);
  });
};
let pro3 = () => {
  return new Promise((res, rej) => {
     setTimeOut(() => {
      if(true) res("3 done");
    }, 1500);
  });
};

Promise.all([pro1(), pro2(), pro3()]).then((str) => {
  console.log(str)});
