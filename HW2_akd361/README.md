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

Francis pointed me toward the right data names in the MTA data, which I could also figure out when looking through the data on Postman.

Using Federica's instructions for writing to a CSV as well as some guidance from Rich on syntax, I had the script open the csv in write mode and write the first row with the labels Latitude, Longitude, Stop Name, and Stop Status. Rich explained using fout.writerow to write to the csv. Then added fout.writerow to the for loop instead of the print function from assignment 1. This simply needed the variable names.

I then helped Alexey Kalinin with the step of writing to a csv using fout commands. His code looked good, but he was getting an error with his sys.argv[3] that we couldn't figure out.

-----------------------------------------------------------------------------------------------------------------------------

Laura Gladson helped me and Alexey with Assignment 3. She explained how to get the correct extension for the dataset (/avwq-z233/1414245694/avwq-z233) using ls in compute.

She showed me how to use <dataframe_name>.head() to show just the first few rows. She also helped by showing me and Alexey what the plt commands are. I figured out the legend command and passed that along to Laura and Alexey.

The dataset I chose (Current Medallions) was a little unfortunate. The only two numerical columns were not related (model year and medallion agent number). Would have been more interesting to pick two variables that were correlated. If I had more time I'd pick different data, but it's too close to the deadline to go back now.
