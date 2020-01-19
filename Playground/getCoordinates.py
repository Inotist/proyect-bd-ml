import googlemaps
import API_KEY

gmaps = googlemaps.Client(API_KEY.api_key)

with open('Datasets/datasets_yelp_food_2020_01_18_crawl.csv', 'r', encoding='utf-8') as read:
    dataset = read.readlines()
    
with open('Datasets/yelp_food_with_coordinates2.csv', 'w') as write:
    write.write(dataset[0][:-1] + "|Latitude|Longitude\n")
    for row in dataset[1:]:
        geocode_result = gmaps.geocode(row.split("|")[7] + " Madrid")
        if geocode_result and len(geocode_result) > 0:
            lat = geocode_result[0]['geometry']['location']['lat']
            lon = geocode_result[0]['geometry']['location']['lng']
            write.write(row[:-1] + "|" + str(lat) + "|" + str(lon) + "\n")