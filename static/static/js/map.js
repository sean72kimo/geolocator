var marker;
var map;
var myLatlng = new google.maps.LatLng(lat, lng);
//console.log('latlngset: ',latlngset);
function initialize() {
    console.log('---- map loading -----');
    
    var mapOptions = {
        center: myLatlng,
        zoom:15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    marker = new google.maps.Marker({
        map: map,
        draggable:true,
        animation: google.maps.Animation.DROP,
        position: myLatlng,        
        title: '{{ location }}'        
    });
    google.maps.event.addListener(marker, 'click', toggleBounce);
}

function toggleBounce() {

  if (marker.getAnimation() !== null) {
    marker.setAnimation(null);
  } else {
    marker.setAnimation(google.maps.Animation.BOUNCE);
  }
}

google.maps.event.addDomListener(window, 'load', initialize); 

//marker.setMap(map);

var content = '<h4>' + '{{ location }}' + '</h4>' + '<p> is located at ' + lat + ', ' + lng + '</p>';
//var infowindow = new google.maps.InfoWindow();
//infowindow.setContent(content);
//google.maps.event.addListener(
//marker,
//'click', infowindwo.open(map,marker)
//);}

