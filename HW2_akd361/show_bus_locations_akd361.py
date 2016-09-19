from __future__ import print_function
import json
import urllib2
import os
import urllib as ul
import sys

mta_key = sys.argv[1]
bus_id = sys.argv[2]

bus_data = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_id

response = ul.urlopen(bus_data)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicles = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
vehicle_count = len(vehicles)

print ('Bus Line : ' + bus_id)

print ('Number of Active Buses : ' + str(vehicle_count))

bus_number = 0

for vehicle in vehicles:
    busLongitude = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    busLatitude = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    print ("Bus " + str(bus_number) + " is at latitude " + str(busLatitude) + " and longitude " + str(busLongitude))
    bus_number += 1
