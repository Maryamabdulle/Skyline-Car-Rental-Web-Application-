'use strict'

////Google Map Functionality////

// let lat= parsefloat(document.getElementById("lat").getAttribute('value'));
// let lng= parsefloat(document.getElementById("long").getAttribute('value'));


// console.log(lat)
// console.log(lng)

//def (user the function)
//tell dom

removeBothLoc();

function saveLocalLoc(key, value){
  localStorage.setItem(key,value);
  return false;
}

function loadLocalLoc(key){
  const val = localStorage.getItem(key);
  // console.log(val);
  return val;
}

function removeBothLoc(){
  localStorage.removeItem('pick');
  localStorage.removeItem('drop');
}

function formPickupField(){
  $('#locationCheckbox').prop('checked', false);
  const locationStr = $('#pickupLoc').val();
  saveLocalLoc('pick', locationStr);

  // TODO when ever thing is done refresh map
  initMap();
}

function formDropoffField(){
  // $('#locationCheckbox').prop('checked', false);
  const locationStr = $('#dropoffLoc').val();
  saveLocalLoc('drop', locationStr);

  // TODO when ever thing is done refresh map
  initMap();
}

function setMarker(latlng, map, address){
  // {lat:-33.890542, lng:151.274856,}
  var redMarker;
  redMarker = new google.maps.Marker({
    position: latlng,
    title: address,
    map
  });

  google.maps.event.addListener(redMarker, 'click', function(){
    window.open(`https://maps.google.com?q=${redMarker.position}`);
  });

  var greenMarker;
  greenMarker = new google.maps.Marker({
    position: latlng,
    icon:{
      url: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
      scaledSize: new google.maps.Size(45, 45),
      origin: new google.maps.Point(0, 0),
      anchor: new google.maps.Point(5,5)
    },
    title: address,
    map
  });

  const infoWindow = new google.maps.InfoWindow({
    content: 'click on marker to view in google map'
  });

  google.maps.event.addListener(greenMarker, 'click', function(){
    window.open(`https://www.google.com/maps/search/?api=1&query=${address}`);
  });

  google.maps.event.addListener(greenMarker, 'mouseover', function(){
    infoWindow.open(map, this);
  });

  google.maps.event.addListener(greenMarker, 'mouseout', function(){
    infoWindow.close();
  });
  // marker.setMarker(map);
}

function get_latlng(address, map, callback){
  const geocoder = new google.maps.Geocoder();

    let geocodePromise;
    geocoder.geocode({ address: address }, (results, status) => {
      if (status == 'OK'){
        // console.log(results);
        const latLng = results[0].geometry.location;
        if (callback){
          callback(latLng, map, address);
        }
      }else{
        // console.log('geocode unsuccessful '+status);
      }
    });
}

function initMap() {
    const map = new google.maps.Map(document.querySelector('#map'), {
        center: {lat:33.448376, lng:-112.074036}, 
          zoom: 9,
    });

    let locationPickup = loadLocalLoc('pick');
    let locationDropOff = loadLocalLoc('drop');
    // get_latlng('2640 East Indian School Road, NA, Phoenix, AZ, 85016, US', map);
    get_latlng(locationPickup, map, setMarker);

    get_latlng(locationDropOff, map, setMarker);
};

window.initMap=initMap;













//     const car= {lat: lat, lng: lng};
//     //the map, centered at page
//     const map= new google.maps.map(document.getElementById("map"),{
//         zoom: 15,
//         center: car,
//     });
//     //the marker, positioned 
//     const marker= new google.maps.marker{{
//         position: car,
//         map: map,
//     });
// }

// window.initmapp=initmapp;