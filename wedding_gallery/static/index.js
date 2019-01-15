$(function(){
    $('button[name=like]').on('click', function(){
        var photo_id = this.id
        $.getJSON($SCRIPT_ROOT + '/do_like', {
            photo_id: photo_id
        }, function(data){
            if(data.not_logged == true){
                window.location.href = $SCRIPT_ROOT + '/login'
            };
            if(typeof data.number_of_likes == 'number'){
                $('div.number_of_likes#' + photo_id).text(data.number_of_likes + ' ♥');
            };
        });
        return false;
    })
})
