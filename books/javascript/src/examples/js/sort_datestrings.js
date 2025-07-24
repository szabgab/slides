"use strict";

var dates = ['2013-04-02', '2012-05-06', '2014-10-10'];
console.log(dates);
console.log(dates.sort());
console.log(dates);
var dates = [
    {
        'd' : '2013-04-02',
        'n' : 'one'
    },
    {
        'd' : '2012-05-06',
        'n' : 'two'
    },
    {
        'd' : '2014-10-10',
        'n' : 'three'
    }
];
console.log(JSON.stringify(dates, undefined, 2));
dates.sort(function(a, b) { return a['d'].localeCompare(b['d']) });
console.log(JSON.stringify(dates, undefined, 2));
