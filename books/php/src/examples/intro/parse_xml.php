<?php
$file = "data.xml";
$depth = array();

function startElement($parser, $name, $attrs) {
    global $debth;
    for ($i = 0; $i < $depth[$parser]; $i++) {
        echo "   ";
    }
    echo "\n";
    $depth[$parser]++;
}


$xml_parser = xml_parser_create();
xml_set_element_handler($xml_parser, "startElement");
 


?>
