let operation = function fileDownload(f) {
    return new Promise((res, rej) => {
      if (f) res("Processed");
      else rej("Not processed");
    });
  };
  
  let pro = operation(true);
  
  pro
    .then((str) => {
      operation(false).then(()=>{console.log("done")});
    })
    .catch((str) => {
      console.error("The thing ", str);
    });
  