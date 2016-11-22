I did this assignment on my own with one set of code borrowed from Avikal Somvanshi: how to select certain months from the year-round dataset and create a new reduced dataframe.

ANALYSIS:

Citi Bike ridership goes down in the winter months and up in the summer months.

When isolated by half-year, both seasons showed consistency in 2013 and 2014 and rises in ridership in 2015-2016.
December 2015 and March 2016 were the two months that deviated the most from the same months in previous years.

Spatial lag seemed to be greater in the summer, with noticeably more in lower Manhattan and the west side of midtown.

All times of year showed a correlation between monthly rider volume and spatial lag.

The spatial autocorrelation shown in hot and cold spots gave slightly more hotspots to the winter months and slightly more
coldspots to the summer months, meaning that for some reason autocorrelation is greater in the winter. Maybe the average length
of trip could be the reason for this? If people take shorter trips in the winter because it's cold and they're only riding out
of necessity, a given census tract's ridership might be more dependent on the ridership in tracts around it. In summer, people
may take longer trips because the weather is nice and it's more of a pleasure activity than pure transportation. This would be
a good next step to investigate.
