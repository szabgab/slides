
function createCounter(n) {
    function counter(v) {
        return v + n;
    }
    return counter;
}

var counter_3 = createCounter(3);

console.log(counter_3(7));

var counter_4 = createCounter(4);

console.log(counter_3(7));
console.log(counter_4(7));
