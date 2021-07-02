document.getElementById("d").innerText = 0;
let incr = function () {
  document.getElementById("d").innerText ++;
};

let formValid=function(){
  let t=document.getElementById("mail").value+"";
  if(t.includes("@")) alert("you entered mail \t"+t);
  else alert("you entered mail is not valid \t"+t);
}