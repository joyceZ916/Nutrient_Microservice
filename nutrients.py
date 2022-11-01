import time
import zmq
import requests

"""
A food essential nutrients scraper
param food_name: String
return food's essential nutrients: json
"""

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5577")

# receive the food name
while True:
    food_name = socket.recv().decode("utf-8")

    time.sleep(1)

    # retrieve essential nutrients of the food
    url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=" + food_name + "&dataType=Foundation&pageSize=1&api_key=IxZhUJn89pmc1V4bMvAJ9g3U0ehx5gZGf0JuPzxC"
    response = requests.get(url)
    foods = response.json()['foods']
    if len(foods) == 0:
        socket.send_string("null")
    else:
        foodNutrients = foods[0]["foodNutrients"]
        responseDictionary = {}
        for foodNutrient in foodNutrients:
            nutrientName = foodNutrient["nutrientName"]
            if nutrientName == "Protein":
                responseDictionary["protein"] = foodNutrient["value"]
            elif nutrientName == "Calcium, Ca":
                responseDictionary["calcium"] = foodNutrient["value"]
            elif nutrientName == "Iron, Fe":
                responseDictionary["iron"] = foodNutrient["value"]

        # return the food's essential nutrients
        socket.send_string('{"protein": ' + str(responseDictionary['protein']) + ', "calcium": ' + str(responseDictionary[
            'calcium']) + ', "iron": ' + str(responseDictionary['iron']) + '}')
