const {parseArgs} = require('node:util');
const calc = require("./mycalc.js");


const args = process.argv;
if (args.length != 4) {
    console.log(`Usage ${args[1]} X Y`);
    process.exit(1);
}

console.log(calc.add(args[2], args[3]));
