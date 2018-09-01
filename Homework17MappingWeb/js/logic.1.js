var newYorkCoords = [40.73, -74.0059];
var mapZoomLevel = 12;

function createMap(bikeStations) {
// Create the tile layer that will be the background of our map  
let lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  })

let baseMaps = {
  "Light Map": lightmap
}
let overlayMaps = {
  "Bike Stations": bikeStations
};
let map = L.map("map-id", {
  center: newYorkCoords,
  zoom: mapZoomLevel,
  layers: [lightmap, bikeStations]
})
L.control.layers(baseMaps, overlayMaps, {
  collapse: false
}).addTo(map);
} 

function createMarkers(response) {
 // console.log(response)
  // Pull the "stations" property off of response.data
let stations = response.data.stations
console.log(stations)
  // Initialize an array to hold bike markers
let bikeMarkers = []
  // Loop through the stations array
    // For each station, create a marker and bind a popup with the station's name
    for(let index=0; index < stations.length; index++) {
 // Add the marker to the bikeMarkers array
      let station = stations[index];
      let bikeMarker = L.marker([station.lat, station.lon])
      .bindPopup("<h3>" + station.name + "</h3><h3>Capacity:" + station.capacity + "</h3>" );
      bikeMarkers.push(bikeMarker);
    }
   

createMap(L.layerGroup(bikeMarkers));
}


// Store our API endpoint inside queryUrl
var queryUrl = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"


// Perform a GET request to the query URL
d3.json(queryUrl, createMarkers);



