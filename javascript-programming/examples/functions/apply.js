var f = function() {
    console.log(this);
}

var x = { fname: 'Gabor'};

f.apply(x, [2, 3]);
