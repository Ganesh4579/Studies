let pone = new Promise((res, rej) => {});
console.log(pone);

let pfunc = (f) => {
  return new Promise((res, rej) => {
    if (f) res("Hi");
    else rej("NO");
  });
};

let p = pfunc(false);
p.then((d) => {
  console.log(`${d}  welcome`);
}).catch((d) => {
  console.log(`${d}  welcome`);
});

//////////////


let p1=new Promise((res,rej)=>{
    setTimeout(()=>{res("p1")},2000)
})
let p2=new Promise((res,rej)=>{
    setTimeout(()=>{res("p2")},1000)
})
let p3=new Promise((res,rej)=>{
    setTimeout(()=>{res("p3")},1000)
})

Promise.all([p1,p2,p3]).then((f)=>{console.log(`${f}  done`)})

//////////////


let getp=(f)=>{
    if(f) return Promise;
    else throw new Error();
}

p1.then((f)=>{console.log(f)
getp(true)}).then(()=>{console.log("Everthing done")})