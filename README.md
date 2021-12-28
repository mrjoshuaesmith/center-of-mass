# center-of-mass
Finding the Center of the State of Massachusetts

## Background

The Town of Rutland, MA prides itself on being the "center" of Massachusetts. They've even identified a particular tree as being the [Central Tree](https://www.google.com/maps/place/Central+Tree,+Geographical+Center+of+Massachusetts/@42.3773906,-71.9280109,17z/data=!4m13!1m7!3m6!1s0x89e3ffb63a179009:0xd3499f926e9ce6d6!2sCentral+Tree+Rd,+Rutland,+MA!3b1!8m2!3d42.3773906!4d-71.9258222!3m4!1s0x89e3ff4c6945dae3:0xc8d8503a3a6d63c5!8m2!3d42.3780333!4d-71.9265767). There is a road called "Central Tree Road" and there are events like the "Central Tree Chowder Challenge" and the "Central Tree Music Festival." This all begs the question: how did they figure that out?

It appears this started with the USGS. Once upon a time, someone there published a list of the "geographic center" of each state. And some other sites picked up this data and ran with it (for example, [this one](https://www.netstate.com/states/geography/ma_geography.htm)). However, if you dig into that site a little, they reveal that the USGS [changed its mind](https://www.netstate.com/subdocuments/geographic_center.htm). The USGS apparently has no idea how this location was selected and has renounced it.

This raises the obvious question: Where is the Center of Massachusetts? Is it *actually* in Rutland, MA? If not, where is it?

## What is a "geographic center" anyway?

[According to the USGS](https://pubs.er.usgs.gov/publication/70039437):
> The geographic center of an area may be defined as the center of gravity of the surface, or that point on which the surface of the area would balance if it were a plane of uniform thickness.

Although it's not particularly clear in that sentence, that "or" doesn't meant there are two definitions. The center of gravity *is* the point a cardboard cutout of the state would balance. If you look at the referenced document, it says that's somewhere in the northern part of the City of Worcester. (They don't give a specific location.) Probably worth pointing out here: Rutland is not in Worcester.

That USGS pub says there are as many centers as there are definitions, which means they acknowledge the balace point isn't the only one. Another obvious one would be the center of a bounding rectangle.

Thinking about the center of gravity (which in this construct is also the center of mass, since we assume constant gravity, and the centroid of the shape, since we assume constant elevation), that's basically an average. When we look at data using an average, outliers (looking at you Provicetown, MA) tend to lead to skewed results. In other data sets (wealth distribution, for example), statisticians like to instead use the *median*. This effecively throws away the outliers and gives you the logical middle.

