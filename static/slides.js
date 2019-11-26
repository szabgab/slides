document.onkeyup = KeyCheck;
function aKeyCheck(e) {
    alert(document.getElementById('prev'));
    alert(document.getElementById('next'));
}

//var extension     = ".html";
var extension     = "";
var previous_page = document.getElementById('prev');
var next_page     = document.getElementById('next');
var toc           = "toc" + extension;
var index         = "index" + extension;
var keywords      = "keywords" + extension;

function KeyCheck(e) {
    var KeyID = (window.event) ? event.keyCode : e.keyCode;
    //console.log(KeyID);
    switch(KeyID) {
        //case 16:
        //document.Form1.KeyName.value = "Shift";
        //break;
        //case 17:
        //document.Form1.KeyName.value = "Ctrl";
        //break;
        //case 18:
        //document.Form1.KeyName.value = "Alt";
        //break;

        case 19:
            //"Pause";
            break;

        case 27:
            // 27 (ESC), 116 (F5) alternating when clicking the lower left button on R400
            break

        case 32:
            // Space
            go_next();
            break;

        //case 34:
        //  go_next();
        //  // PageDown
        //  break;

        case 37:
            // Arrow Left
            go_prev()
            break;

        case 38:
          // Arrow Up
          break;

        case 39:
            // Arrow Right
            go_next();
            break;

        case 40:
            //"Arrow Down";
            break;

        case 66:
            // 66 (b) when clicking the lower right on Logitech R400
            window.history.back();
            break;

        case 72:
            // h
            // hide/show .remark classes
            //alert(72);
            toggle_extras();
            break;

        case 73:
          // i
          document.location.href = index;
          break;

        case 75:
            // k
            document.location.href = keywords;
            break;

        //case 84:
        //    // t
        //    document.location.href = toc;
        //    break;

        // PageDown and PageUp might be useful in courses but not on the edumaven site
        // The buttons of the Logitech R400 remote are generating PageUp and PageDown hits
        //case 33:
        //   // PageUp
        //   go_prev();
        //   break;


        case 116:
            // F5
            break;

        case 191:
            // ?
            alert("? - this help\n-> next\n<- - prev\nSPACE - next\ni - index\nk - keywords\n");
            //alert(t - toc\nh - toggle extra text\n");
            //PgUp - prev\nPgDown - next
        break;

        //default:
        //    alert(KeyID);
   }
}

function go_next() {
    if (next_page) {
        document.location.href = next_page;
    } else {
        alert('Sorry, there are no further pages');
    }
}

function go_prev() {
    if (previous_page) {
        document.location.href = previous_page;
    } else {
        alert('Sorry, there is no previous page.');
    }
}

function set_extra_default(v) {
    var t = localStorage.getItem('show_extra');
    //console.log('show_extra: ' + t);
    if (t === null) {
        t = v;
        //console.log('Set default to ' + t);
    } else {
        t = JSON.parse(t);
    }
    localStorage.setItem("show_extra", t);
    show_extras(t);
}

function start_extras() {
    console.log('start')
    var t = localStorage.getItem('show_extra');
    console.log(t)
    if (t === null) {
        //console.log('false is null');
        t = true;
    }
    localStorage.setItem("show_extra", t);
    show_extras(t)
}

function toggle_extras() {
    console.log('toggle')
    //console.log('show_extra was: ' + t);
    var t = localStorage.getItem('show_extra');
    console.log(t)
    if (t === null) {
        //console.log('false is null');
        t = false;
    } else {
        t = JSON.parse(t);
    }
    t = ! t;
    localStorage.setItem("show_extra", t);
    //console.log('Toggle to ' + t);
    show_extras(t)
}

function show_extras(t) {
    var nl = document.getElementsByClassName('extra');
    for (var i = 0; i < nl.length; i++) {
        //console.log('setting ' + t);
        nl[i].style.display = t ? "block" : "none";
    }
}

setTimeout(start_extras, 500)


