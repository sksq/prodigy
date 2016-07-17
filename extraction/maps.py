import requests
import json
import datetime

key = REDACTED

find_place = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&key="+key

rests = [{"name": "empire_restaurant",'maps': "ChIJ6esDJU4UrjsRFo0qDlJZOxY", "zomato":"https://www.zomato.com/bangalore/empire-restaurant-koramangala-5th-block"}, {"name": "truffles",'maps': "ChIJdz4L2VEUrjsRvSsPGCwDl2I", "zomato":"https://www.zomato.com/bangalore/truffles-koramangala-5th-block"}, {"name": "meghana",'maps': "ChIJCa2FK04UrjsRmBiq9ethY9s", "zomato":"https://www.zomato.com/bangalore/meghana-foods-koramangala-5th-block"}, {"name": "a_hole_lotta",'maps': "ChIJ4cDixFEUrjsRKCYR0pMMDWE", "zomato":"https://www.zomato.com/bangalore/a-hole-lotta-love-cafe-koramangala-5th-block"}, {"name": "sultans_of_spice",'maps': "ChIJFdJfw1EUrjsRKfEwVSPTH34", "zomato":"https://www.zomato.com/bangalore/sultans-of-spice-koramangala-5th-block"}, {"name": "stoner",'maps': "ChIJl5L2T0QUrjsRSj6jCHXjO4E", "zomato":"https://www.zomato.com/bangalore/stoner-koramangala-5th-block"}, {"name": "buff_buffet",'maps': "ChIJqSsUw1EUrjsRtJnGsaYq6cU", "zomato":"https://www.zomato.com/bangalore/buff-buffet-buff-koramangala-5th-block"}, {"name": "kopper_kadai",'maps': "ChIJN4YMjFEUrjsRJBAyGUiABCI", "zomato":"https://www.zomato.com/bangalore/kopper-kadai-koramangala-5th-block"}, {"name": "tim_tai",'maps': "ChIJISZ5JlsUrjsRCLUBGpTL3QM", "zomato":"https://www.zomato.com/bangalore/tim-tai-koramangala-5th-block"}, {"name": "the_black_pearl",'maps': "ChIJjzdGKk4UrjsRKqnBh8iwPYQ", "zomato":"https://www.zomato.com/bangalore/the-black-pearl-koramangala-5th-block"}, {"name": "om_made_cafe",'maps': "ChIJGVzyK04UrjsRdvT82NJs8YE", "zomato":"https://www.zomato.com/bangalore/om-made-cafe-koramangala-5th-block"}, {"name": "bonsouth",'maps': "ChIJX7qSPFsUrjsRH0j0Sc6UGh0", "zomato":"https://www.zomato.com/bangalore/bonsouth-koramangala-5th-block"}, {"name": "boozy_griffin",'maps': "ChIJyZ7MK04UrjsRMdiRfgNb3fk", "zomato":"https://www.zomato.com/bangalore/the-boozy-griffin-koramangala-5th-block"}, {"name": "gilly",'maps': "ChIJDRTh6lEUrjsRJhhn5I6lIQ4", "zomato":"https://www.zomato.com/bangalore/gillys-restobar-koramangala-5th-block"}, {"name": "happy_brew",'maps': "ChIJC-Pg21EUrjsRFc-0VSf646U", "zomato":"https://www.zomato.com/bangalore/happy-brew-koramangala-5th-block"}, {"name": "berryd",'maps': "ChIJnff-xloUrjsRLBbd7iVNbms", "zomato":"https://www.zomato.com/bangalore/berryd-alive-koramangala-5th-block"}, {"name": "cupojoe",'maps': "ChIJQWpKD1AUrjsRpdRi0PJ-F8Q", "zomato":"https://www.zomato.com/bangalore/cup-o-joe-koramangala-5th-block"}, {"name": "overthetop",'maps': "ChIJ_VRecEIUrjsRIQXNNF6nk4o", "zomato":"https://www.zomato.com/bangalore/over-the-top-terrace-lounge-koramangala-5th-block"}, {"name": "anandsweets",'maps': "ChIJ77vvfkUUrjsRitclMW-11WA", "zomato":"https://www.zomato.com/bangalore/anand-sweets-and-savouries-koramangala-5th-block"}, {"name": "le_charcoal",'maps': "ChIJ37rny1EUrjsRfCXN1v_wSqc", "zomato":"https://www.zomato.com/bangalore/le-charcoal-koramangala-5th-block"}, {"name": "dhide",'maps': "ChIJ445q21oUrjsRc9JAibsz1ZU", "zomato":"https://www.zomato.com/bangalore/dhide-cafe-koramangala-5th-block"}, {"name": "hotel_junior",'maps': "ChIJ1_5JFEUUrjsR7XoksVcx5-0", "zomato":"https://www.zomato.com/bangalore/hotel-junior-kuppanna-koramangala-5th-block"}, {"name": "kritunga",'maps': "ChIJn2icKU4UrjsR04FZVwZ9E0I", "zomato":"https://www.zomato.com/bangalore/kritunga-restaurant-koramangala-5th-block"}, {"name": "tandoor_hut",'maps': "ChIJrfzApFoUrjsROUA_TzVjnNI", "zomato":"https://www.zomato.com/bangalore/tandoor-hut-koramangala-5th-block"}, {"name": "asia_kitchen",'maps': "ChIJU0zWxFoUrjsRv-QQP72ryTA", "zomato":"https://www.zomato.com/bangalore/asia-kitchen-by-mainland-china-koramangala-5th-block"}, {"name": "dice_n_dine",'maps': "ChIJMV0TilEUrjsRh0i7EQ23rjM", "zomato":"https://www.zomato.com/bangalore/dice-n-dine-koramangala-5th-block"}, {"name": "hunan",'maps': "ChIJqwJLLE4UrjsRxMtwepSM9e8", "zomato":"https://www.zomato.com/bangalore/hunan-koramangala-5th-block"}, {"name": "bamey",'maps': "ChIJC0B9SU4UrjsRlIupwLP8Lak", "zomato":"https://www.zomato.com/bameys"}, {"name": "chianti",'maps': "ChIJwTjQW0EUrjsRIRf9d3YjyK4", "zomato":"https://www.zomato.com/bangalore/chianti-koramangala-5th-block"}, {"name": "bathinda",'maps': "ChIJw33g21EUrjsR6OlF39lULgU", "zomato":"https://www.zomato.com/bangalore/bathinda-junction-koramangala-5th-block"}]

all_rest = []
for rest in rests:
	details = "https://maps.googleapis.com/maps/api/place/details/json?placeid="+rest['maps']+"&key="+key
	response = requests.get(details).json()
	tmp_rest = {}
	tmp_rest['name'] = response['result']['name']
	try:
		tmp_rest['rating'] = response['result']['rating']
	except:
		pass
	try:
		reviews_arr = response['result']['reviews']
		review_list = []
		for review in reviews_arr:
			temp_r = {}
			try:
				temp_r["rating"] = review["rating"]
			except:
				temp_r["rating"] = ""
			try:
				temp_r["text"] = review["text"]
			except:
				temp_r["text"] = ""
			try:
				temp_r["time"] = datetime.datetime.utcfromtimestamp(review["time"]).strftime("%Y-%m-%d %H:%M:%S")
			except:
				temp_r["time"] = ""
			temp_r["source"] = "maps"
			review_list.append(temp_r)
		tmp_rest['reviews'] = review_list
	except:
		pass
	all_rest.append(tmp_rest)

with open('maps.txt', 'w') as outfile:
  json.dump(all_rest, outfile)