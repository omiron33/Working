$(document).ready(function () {
    var cities = ["Dallas","Houston","Des Moines","Los Angeles","Lansing","New York","Seattle","Salt Lake City","Chicago","Louisville","Memphis","Baltimore","Bucaramenga"];
    
    $('form').on( "click", "input", function() {
        $(this).remove();
        for (var i = 1; i <= 12; i++) {
            $('#directory').append('<div id="'+cities[i]+'" class="box"><p>'+cities[i]+'</p></div>');
            //Below line would be in above append if you could call API without 504 errors
            //<img id="'+i+'" src="https://pokeapi.co/media/img/'+i+'" alt="'+i+'">
        }
        return false;
    });

    $('#directory').on( "click", "div", function() {
        if ($('#stats').length > 0) {
            $('#stats').remove();
        }
        $(this).before('<div id="stats"></div>');
        var poke = $(this).attr("id");
        //Using openweatherrmap as proof of concept and functionality as it works

        $.get('https://api.openweathermap.org/data/2.5/weather?q='+poke+'&&appid=d3ec4ed15baab3319ddd51726a3dc9d5', function (res) {
            $('#stats').append('<h1>'+poke+'</h1><p>'+res.main.temp+'</p><h3>Pressure and Humidity</h3><p>'+res.main.pressure+'</p><p>'+res.main.humidity+'</p><h2>High Temp Today</h2><p>'+res.main.temp_max+'</p><h2>Low Temp Today</h2><p>'+res.main.temp_min+'</p>');
            
        }, 'json');
        return false;
        
        //Below code works. Pokeapi 504 error based on requests from everyone
        /*$.get('https://pokeapi.co/api/v2/pokemon/'+poke, function(res){
           $('#stats').append('<img src="'+res.sprites.front_default+'" alt="img">');
        }, 'json');*/

        
    });






});