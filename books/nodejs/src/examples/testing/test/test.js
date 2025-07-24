var assert = require('assert');

const calc = require("./calc.js")

describe('Array', function() {
  describe('calc', function() {
    it('should be ok', function() {
      assert.equal(calc.add(2, 7), 9);
    });
  });
});

