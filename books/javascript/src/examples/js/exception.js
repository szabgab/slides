function add(x, y) {
    if (Number(x) !== x) {
        throw {
            'name': 'TypeError',
            'message': 'First argument is not a number'
        };
    }
    if (Number(y) !== y) {
        throw {
            'name': 'AnyNameCanComeHere',
            'message': 'Second argument is not a number'
        };
    }
    return x+y;
}

var arr = [
    [2, 3],
    ['two', 3],
    [2, 'three'],
    [7, 9]
];
var i, res;
for (i=0; i<arr.length; i++) {
    v = arr[i];
    console.log(v);
    try {
        res = add(v[0], v[1]);
    } catch(e) {
        console.log('exception:', e);

    }
    console.log(res);
}
