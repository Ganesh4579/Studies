document.getElementById("d").innerText = 0;
let incr = function () {
  document.getElementById("d").innerText++;
  document.getElementById("cont").innerHTML = "<br/> " + event.type + "<br/>";
};

let formValid = function () {
  let t = document.getElementById("mail").value + "";
  if (t.includes("@") && confirm("Are you sure"))
    alert("you entered mail \t" + t);
  else alert("you entered mail is not valid \t" + t);
};
