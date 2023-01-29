var assert = require('assert');

const calc = require("../mycalc.js")

describe('Array', function() {
  describe('calc', function() {
    it('should be ok', function() {
      assert.equal(calc.add(2, 2), 4);
    });
    it('should be ok', function() {
      assert.equal(calc.add(2, 3), 5);
    });
  });
});

