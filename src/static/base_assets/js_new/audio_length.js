 // Calculate AudioLength
 $(document).ready(function(){

    function getDuration(src) {
        return new Promise(function(resolve) {
            var audio = new Audio();
            $(audio).on("loadedmetadata", function(){
                resolve(audio.duration);
            });
            audio.src = src;
        });
    }
    function duration(duration){

        var minutes = parseInt(duration / 60, 10);
        var seconds = parseInt(duration % 60);
        return minutes+":"+seconds
  }

    $.each($('.calculateAudioLength'), function(index, value) {
        getDuration(value.src)
        .then(function(length) {
            console.log('I got length ' + length);
            $(value).parent().text(duration(length));
        });
    });


    //These two function are for getting video durations
    $.each($('.calculateVideoLength'), function(index, value) {
        getDuration(value.src)
        .then(function(length) {
            $(value).siblings('.videoduration').text(duration(length));
        });
    });


    function getDuration(src) {
        return new Promise(function(resolve) {
            var video = document.createElement("video");
            $(video).on("loadedmetadata", function(){
                resolve(video.duration);
            });
            video.src = src;
        });
    }
    // end video duration


   });
