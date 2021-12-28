#!/opt/local/bin/python3

import math
import json
import sys

def meterToLat():
    return 1/111139.0

def meterToLon(lat):
    return 1/ (40075000.0 * abs(math.cos(lat*math.pi/180)) / 360.0)

with open("georef-united-states-of-america-state-millesime.geojson") as f:
    state = json.load(f)
with open("georef-united-states-of-america-zcta5.geojson") as f:
    zips = json.load(f)

stateBorder = state["features"][0]["geometry"]["coordinates"][0]

minLat = minLon = 360
maxLat = maxLon = -360
for c in stateBorder:
    lon = c[0]
    lat = c[1]
#    print("%f\t%f" % (lon , lat))
    if lat < minLat:
        minLat = lat
    if lon < minLon:
        minLon = lon
    if lat > maxLat:
        maxLat = lat
    if lon > maxLon:
        maxLon = lon

def testInPolygon(x, y, polygon):
    count = 0
    for i in range(0,len(polygon)-1):
        segX0 = polygon[i][0]
        segX1 = polygon[i+1][0]
        segY0 = polygon[i][1]
        segY1 = polygon[i+1][1]
        if x < min(segX0,segX1) or x >= max(segX0,segX1):
            continue
        if y >= max(segY0,segY1):
            continue
        if y < min(segY0,segY1):
            count += 1
            continue
        if segX1 == segX0:
            count += 1
            continue
        yOnSeg = segY0 + (segY1 - segY0) * (x - segX0) / (segX1 - segX0)
        if y < yOnSeg:
            count += 1
            continue
    return (count % 2) == 1

def test(lon, lat):
    if not testInPolygon(lon, lat, stateBorder): # test in state or territorial water
        return False
    if lon < -71.5: # test if inland
        return True
    for town in zips["features"]: # test if it's in a land mass
        if town["geometry"]["type"] == "Polygon":
            for poly in town["geometry"]["coordinates"]:
                if testInPolygon(lon, lat, poly):
                    return True
        else:
            for polys in town["geometry"]["coordinates"]:
                for poly in polys:
                    if testInPolygon(lon, lat, poly):
                        return True
    return False

samples = []

meters = 500
lat = minLat
latStep = meters*meterToLat()
while lat <= maxLat:
    lon = minLon
    lonStep = meters*meterToLon(lat)
    while lon <= maxLon:
        if test(lon, lat):
            #print("%f\t%f" % (lon, lat))
            samples.append([lon,lat])
        lon += lonStep
    lat += latStep
    print("%f%%" % (100*(lat-minLat)/(maxLat-minLat)))

# Find the actual min/max lat/lon, excluding territorial waters
minLat = minLon = 360
maxLat = maxLon = -360
for s in samples:
    if s[0] < minLon:
        minLon = s[0]
    if s[1] < minLat:
        minLat = s[1]
    if s[0] > maxLon:
        maxLon = s[0]
    if s[1] > maxLat:
        maxLat = s[1]

print("Center of Bounding Box: %f, %f" % ((minLat+maxLat)/2, (minLon+maxLon)/2))

sumLon = 0
sumLat = 0
for s in samples:
    sumLon += s[0]
    sumLat += s[1]

print("Balance Point: %f, %f" % (sumLat/len(samples), sumLon/len(samples)))

allLon = []
allLat = []
for s in samples:
    allLon.append(s[0])
    allLat.append(s[1])
allLon.sort()
allLat.sort()
mid0 = math.floor(len(allLon)/2)
mid1 = math.ceil(len(allLon)/2)

print("Median: %f, %f" % ((allLat[mid0]+allLat[mid1])/2, (allLon[mid0]+allLon[mid1])/2))

