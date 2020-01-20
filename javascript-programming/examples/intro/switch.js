"use strict";

var n = 42;

switch (n) {
  case 1: {
    console.log(1);
    break;
  };
  case 42: {
    console.log(42);
  };
  case 'other': {
    console.log('other');
  };
  default: {
    console.log('default')
  };

}

// 42
// other
// default
