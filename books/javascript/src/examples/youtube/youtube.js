
var btn_add = document.querySelector('#btn-add');
var btn_play = document.querySelector('#btn-play');

function get_songs() {
    var values_str = localStorage.getItem('songs');
    var values     = JSON.parse(values_str);
    //console.log(values);
    if (values == null) {
        values = [];
    }
    return values;
}

function list_songs() {
    var songs = get_songs();
    var html = '<ul>\n';
    for ( var i=0; i < songs.length; i++ ) {
        html += '<li><a href="' + songs[i] + '">' + songs[i] + '</a></li>\n';
    }
    html += '</ul>\n';
    song_list = document.querySelector('#song-list');
    song_list.innerHTML = html;
    //console.log(html);
    return;
}

btn_add.addEventListener('click', function() {
    text_song = document.querySelector('#song');
    song = text_song.value;
    //console.log(song);
//    var values_str = JSON.stringify(values);
//

    var values = get_songs();

    values.push(song);
    //console.log(values);

    var values_str = JSON.stringify(values);
    localStorage.setItem('songs', values_str);

    list_songs();

    return;
});

btn_play.addEventListener('click', function() {
    songs = get_songs();
    console.log(songs[0]);
    //displayVideo(songs[0]);
    displayVideo('CN11bI1_sZo');
});

// functions related to YouTube
function onYouTubePlayerReady(playerId) {
      ytplayer = document.getElementById("myytplayer");
	  ytplayer.addEventListener("onStateChange", "onytplayerStateChange");
	  //alert('loaded');
	  //ytplayer.cuePlaylist('I2rb0L5P2ME', 'DWW4vL_Zq_U');
}

function onytplayerStateChange(newState) {
   //alert("Player's new state: " + newState);
   ytplayer = document.getElementById("myytplayer");
   if (newState == 0) {
	var before = ytplayer.getVideoUrl();
	//alert(before);
    var after = before.replace(/.*v=(\w*)/, "$1");
	//alert(after);
    ytplayer.cueVideoById(after);
    //ytplayer.cueVideoByUrl(ytplayer.getVideoUrl());
   }
}

function displayVideo(id) {
    var params = { allowScriptAccess: "always" };
    var atts = { id: "myytplayer" };
    swfobject.embedSWF("http://www.youtube.com/v/" + id + "?enablejsapi=1&playerapiid=ytplayer&version=3",
                       "ytapiplayer", "853", "480", "8", null, null, params, atts);
}
// End YouTube functions


list_songs();



