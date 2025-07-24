"use strict";

check_null(null);
check_null({});
check_null(42);

function check_null(x) {
    console.log(typeof x);
    console.log(x === null ? "null" : "not null");
    console.log(x && typeof x === 'object' ? "object" : "null");
}
