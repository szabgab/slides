var t3000 = setTimeout(function() {
    console.log("Hello 3000");
}, 3000)

var t2000 = setTimeout(function() {
    console.log("Hello 2000");
}, 2000)

var t1000 = setTimeout(function() {
    console.log("Hello 1000");
    clearTimeout(t2000);
    console.log("cleared 2000");
}, 1000)

console.log("start")
