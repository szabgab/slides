var cfg = {
    textExtraction: function(node) {
        var $node = $(node);
        var sort = $node.attr("sort");
        if (!sort) { return $node.text(); }
        if ($node.hasClass("date")) {
            return (new Date(sort)).getTime();
        } else {
           return sort;
       }
   }
};
$("#items-table").tablesorter(cfg);

