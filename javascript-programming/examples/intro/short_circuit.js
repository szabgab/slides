"use strict";

var salary = 8000;
var money = 100000;

function check_standard_of_living() {
    if (money > 1000000 || salary++ > 10000) {
        console.log('I can live well.');
    }
    console.log('I have ' + money + ' in the bank and I get ' + salary + ' as salary.')
}

check_standard_of_living();
check_standard_of_living();
check_standard_of_living();

money = 2000000;
check_standard_of_living();
check_standard_of_living();
check_standard_of_living();
