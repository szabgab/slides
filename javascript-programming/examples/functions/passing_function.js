var add = function (a, b) {
    return a+b;
}
var subtract = function (a, b) {
    return a-b;
}

var handle_data = function (func) {
    // get data from user or other external source
    var x = 2;
    var y = 3;
    return func(x, y);
}

console.log(handle_data(add));       // 5
console.log(handle_data(subtract));  // -1
