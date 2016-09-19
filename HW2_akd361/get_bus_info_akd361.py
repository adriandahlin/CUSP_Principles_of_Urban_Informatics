from __future__ import print_function
import sys
import json
import numpy as np
import urllib2
import pandas as pd
import urllib as ul
import csv

mta_key = sys.argv[1]
bus_id = sys.argv[2]
csv_output = sys.argv[3]

bus_data = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_id

response = ul.urlopen(bus_data)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicles = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python aPythonScriptThatWritesToCSV.py mycvs.csv")
    sys.exit()

fout = csv.writer(open(sys.argv[3], "wb+"))

fout.writerow(['Latitude','Longitude','Stop Name','Stop Status'])

for vehicle in vehicles:
    busLongitude = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    busLatitude = vehicle["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    stopName = vehicle["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"]
    stopStatus = vehicle["MonitoredVehicleJourney"]["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"]
    fout.writerow([busLatitude,busLongitude,stopName,stopStatus])
