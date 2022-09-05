from webbrowser import get
from django.shortcuts import render
import requests
import json
get_json = requests.get("https://www.fruityvice.com/api/fruit/all")


def get_fruits_name():
    fruits_list = get_json.json()
    fruits = []
    for i in range(len(fruits_list)):
        fruits.append(fruits_list[i]['name'])
    return fruits

# Create your views here.


def fruit_info(request):
    fruit = request.POST['select']
    fruits = get_fruits_name()
    selected_fruit_info = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit}")
    fruit_info_json = selected_fruit_info.json()
    
    #Fruit information

    carbohydrates = fruit_info_json['nutritions']['carbohydrates']
    protein = fruit_info_json['nutritions']['protein']
    fat = fruit_info_json['nutritions']['fat']
    calories = fruit_info_json['nutritions']['calories']
    sugar = fruit_info_json['nutritions']['sugar']


    return render(request, 'fruit_info.html', context={
        'fruit': fruit, 'fruits':fruits, 'carbohydrates':carbohydrates,
        'protein':protein, 'fat':fat, 'calories':calories, 'sugar':sugar
        })

def home(request):
    if get_json.status_code != 200:
        return render(request, 'error.html')
    else:
        fruits = get_fruits_name()   
        return render(
            request,
            "home.html",
            context={
                'fruits':fruits
                }
            )