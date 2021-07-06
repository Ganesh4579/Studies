function changeimage(event) {
  event = event || window.event;
  clickedimage = event.target || event.srcElement;
  if (clickedimage.tagName == "IMG") {
    document.getElementById("main").src = clickedimage.getAttribute("src");
  }
  console.log(event.target.tagName);  
}
function iover(){
    document.getElementById("main").style.cursor="hand";
    document.getElementById("main").style.border="3px solid red";
}
function iout(){
    document.getElementById("main").style.cursor="pointer";
    document.getElementById("main").style.border="3px solid gray";
}