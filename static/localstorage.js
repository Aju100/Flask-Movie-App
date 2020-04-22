function favadder(){
    var xhr= new XMLHttpRequest();
    
    //and check if works in mobile or not
    //change this during porduction
    url="http://simplymovieapp.herokuapp.com/";
    xhr.open('POST',url);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
   /* document.addEventListener("DOMContentLoaded", function(event) { 
        });
        */
    var title=document.getElementById("title").textContent;
    var year=document.getElementById("year").innerHTML;
    var type=document.getElementById("type").textContent;
    var imdb=document.getElementById("details").textContent;
    var Poster=document.getElementById("card-img-top").src;

    xhr.send(`title=${title}&year=${year}&type=${type}&imdb=${imdb}&poster=${Poster}`);
    xhr.onreadystatechange=function(){
        document.getElementById("click").value="Added to Favourite";
        document.getElementById("click").readOnly = true;
    };
    
}

function flash(msg){

}
