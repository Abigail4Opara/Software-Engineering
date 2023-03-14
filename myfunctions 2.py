from math import radians, cos, sin, asin, sqrt

def haversine(Lon1, Lat1, Lon2, Lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    Lon1, Lat1, Lon2, Lat2 = map(radians, [Lon1, Lat1, Lon2, Lat2])

    # haversine formula
    dLon = Lon2 - Lon1
    dLat = Lat2 - Lat1
    a = sin(dLat/2)**2 + cos(Lat1) * cos(Lat2) * sin(dLon/2)**2
    c = 2 * asin(sqrt (a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r
