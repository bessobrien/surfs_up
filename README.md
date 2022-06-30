# Surf's Up Analysis

## Overview

The purpose of this analysis was to utilize the SQLite database and look at the weather data to ensure that the investment for a surf shop / ice cream shop combo is well-spent. This analysis specifically, looks at June and December temperatures to ensure that the investment in the business is viable year round.

## Results

Firstly, we created an engine to generate queries from the SQLite database. From there, we wrote a query, placed in a list, and then created a dataframe for each. We utilized the .describe() function to generate summary statistics for both June and December. 

Our results:

JUNE Temperatures

![june_temps](https://github.com/bessobrien/surfs_up/blob/main/Resources/june_temps.png)

and 

DECEMBER Temperatures

![dec_temps](https://github.com/bessobrien/surfs_up/blob/main/Resources/December_temps.png)

Our key differences between the two:
* Temperatures are higher in June by approximately 3-4 degrees (mean), and 2 degrees (max).
* June also has more days counted of rain.
* The minimum temperature in December is 8 degrees lower than in June.

## Summary

After looking at both June and December, we can see that the mean is within 3-4 degrees comparing June and December. The standard deviation is similiar, which means that temperatures stay fairly consistent year-round.

### Other Options

We could run additional queries to do a more in-depth analysis. Two additional options:

1. A query to get precipitation for the months of June and December to see weather patterns:

session.query(Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
session.query(Measurement.prcp).filter(extract('month', Measurement.date)==12).all()

These could be turned into a list and dataframe, similiar to our attached analysis.

2. A query to get temperatures and preciption into the same query:
session.query(Measurement.prcip, Measurement.tobs).filter(extract('month', Measurement.date)==6).all()

This could be turned into a list and dataframe, and use the date as the index.

