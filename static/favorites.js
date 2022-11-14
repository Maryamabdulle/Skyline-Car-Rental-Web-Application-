$(window).on("load", function(){
    $('.btn.btn-outline-dark.fav-button').each(function(i,obj){
        $.get('/check_favorites/'+obj.favorites_id,response => {
            console.log(typeof response)
            if(response=='true'){
                $(this).addClass('btn btn btn-warning fav-button')
            }else{
                $(this).addClass('btn btn-outline-dark fav-button')
            }
        })
    });
});


$("button.fav-button").click(function(){
    if($(this).attr('class')== "btn btn-outline-dark fav-button"){
        $post('/favorite_action/'+ this.favorite_id, response => {
            console.log(response)
            if(response =="Add car"){
                $(this).removeClass('btn btn-outline-dark fav-button')
                $(this).addClass('btn btn btn-warning fav-button')
            }
        });
}else{
    $.post('/favorite_action/'+ this.favorite_id, response => {
        console.log(response)
        if(response=="Removed car"){
            $(this). removeClass('btn btn btn-warning fav-button')
            $(this).addClass('btn btn-outline-dark fav-button')
        }
    });
    }
});

document.getElementById("btn").addEventListener(
    "click",
    function(event) {
      if (event.target.value === "Submit") {
        event.target.value = "Saved";
      } else {
        event.target.value = "Save";
      }
    },
    false
  );
  