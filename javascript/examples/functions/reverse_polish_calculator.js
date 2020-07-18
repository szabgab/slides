"use strict";

function RPN() {
    var stack = [];
    var f = function() {
    };
    f.size = function() {
        return stack.length;
    }
    f.exe = function(v) {
        if (v === '+') {
            var res = stack.pop() + stack.pop();
            stack.push(res);
            return;
        }
        if (v === '*') {
            var res = stack.pop() * stack.pop();
            stack.push(res);
            return;
        }
        if (v === '-') {
            var res = stack.pop() - stack.pop();
            stack.push(res);
            return;
        }
        if (v === '/') {
            var res = stack.pop() / stack.pop();
            stack.push(res);
            return;
        }
        if (v === '=') {
            return stack.pop();
        }
        stack.push(v);
    };
    return f;
}

var r = RPN();
r.exe(2);
r.exe(3);
r.exe(4);
console.log(r.size());     // 3
r.exe('+');
r.exe('*');
console.log(r.exe('='));   // 14
console.log(r.size());     // 0
r.exe(6);
r.exe(2);
r.exe('-');
console.log(r.exe('='));   // -4
