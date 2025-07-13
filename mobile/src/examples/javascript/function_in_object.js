var math = {
  'add' : function(x, y) {
    var z = x+y;
    return z;
  }
};

console.log(math['add'](2, 3));      // 5

math['multiply'] = function(x, y) { return x * y };

console.log(math['multiply'](2, 3)); // 6

