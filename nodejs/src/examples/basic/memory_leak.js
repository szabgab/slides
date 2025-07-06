// This does not show it properly


function create() {
    let left = {
        "name" : "Left"
    };
    let right = {
        "name" : "Right"
    };
    left["other"] = right;
    //right["other"] = left;
    //console.log(left);
    left["payload"] = "a".repeat(1000000);
}

//create();
const used = process.memoryUsage().heapUsed / 1024 / 1024;
console.log(`The script uses approximately ${Math.round(used * 100) / 100} MB`);

const before = process.memoryUsage();
for (let i = 0; i < 10000000; i++) {
    create()
}
const after = process.memoryUsage();
const headDiff = after.heapUsed-before.heapUsed;

console.log(headDiff);

