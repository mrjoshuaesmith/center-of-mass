# center-of-mass
Finding the Center of the State of Massachusetts

## Background

The Town of Rutland, MA prides itself on being the "center" of Massachusetts. They've even identified a particular tree as being the [Central Tree](https://www.google.com/maps/place/Central+Tree,+Geographical+Center+of+Massachusetts/@42.3773906,-71.9280109,17z/data=!4m13!1m7!3m6!1s0x89e3ffb63a179009:0xd3499f926e9ce6d6!2sCentral+Tree+Rd,+Rutland,+MA!3b1!8m2!3d42.3773906!4d-71.9258222!3m4!1s0x89e3ff4c6945dae3:0xc8d8503a3a6d63c5!8m2!3d42.3780333!4d-71.9265767). There is a road called "Central Tree Road" and there are events like the "Central Tree Chowder Challenge" and the "Central Tree Music Festival." This all begs the question: how did they figure that out?

It appears this started with the USGS. Once upon a time, someone there published a list with the "geographic center" of each state. And some other sites picked up this data and ran with it (for example, [this one](https://www.netstate.com/states/geography/ma_geography.htm)). However, if you dig into that site a little, they reveal that the USGS [changed its mind](https://www.netstate.com/subdocuments/geographic_center.htm). The USGS apparently has no idea how this location was selected and has renounced it.

This raises the obvious question: Where is the Center of Massachusetts? Is it *actually* in Rutland, MA? If not, where is it?

## What is a "geographic center" anyway?

[According to the USGS](https://pubs.er.usgs.gov/publication/70039437):
> The geographic center of an area may be defined as the center of gravity of the surface, or that point on which the surface of the area would balance if it were a plane of uniform thickness.

Although it's not particularly clear in that sentence, that "or" doesn't meant there are two definitions. The center of gravity *is* the point a cardboard cutout of the state would balance. If you look at the referenced document, it says that's somewhere in the northern part of the City of Worcester. (They don't give a specific location.) Probably worth pointing out here: Rutland is not in Worcester.

That USGS pub says there are as many centers as there are definitions, which means they acknowledge the balace point isn't the only one. Another obvious one would be the center of a bounding rectangle.

Thinking about the center of gravity (which in this construct is also the center of mass, since we assume constant gravity, and the centroid of the shape, since we assume constant elevation), that's basically an average. When we look at data using an average, outliers (looking at you Provicetown, MA) tend to lead to skewed results. In other data sets (wealth distribution, for example), statisticians like to instead use the *median*. This effecively throws away the outliers and gives you the logical middle.

So that's what this project does. It finds the geographic center of Massachusetts using three definitions: center of bounding rectangle, balance point, and median.

## Data sources

To find these places, we need a source of data for the boundary of the state. I found a French company called Open Data Soft that has a great repository of this kind of data. On that site, I was able to find a [public domain border of the state of MA in JSON format](https://data.opendatasoft.com/explore/dataset/georef-united-states-of-america-state-millesime%40public/map/?disjunctive.ste_code&disjunctive.ste_name&sort=year&q=massachusetts). The exported file is included in this project.

What I learned, however, is that the Commonwealth includes some territorial waters. While that might *technically* be part of the state, people think of the state as the land part.

Looking at other data on that same site, I found [maps of all the zip codes in MA in JSON format](https://data.opendatasoft.com/explore/dataset/georef-united-states-of-america-zcta5%40public/map/?disjunctive.ste_code&disjunctive.ste_name&disjunctive.coty_code&disjunctive.coty_name&disjunctive.zcta5_code&disjunctive.zcta5_name&sort=year&q=massachusetts&location=8,42.09976,-71.76237&basemap=jawg.streets). Since the USPS doesn't deliver to bodies of water, these are a much better fit for the land mass of the state.

The next thing I learned, though, is that there are a handful of zip codes that span state boundaries!

So what we have to do is look for points that are in *both* a ZIP code and within the border of the state. The only remaining catch is that a couple big bodies of water, such as the Quabbin Reservior do no have a ZIP code. The simple fix for this is to just assume presence in a ZIP code west of -71.5º longitude.

## Computational approach

Given the nature of the above data, the most straightforward way to find the center is via sampling. Imagine putting push pins all over the map at regular intervals. The balance point is the average location of all those pins. The median is the place where there are an equal number of pins on the left/right and above/below. The bounding box is found by searching for the highest and lowest pin location.

The other advantage of using sampling, is that we can print all the pin locations, paste those into Excel, and make a scatter plot to ensure our algorithms are all working correctly.

## Coordinate system complications

All our data is in degrees of latitude and longitude. However, the size of a degree of longitude is not a constant. It gets shorter and shorter the closer you get to the poles. Usually, some sort of projection (such as UTM) would be applied to stretch things out so the coordinates are consistent. However, given that we are sampling, this is pretty simple. You just slightly change the longitudinal sampling interval, based on how many degrees a meter covers at that point.

## Results

I tested the sampling code using Excel as mentioned above, and the resulting file is included with the sources. The orange dots are my samples that pass all the tests, and the gray dots are the boundaries of the state.

<img width="1061" alt="excel plot of 2KM sample interval" src="https://user-images.githubusercontent.com/42067635/147588456-850e08a8-7452-4339-a969-70872710a267.png">

You'll notice a little hole at Lake Massapoag, and at a tigher sampling interval, there are probably a couple other lakes that get skipped east of -71.5º, but all in all, it seems unlikely those would impact our results much.

Using a 100 meter sampling interval, the program eventually yielded these results:

