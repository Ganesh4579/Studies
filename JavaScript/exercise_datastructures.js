//generate a array of size(10) with random numbers
function getArray() { // creating a new array with random numbers
    let array = new Array(10);
    for (i = 0; i < array.length; i++) array[i] = Math.round(Math.random() * 100);
    return array;
}

function sum(array) { //this function is adding a array of elements
    let temp = 0;
    for (let i of array) temp += i;
    return temp;
}
console.log("\n")

function min(array) { //this function is for finding minimum value of an array 
    let temp = array[0];
    for (let i of array) if (temp > i) temp = i;
    return temp;
}

function max(array) { //this function is for finding maximum value of an array
    let temp = 0;
    for (let i of array) if (temp < i) temp = i;
    return temp;
}

function average(array) { //this function is for finding average value of an array
    return sum(array) / array.length;
}

let arr = getArray();
console.log("Random Array: \t\n", arr);


/*InBuilt Functions:
 console.log(Math.max(...arr) + "")
 console.log(Math.min(...arr) + "")*/

var map = new Map(); //Key as operation and value as a function
map.set("Addition", sum(arr));
map.set("Minimum", min(arr));
map.set("Maximum", max(arr));
map.set("Average", average(arr));

console.log("Available options: \t ");

for (let i of map.keys())  console.log("\t" + i);  //Iterating through keys

let option = "Maximum";
console.log("user option: \t" + option);

switch (option) { //Branching through option

    case "Addition":
        console.log("Adding all elements of given array:\t " + map.get(option));
        break;
    case "Minimum":
        console.log("Minimum value of given array:\t " + map.get(option));
        break;
    case "Maximum":
        console.log("Maximum value of given array:\t " + map.get(option));
        break;
    case "Average":
        console.log("Average value of given array:\t " + map.get(option));
        break;
    default:
        console.log(` ${option} is Invalid`)

}

//Bonus Ques 2
/*console.log("Adding all elements of given array:\t " + sum(arr));
console.log("Maximum value of given array:\t " + max(arr));
console.log("Minimum value of given array:\t " + min(arr));
console.log("Average value of given array:\t " + average(arr));*/