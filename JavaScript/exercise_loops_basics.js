/*
var st="#";
for(var i=0;i<7;i++){
    console.log(st);
    st=st+"#";
}


var st="";
for(var i=0;i<8;i++){

}
*/
var n = 8,
  st = "";

for (var i = 0; i < n; i++) {
  for (var j = 0; j < n; j++) {
    if ((j % 2 === 0 && i % 2 === 0) || (j % 2 === 1 && i % 2 === 1)) {
      st += " ";
    } else {
      st += "#";
    }
  }
  st += "\n";
}
console.log(st);
