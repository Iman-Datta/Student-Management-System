$(document).ready(function (){
    console.log('We are using JQuery');

    $('#btnRegister').click(function (event){
        event.preventDefault();
        console.log('Button Click');

        const stream_name = $('#stream_name').val();
        const csrf_token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            url:'/add/',
            method: 'POST',
            data: {
                stream_name: stream_name,
                csrf_token: csrf_token
            },
            sucess: function(response){

            },
            error: function(error) {
                
            }
        });
        
    });
});