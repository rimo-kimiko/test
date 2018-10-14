var firstName = prompt("First Name Please:")
var lastName = prompt("Last Name please:")
var age = prompt("how old are you?")
var height = prompt("What is your height?")
var petName = prompt("What is your pet name?")
alert("Thank you so much for the information")

//Name condition
var nameCond = null;
var ageCond = null;
var heightCond = null;
var petCond= null;

if (firstName［0］) === lastName［0］{
  nameCond = true;
}else {
  nameCond = fales;
}

//Age conditions
if (age>20 && age < 30) {
  ageCond = true;
}else {
  ageCond = false;
}

//height conditions
if (heiht >=170) {
  heightCond = true;

}else {
  heightCond = false;
}

//pet name
if (petName［petName.length-1］=== "y") {
  petCond = true;
}else {
  petCond = false;
}

//check all conditoion
if (nameCond && ageCond && heightCond && petCond) {
console.log("Welcome Spy");
}else {
  console.log("Nothng to see here");
}
