Jonathan Pichot helped me with assignment 1. He recommended Atom as a text editor and Postman to view the bus data.
So the file was stored locally.

I followed Federica's lead on the modules needed. Might have imported more than needed.

The script inputs the API key and the bus line by editing the URL as shown by Federica's example.

Jonathan explained how to use the following syntax to pick a location within the data:
data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

As recommended by Jonathan, I used a for loop to extract data for each bus at the "MonitoredVehicleJourney" level.

Used an iterator to give the bus a number label.

I needed help on this one so I didn't help anyone else.

Ben Miller answered a quick question on Assignment 1 too.

------------------------------------------------------------------------------------------------------------------

I was able to handle Assignment 2 mostly on my own, with a little help from Rich Vecsler and Francis Ko.

Copied lots of code from show_bus_locations. Imported CSV module. Added an additional sys.argv for the csv. Used if not length command to make sure the user has supplied all needed inputs.

Using Federica's instructions for writing to a CSV as well as some guidance from Rich on syntax, I had the script open the csv in write mode and write the first row with the labels Latitude, Longitude, Stop Name, and Stop Status. Rich explained using fout.writerow to write to the csv.
