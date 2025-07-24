"use strict";

var hidden = Math.round(Math.random()*200+0.5);
console.log(hidden);

// ramat chaim => 'חיים רמת'

// 'ch' : 'ח'
var tr = {
    a: 'א',
    b: 'ב',
    c: '',
    d: 'ד',
    e: '',
    f: 'פ',
    g: 'ג',
    h: '',
    i: 'י',
    j: '',
    k: '',
    l: 'ל',
    m: 'מ',
    n: 'נ',
    o: 'ו',
    p: '',
    q: '',
    r: 'ר',
    s: 'ש',
    t: 'ת',
    ' ': ' '
}

function transliterate() {
    var latin = document.getElementById('latin').value;
    var result = '';
    var i;
    for (i = 0; i < latin.length; i++) {
        console.log(latin[i]);
        if (tr[ latin[i]] ) {
            result += tr[ latin[i]];
        }
    }
    document.getElementById('result').innerHTML = result;
    return false;
}

document.getElementById('latin').addEventListener('keyup', transliterate);
