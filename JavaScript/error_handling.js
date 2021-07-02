try {
  //console.log(g);
  //func();
  throw {
    error: "jus an err",
    message: "gosh!",
    description: "jus an err",
  };
} catch (e) {
  console.log(e.description);
  console.log(e.message);
  console.log(e.stack);
}
//  var g=1;
//function func() {};