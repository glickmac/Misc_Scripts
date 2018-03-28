import json
import urllib.request

def exploringEarthquakes(city, radius, startdate, enddate, mode):
    #encode city
    city = city.replace(' ', '+')
    
    #helper to get json data from API
    def getJSONDataFromAPI(url):
        req  = urllib.request.Request(url)
        resp = urllib.request.urlopen(req).read()
        return json.loads(resp.decode('utf-8'))
    
    #returns the average magnitude of quakes
    def getAverageMagnitude(quakes):
        count = len(quakes)
        
        if count == 0:
            return 0
        else:
            mag_sum = 0
            for quake in quakes:
                mag_sum += quake['properties']['mag']
            
            return mag_sum / count
    
    
    #get lat and long from google
    geo_j = getJSONDataFromAPI("https://maps.googleapis.com/maps/api/geocode/json?address="+city+"&key=AIzaSyAtgxw7fkse0ldJmfS-BfkIPrCOvkzfS6I")
    print(geo_j['status'])
    if geo_j['status'] != "OK":
        return -1
    location = geo_j['results'][0]['geometry']['location']
    
    #get eq data from USGS
    eq_api = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+startdate+"&endtime="+enddate+"&minmagnitude=4&maxradiuskm="+str(radius)+"&latitude="+str(location['lat'])+"&longitude="+str(location['lng'])
    eq_jc = getJSONDataFromAPI(eq_api)
    
    #common data
    eq_count = eq_jc['metadata']['count']
    
    if mode == "count":
        return eq_count
    
    elif mode == "average":
        return getAverageMagnitude(eq_jc['features'])

        
    elif mode == "compare":
        #get world earthquakes
        eq_api_w = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime="+startdate+"&endtime="+enddate+"&minmagnitude=4"
        eq_jw = getJSONDataFromAPI(eq_api_w)
        
        eq_avg_w = getAverageMagnitude(eq_jw['features'])
        eq_avg_c = getAverageMagnitude(eq_jc['features'])
        
        return eq_avg_c - eq_avg_w
