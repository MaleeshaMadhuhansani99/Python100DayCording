travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,visited,cities) :
  travel_new={}
  travel_new["country"]=country
  travel_new["visits"]=visited
  travel_new["cities"]=cities
  
  travel_log.append(travel_new) 
  
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



