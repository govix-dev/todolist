var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'; // Check https://jquery.com/ for the current version
document.getElementsByTagName('head')[0].appendChild(script);

function send_data(){
    
var task=document.getElementById("inp-box1").value;
var detail=document.getElementById("inp-box2").value;

$.ajax({ 
    url: '{{url_for('/')}}', 
    type: 'POST',  
    data: {"task":task,"detail":detail},
    success:function(success){
location.reload()
    },
    error:function(error){
        console.log(error);
    }

});



}

function send(data){

    var del=data;
/*

$.ajax({ 
    url: '{{url_for('/delete')}}', 
    type: 'POST',  
    data: {"load":data},
    success:function(success){
location.reload()
    },
    error:function(error){
        console.log(error);
    }

});
*/


console.log(del)



}