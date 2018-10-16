// alert("Hello World");
//問題２
// var num=1
// while (num<11) {
// if (num%2===0) {
//   console.log(num);
// }
// num = num+1
// }

// 問題３


//問題４

//足していく整数を設定
// var i = 1;
// x = prompt("値を入れてください");
// while (i <= x) {
//   i++;
// }




//変数 i に1から続く任意の整数を代入する。
var i = 1;

// 整数 1 からInputより受け取った整数になるまで処理いかを繰り返す。
x = prompt("値代入してください")
while (i<= x) {

// 変数 i が 3 で割り切れるなら"Fizz"をalert表示する。
if (i%3===0) {
  alert("Fizz");
}

// 変数 i が 5 で割り切れるなら"Buzz"をalert表示する。
if (i%5===0) {
  alert("Buzz");
}

// 変数 i が 3 と 5 のどちらでも割り切れるなら”FizzBuzz”をalert表
if (i%3===0 && i%5===0) {
  alert("FizzBuzz")
}
// その他の場合は　i の値を出力
else {
  alert(i)
}
i++
}
