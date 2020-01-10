document.onkeyup = KeyCheck;
function aKeyCheck(e) {
    alert(document.getElementById('prev'));
    alert(document.getElementById('next'));
}

var extension     = "";

function KeyCheck(e) {
    var ev = (window.event) ? event : e;
    var KeyID = ev.keyCode;
    if (ev.ctrlKey) {
        return;
    }
    //console.log(ev.ctrlKey);
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

        case 67:
            // c
            go_chapter_toc();
            break;

        case 72:
            // h
            // hide/show .remark classes
            //alert(72);
            toggle_extras(true);
            break;

        case 73:
          // i
          //
          document.location.href = "index" + get_extension();
          break;

        case 75:
            // k
            document.location.href = "keywords" + get_extension();
            break;

        case 84:
            // t
            document.location.href = "toc" + get_extension();
            break;

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
            alert("? - this help\n-> next\n<- - prev\nSPACE - next\ni - index\nk - keywords\nt - toc\nh - toggle extra text\nc - chapter TOC\n");
            //PgUp - prev\nPgDown - next
        break;

        //default:
        //    alert(KeyID);
   }
}

function go_chapter_toc() {
    var the_page     = document.getElementById('chapter');
    if (the_page) {
        document.location.href = the_page;
    } else {
        alert('Sorry, there are no chapter TOC');
    }
}


function go_next() {
    var next_page     = document.getElementById('next');
    if (next_page) {
        document.location.href = next_page;
    } else {
        alert('Sorry, there are no further pages');
    }
}

function go_prev() {
    var previous_page = document.getElementById('prev');
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
    toggle_extras(false)
}

function toggle_extras(toggle) {
    //console.log('toggle')
    //console.log('show_extra was: ' + t);
    var t = localStorage.getItem('show_extra');
    //console.log(t)
    if (t === null) {
        // defaults to show extras
        t = true;
    } else {
        t = JSON.parse(t);
    }
    if (toggle) {
        t = ! t;
    }
    localStorage.setItem("show_extra", t);
    //console.log('Toggle to ' + t);
    show_extras(t)
}

function show_extras(t) {
    //console.log('show_extras:', t);
    var nl = document.getElementsByClassName('extra');
    for (var i = 0; i < nl.length; i++) {
        //console.log('setting ');
        nl[i].style.display = t ? "block" : "none";
    }
}

function get_extension() {
    var obj = document.getElementById('extension');
    return obj.value;
}

setTimeout(start_extras, 100)
var obj = document.getElementById('showhide');
function showhide() {
    toggle_extras(true);
}
obj.addEventListener('click', showhide)



