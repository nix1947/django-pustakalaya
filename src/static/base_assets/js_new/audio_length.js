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
   });
