



import requests
from flask import Flask
from flask import request


app = Flask(__name__)
homepage = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Carbon Emisisons</title>
    <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
    <link href="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css" rel="stylesheet">
    <script src="https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js"></script>
    <style media="screen">

      .c{
        color:#625D5D;
        text-align: center;
        font-family: cursive;
      }
      .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
      }
      form{
        text-align: center;
        font-size: 2em;
      }
      form input{
        font-size: 1em;
      }
      body { margin: 0; padding: 0; }
      #map { position: absolute; height: 93%; width: 48%; left: 0px; }
      #map1 { position: absolute; height: 93%; width: 48%; right: 0px; }
      h3{
        overflow-x: hidden;
        text-align: center;
        background-color: #0085BF;
        position: absolute;
        bottom: -1410px;
        width: 100%;
    }
    .submission{
      bottom: -1362.5px;
      position: absolute;
      width: 100%;
    }
    a {
      color: white;
    }
    </style>
  </head>
  <STYLE>A {text-decoration: none;} </STYLE>
  <h1 class="c" > Carbon Emissions </h1>
  <img src="https://images.theconversation.com/files/354902/original/file-20200826-7069-1mp7gk0.jpg?ixlib=rb-1.1.0&rect=5%2C80%2C3589%2C1794&q=45&auto=format&w=1356&h=668&fit=crop" alt="Carbon" class="center">
  <body>
    <form>
      <!---
      <label for="begarea">Place of Departure:</label><br>
      <input type="text" id="depart" name="depart"><br>
      <label for="endarea">Destination:</label><br>
      <input type="text" id="destin" name="destin"><br><br>
      --->
      <label for="vehicle">What type of vehicle do you plan to use?</label><br>
      <input type="radio" id="car" name="transportation" value="Car">
      <label for="Car">Car</label><br>
      <input type="radio" id="ctruck" name="transportation" value="Class 8 Truck">
      <label for="Class 8 Truck">Class 8 Truck</label><br>
      <input type="radio" id="dtruck" name="transportation" value="Delivery Truck">
      <label for="Delivery Truck">Delivery Truck</label><br>
      <input type="radio" id="tbus" name="transportation" value="Transit Bus">
      <label for="Transit Bus">Transit Bus</label> <br>
      <input type="radio" id="pshuttle" name="transportation" value="Paratransit Shuttle">
      <label for="Paratransit Shuttle">Paratransit Shuttle</label> <br>
      <input type="radio" id="lvan" name="transportation" value="Light Truck/Van">
      <label for="Light Truck/Van">Light Truck/Van</label> <br>
      <input type="radio" id="motor" name="transportation" value="Motorcycle">
      <label for="Motorcycle">Motorcycle</label> <br>
      <input type="radio" id="hybrid" name="transportation" value="Hybrid">
      <label for="Hybrid">Hybrid</label> <br><br>
      <label for="vehicle">What type of fuel do you plan to use?</label><br>
      <input type="radio" id="gas" name="fuel" value="Gas">
      <label for="Gas">Gas</label> <br>
      <input type="radio" id="diesel" name="fuel" value="Diesel">
      <label for="Diesel">Diesel</label> <br>
    </form>
    <!-- Load the `mapbox-gl-geocoder` plugin. -->
    <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.7.2/mapbox-gl-geocoder.min.js"></script>
    <link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.7.2/mapbox-gl-geocoder.css" type="text/css">

    <h1> Put your first position on the map &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Put your second position on the map</h1>

    <div id="map"></div>

    <script>
      // TO MAKE THE MAP APPEAR YOU MUST
      // ADD YOUR ACCESS TOKEN FROM
      // https://account.mapbox.com
      mapboxgl.accessToken = 'pk.eyJ1IjoiamtydXNlNyIsImEiOiJja3owMjgwOGwxNXluMndtc25nd3ptdTQ5In0.FUuO0vke7KYzyc7nJaz0jg';
    const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-79.4512, 43.6568],
    zoom: 13
    });

    // Add the control to the map.
    map.addControl(
    new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl
    })
    );
    map.on('load', () => {
      map.addSource('single-point', {
        type: 'geojson',
        data: {
          type: 'FeatureCollection',
          features: []
        }
      });

      map.addLayer({
        id: 'point',
        source: 'single-point',
        type: 'circle',
        paint: {
          'circle-radius': 10,
          'circle-color': '#448ee4'
        }
      });

      // Listen for the result event from the Geocoder
      // result event is triggered when a user makes a selection
      //  Add a marker at the result's coordinates
      geocoder.on('result', (event) => {
        const mapcord = map.getSource('single-point').setData(event.result.geometry);
      });
    });
    </script>
    <!---
     second map
    --->
  <!-- Load the `mapbox-gl-geocoder` plugin. -->
  <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.7.2/mapbox-gl-geocoder.min.js"></script>
  <link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v4.7.2/mapbox-gl-geocoder.css" type="text/css">

  <div id="map1"></div>

  <script>
  	// TO MAKE THE MAP APPEAR YOU MUST
  	// ADD YOUR ACCESS TOKEN FROM
  	// https://account.mapbox.com
  	mapboxgl.accessToken = 'pk.eyJ1IjoiamtydXNlNyIsImEiOiJja3owMjgwOGwxNXluMndtc25nd3ptdTQ5In0.FUuO0vke7KYzyc7nJaz0jg';
  const map1 = new mapboxgl.Map({
  container: 'map1',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-79.4512, 43.6568],
  zoom: 13
  });

  // Add the control to the map.
  map1.addControl(
  new MapboxGeocoder({
  accessToken: mapboxgl.accessToken,
  mapboxgl: mapboxgl
  })
  );
  map.on('load', () => {
    map.addSource('single-point', {
      type: 'geojson',
      data: {
        type: 'FeatureCollection',
        features: []
      }
    });

    map.addLayer({
      id: 'point',
      source: 'single-point',
      type: 'circle',
      paint: {
        'circle-radius': 10,
        'circle-color': '#448ee4'
      }
    });

    // Listen for the result event from the Geocoder
    // result event is triggered when a user makes a selection
    //  Add a marker at the result's coordinates
    geocoder.on('result', (event) => {
      const mapcord2 = map.getSource('single-point').setData(event.result.geometry);
    });
  });
  </script>
  <form class = "submission" action="Homepage.html" method="get">
    <input type="submit" value="Click to see your carbon emissions"> <br><br>
  </form>
  <h3> <a href="aboutus.html"> About The Creators <br> Ruchi, Emme, Julianne </a> </h3>
</body>
</html>"""
presentpage = """<!DOCTYPE html>
<head>
<script src='https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js'></script>
<link href='https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css' rel='stylesheet' />
</head>

<body>
  <div id='map' style='width: 400px; height: 300px;'></div>
<script>
// TO MAKE THE MAP APPEAR YOU MUST
// ADD YOUR ACCESS TOKEN FROM
// https://account.mapbox.com
mapboxgl.accessToken = 'pk.eyJ1IjoiamtydXNlNyIsImEiOiJja3owMjgwOGwxNXluMndtc25nd3ptdTQ5In0.FUuO0vke7KYzyc7nJaz0jg';
const map = new mapboxgl.Map({
container: 'map', // container ID
style: 'mapbox://styles/mapbox/streets-v11', // style URL
center: [-74.5, 40], // starting position [lng, lat]
zoom: 9 // starting zoom
});
</script>
</body>"""
testpage = """<!DOCTYPE html>
<html>
    <head>
        <title>Present data!</title>
    </head>
    <body>
        You entered this number:  {}
        <br />
        You entered this string:  {}
    </body>
</html>
"""
formpage = """<!DOCTYPE html>
<html>
    <head>
        <title>Basic form</title>
    </head>
    <body>
        <form action="" method="post">
            Enter a number:  <input type="text" name="anumber" />
            <br />
            Enter a string:  <input type="text" name="astring" />
            <br />
            <input type="submit" value="submit" />
        </form>
    </body>
</html>
"""

@app.route("/", methods = ['GET', 'POST'])

def form():
   if request.method == 'POST':
       depart = request.form['depart']
       destin = request.form['destin']
       transpo = request.form['transporation']
       fuel = request.form['fuel']

       return presentpage.format()
   else:
        return homepage
@app.route("/api/coordToDist", methods = ["POST"])
def coordToDist():
    #mapcoors = request.form['result']
    #print(mapcoors)
    #return ('distance': distance)
    pass

app.run()


#test = request.form[results]
#print(test)

driving_endpoint = "https://api.mapbox.com/optimized-trips/v1/mapbox/driving/"
walking_endpoint = "https://api.mapbox.com/optimized-trips/v1/mapbox/walking/"
cycling_endpoint = "https://api.mapbox.com/optimized-trips/v1/mapbox/cycling/"
def getDist(api):

    coords = "-73.97836904822721%2C40.76619736766432%3B-73.87327233316093%2C40.769997172823025"
    data = {
        #"alternatives": 'false',
        "geometries": "geojson",
        "language": "en",
        "overview": "simplified",
        "steps": "false",
        "access_token": "pk.eyJ1IjoiamtydXNlNyIsImEiOiJja3owMjgwOGwxNXluMndtc25nd3ptdTQ5In0.FUuO0vke7KYzyc7nJaz0jg",
    }

    response = requests.get(api + coords, params=data)
    data = response.json()
    distance = data['trips'][0]['legs'][0]['distance'] / 1609
    return distance
def getTime(api):
    coords = "-73.97836904822721%2C40.76619736766432%3B-73.87327233316093%2C40.769997172823025"
    data = {
        # "alternatives": 'false',
        "geometries": "geojson",
        "language": "en",
        "overview": "simplified",
        "steps": "false",
        "access_token": "pk.eyJ1IjoiamtydXNlNyIsImEiOiJja3owMjgwOGwxNXluMndtc25nd3ptdTQ5In0.FUuO0vke7KYzyc7nJaz0jg",
    }

    response = requests.get(api + coords, params=data)
    data = response.json()
    time = data_drive['trips'][0]['legs'][0]['duration']/60
    return time


data_drive = getDist(driving_endpoint)
data_bike = getDist(cycling_endpoint)
data_walk = getDist(walking_endpoint)

time_drive = getTime(driving_endpoint)
time_bike = getTime(cycling_endpoint)
time_walk = getTime(Walking_endpoint)

#test values below
fuel_type = 'Gas'
car_type = 'Car'
def calc_pounds(car_type,fuel_type):
    pounds = {}
    co2_gas = 18.74
    co2_diesel = 22.46

    if(fuel_type == 'Gas'):
        #car
        mpg = 24.2
        car_pounds = (distance_mi/mpg)*co2_gas
        pounds['car'] = car_pounds
        if(car_type == "Car"):
            pounds['chosen'] = car_pounds
        #transit bus
        mpg = 3.3
        bus_pounds = (distance_mi / mpg) * co2_gas
        pounds['bus'] = bus_pounds/10
        if (car_type == "Transit Bus"):
            pounds['chosen'] = bus_pounds/10
        #paratransit shuttle
        mpg = 7.1
        shuttle_pounds = (distance_mi / mpg) * co2_gas
        pounds['shuttle'] = shuttle_pounds/5
        if (car_type == "Paratransit Shuttle"):
            pounds['chosen'] = shuttle_pounds/5
        #motorcycle
        mpg = 44.0
        motor_pounds = (distance_mi / mpg) * co2_gas
        pounds['motorcycle'] = motor_pounds
        #hybrid
        mpg = 34.8
        hybrid_pounds = (distance_mi / mpg) * co2_gas
        pounds['hybrid'] = hybrid_pounds
        if (car_type == "Motorcycle"):
            pounds['chosen'] = motor_pounds
        if (car_type == 'Class 8 Truck'):
            mpg = 5.3
            truck_pounds = (distance_mi / mpg) * co2_gas
            pounds['chosen'] = truck_pounds
        if (car_type == 'Delivery Truck'):
            mpg = 6.5
            truck_pounds = (distance_mi / mpg) * co2_gas
            pounds['chosen'] = truck_pounds
        if (car_type == 'Light Van/Truck'):
            mpg = 17.5
            truck_pounds = (distance_mi / mpg) * co2_gas
            pounds['chosen'] = truck_pounds

    else:
        #car
        mpg = 27.3
        car_pounds = (distance_mi/mpg)*co2_diesel
        pounds['car'] = car_pounds
        #transit bus
        mpg = 3.7
        bus_pounds = (distance_mi / mpg) * co2_diesel
        pounds['bus'] = bus_pounds
        #paratransit shuttle
        mpg = 8.0
        shuttle_pounds = (distance_mi / mpg) * co2_diesel
        pounds['shuttle'] = shuttle_pounds
        #motorcycle
        mpg = 49.7
        motor_pounds = (distance_mi / mpg) * co2_diesel
        pounds['motor'] = motor_pounds
        if (car_type == 'Hybrid'):
            print('Data not found. Please use type gas.')
        if (car_type == 'Class 8 Truck'):
            mpg = 6.0
            truck_pounds = (distance_mi / mpg) * co2_diesel
            pounds['chosen'] = truck_pounds
        if (car_type == 'Delivery Truck'):
            mpg = 7.4
            truck_pounds = (distance_mi / mpg) * co2_diesel
            pounds['chosen'] = truck_pounds
        if (car_type == 'Light Van/Truck'):
            mpg = 19.8
            truck_pounds = (distance_mi / mpg) * co2_diesel
            pounds['chosen'] = truck_pounds
    #check if other car types where chosen
    if pounds['chosen'] == 0:
        print('Car_type invalid. try again.')
    return pounds

pounds = calc_pounds(car_type, fuel_type)
#show output
print('You will get there in ' + str(round(data_drive, 2)) + " miles and " +  str(round(time_drive, 2)) + " minutes, but you will emit " + str(round(pounds['chosen'], 2)) + "pounds of carbon.")
#alternate options

print('Alternate Options!')
print('You could bike there for ' + str(round(data_bike, 2)) + " miles in " + str(round(time_bike, 2)) + ' minutes and release 0 emissions')
print('You could walk there for ' + str(round(data_walk, 2)) + " miles in " + str(round(time_walk, 2)) + ' minutes and release 0 emissions')
#alternate motor vehicles that produce less
for key in pounds:
    if pounds[key]< pounds['chosen']:
        print("You can also travel by " + key + " and only emit " + str(round(pounds[key],2)) + " pounds of carbon")
        if key == 'bus' or key == 'shuttle':
            print('This emission accounts for the average  number of people on transit.')



