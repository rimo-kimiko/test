alert("Hello");
var hot =false
var temp= 35


if (true) {
  console.log("I ran");
}

if (temp>80) {
hot=true
}
console.log(hot);

if(temp>80){
  console.log("Hot Outsidee");
}else {
  console.log("Its not very hot today");
}

if (temp>80) {
  console.log("Hot outside!");
}else if (temp<=80 && temp>=50) {
console.log("Average temp Outside");
}else if (temp < 50 && temp>= 32) {
  console.log("Its pretty cold out!");
}else {
  console.log("It is very cold out");
}


var ham=0;
var cheese =0;

var report = "blank";

if (ham>= 10 && cheese >= 10) {
  report = "Strong sales of both ham and cheese!"
}else if (ham===0 && cheese===0) {
  report = "Nothing Sold!"
}else {
  report = "We had some sales of items"
}
console.log(report);
