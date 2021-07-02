for (var i = 1; i <= 100; i++) {
  if (i % 3 == 0 && i % 5 == 0) console.log(i + "\tFizzBuzz");
  else if (i % 3 == 0) console.log(i + "\tFizz");
  else if (i % 5 == 0) console.log(i + "\tBuzz");
  else console.log(i);
}
