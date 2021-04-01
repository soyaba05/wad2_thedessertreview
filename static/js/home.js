function getRandomSize(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

var allImages = "";

for (var i = 0; i < 25; i++) {
    var width = getRandomSize(200, 400);
    var height =  getRandomSize(200, 400);
    allImages += '<img src="https://unsplash.com/s/photos/'+width+'/'+height+'/desserts" alt="pretty kitty">';
}

$('#photos').append(allImages);