function call_back(cb) {
    console.log("Start call_back");
    cb();
    //console.log("End call_back");
}

function helper() {
    console.log("In helper function");
}

call_back(function() {
    console.log("Inside anonymous function");
})

call_back(helper);