"use strict";

var continents = new Array();
continents['na'] = "North America";
continents['sa'] = "South America";
continents['eu'] = "Europe";

var countries = new Array();
countries['na'] = new Array();
countries['sa'] = new Array();
countries['eu'] = new Array();
countries['na']['usa'] = "USA";
countries['na']['ca']  = "Canada";
countries['eu']['de']  = "Germany";
countries['eu']['at']  = "Austria";
countries['sa']['ch']  = "Chile";

function fill_continents() {
    document.reg.continent.length=1;
    document.reg.continent[0].value = "";
    document.reg.continent[0].text = "";
    for (c in continents) {
        var i = document.reg.continent.length++;
        document.reg.continent[i].value = c;
        document.reg.continent[i].text = continents[c];
    }

}
function change_continent() {
    var continent = document.reg.continent.value;
    document.reg.country.length=1;
    document.reg.country[0].value = "";
    document.reg.country[0].text = "";
    for (c in countries[continent]) {
        var i = document.reg.country.length++;
        document.reg.country[i].value = c;
        document.reg.country[i].text = countries[continent][c];
    }
}


function countries() {
   for(i=0; i<countries.length; i++) {
     alert(countries[i]);
   }
}


function submit_form() {
   //alert(reg.continent.value);
   countries();

   //alert(countries["us"]);
   //alert("done");
}
