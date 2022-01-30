import requests

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
    time = data['trips'][0]['legs'][0]['duration']
    return time/60


distance_mi = getDist(driving_endpoint)
data_bike = getDist(cycling_endpoint)
data_walk = getDist(walking_endpoint)

time_drive = getTime(driving_endpoint)
time_bike = getTime(cycling_endpoint)
time_walk = getTime(walking_endpoint)

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
print('You will get there in ' + str(round(distance_mi, 2)) + " miles and " +  str(round(time_drive, 2)) + " minutes, but you will emit " + str(round(pounds['chosen'], 2)) + "pounds of carbon.")
#alternate options

print('Alternate Options!')
print('You could bike there for ' + str(round(data_bike, 2)) + " miles in " + str(round(time_bike, 2)) + ' minutes and release 0 emissions')
print('You could walk there for ' + str(round(data_walk, 2)) + " miles in " + str(round(time_walk, 2)) + ' minutes and release 0 emissions')
#alternate motor vehicles that produce less
final = ""
for key in pounds:
    if pounds[key]< pounds['chosen']:
        final += ("You can also travel by " + key + " and only emit " + str(round(pounds[key],2)) + " pounds of carbon")
        if key == 'bus' or key == 'shuttle':
            final += (' This emission accounts for the average  number of people on transit.')
print(final)



