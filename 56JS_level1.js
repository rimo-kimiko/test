// 1
var x = 0;

while (x < 5)  {
  console.log("x is currently: "+x);
  console.log("x is still less than 5, adding 1 to x");
x = x+1;
}

// 2
var x = 0;

while (x < 5)  {
  console.log("x is currently: "+x);

if (x===3)
  console.log("x is equarl to three!");

console.log("x is still less than 5,adding 1 to x");

x = x+1;
}

// 3
var x =0;

while (x<5) {
  console.log("x is currently: "+x);

if (x===3) {
  console.log("x is equal to three!");
  break;
}

console.log("x is still less than 5,adding 1 to x");
x = x+1
}

//write while loop that prints out
// only the even number from 1 to 10.
var num=1
while (num<11) {
console.log(num);
num = num +1;
}

var num=1
while (num<11) {
if (num%2===0) {
  console.log(num);
}
num = num+1;
}
