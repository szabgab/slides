(function() {
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

            case 65:
                // a
                //
                document.location.href = "admin"  + get_extension() + "?frompath=" + baseName(window.location.pathname);
                break;

            case 66:
                // 66 (b) when clicking the lower right on Logitech R400
                window.history.back();
                break;

            case 67:
                // c
                break;

            case 68:
                // d
                go_chapter_toc();
                break;
            // 69 e
            // 70 f
            // 71 g

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
            // 74 j

            case 75:
                // k
                document.location.href = "keywords" + get_extension();
                break;
            // l
            // m
            case 78:
                // n
                toggle_navigation(true);
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
                alert("? - this help\n-> next\n<- - prev\nSPACE - next\ni - index\nk - keywords\nt - toc\nd - chapter TOC\nh - toggle extra text\nn - toggle navigation\n");
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
        var show = localStorage.getItem('show_extra');
        //console.log('show_extra: ' + show);
        if (show === null) {
            show = v;
            //console.log('Set default to ' + show);
        } else {
            show = JSON.parse(show);
        }
        localStorage.setItem("show_extra", show);
        show_extras(show);
    }

    function start_extras() {
        toggle_extras(false)
    }
    function start_navigation() {
        toggle_navigation(false)
    }

    function toggle_extras(toggle) {
        //console.log('toggle')
        var show = get_field('show_extra');
        //console.log('show_extra was: ' + show);
        if (toggle) {
            show = ! show;
        }
        localStorage.setItem("show_extra", show);
        //console.log('Toggle to ' + show);
        show_extras(show)
    }
    function toggle_navigation(toggle) {
        //console.log('toggle')
        var show = get_field('show_navigation');
        //console.log('show_extra was: ' + show);
        if (toggle) {
            show = ! show;
        }
        localStorage.setItem("show_navigation", show);
        //console.log('Toggle to ' + show);
        show_navigation(show)
    }


    function get_field(name) {
        var show = localStorage.getItem(name);
        if (show === null) {
             show = true; // default
        } else {
            show = JSON.parse(show);
        }
        return show;
    }

    function show_banners() {
        var show = get_field('show_banner');
        show_things('banner', show);
        if (show) {
            var top = document.getElementById('banner-top');
            var path = window.location.pathname;
            // var re = new RegExp('/docker/');
            //if (re.exec(path)) {
            //    return;
            //}

            var msg = 'You are reading one of the thousands of slides on the <a href="/">Code-Maven</a> site. Check out <a href="/slides/">all the slides</a>.';
            //top.innerHTML = msg;
            //top.setAttribute('style', 'background-color: #42e8f4;');
            //background-color: orange'
        }
    }

    function show_extras(show) {
        show_things('extra', show);
    }

    function show_navigation(show) {
        show_things('navigation', show);
    }

    function show_things(what, show) {
        //console.log('show', what, t);
        var nl = document.getElementsByClassName(what);
        for (var i = 0; i < nl.length; i++) {
            nl[i].style.display = show ? "block" : "none";
        }
    }

    function get_extension() {
        var obj = document.getElementById('extension');
        return obj.value;
    }

    function baseName(str) {
        var base = new String(str).substring(str.lastIndexOf('/') + 1);
        return base;
    }

    start_extras();
    start_navigation();
    show_banners();
    var showhide = document.getElementById('showhide');
    if (showhide) {
        showhide.addEventListener('click', function () { toggle_extras(true) })
    }

    //var start_xPos;
    //var start_yPos;
    //var start_time;
    //function touch_start(event) {
    //    start_xPos = event.touches[0].pageX;
    //    start_yPos = event.touches[0].pageY;
    //    start_time = new Date();
    //}


    //function touch_end(event) {
    //    var end_xPos = event.changedTouches[0].pageX;
    //    var end_yPos = event.changedTouches[0].pageY;
    //    var end_time = new Date();
    //    let move_x = end_xPos - start_xPos;
    //    let move_y = end_yPos - start_yPos;
    //    let elapsed_time = end_time - start_time;
    //    if (Math.abs(move_x) > 30 && Math.abs(move_y) < 30 && elapsed_time < 1000) {
    //        if (move_x < 0) {
    //            //alert("left");
    //            go_next();
    //        } else {
    //            //alert("right");
    //            go_prev();
    //        }
    //    }
    //}

    //var content = document.getElementById("content");
    //content.addEventListener('touchstart', touch_start);
    //content.addEventListener('touchend', touch_end);

})();

