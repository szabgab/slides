var intervalId = setInterval(function() {
    console.log("world");
}, 1000);

setTimeout(function() {
    console.log("Calling clearInterval");
    clearInterval(intervalId);
}, 3030);

console.log("hello");
