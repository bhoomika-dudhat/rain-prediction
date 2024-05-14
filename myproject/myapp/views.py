import os
import pickle
import numpy as np
from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'index.html')

def predictor_page(request):
    return render(request,'predictor.html')



crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

model = pickle.load(open(r'myapp/static/model.pkl','rb'))

def after_rainy_page(request):
    if request.method == 'POST':
        nitrogen = float(request.POST.get('Nitrogen'))
        phosphorus = float(request.POST.get('Phosphorus'))
        potessium = float(request.POST.get('Potessium'))
        temperature = float(request.POST.get('Temperature'))
        humidity = float(request.POST.get('Humidity'))
        pH = float(request.POST.get('pH'))
        rainfall = float(request.POST.get('Rainfall'))
        feature_list =  np.array([[nitrogen, phosphorus, potessium, temperature, humidity, pH, rainfall]])
        prediction = model.predict(feature_list).reshape(1,-1)

        print("prediction:::::::::::: ",prediction)

        result = prediction[0][0]
        if result in crop_dict:
            crop = crop_dict[result]
            print("{} is a best crop to be cultivated ".format(crop))
        else:
            print("Sorry are not able to recommend a proper crop for this environment")        
                        

    return render(request, 'after_rainy.html', {'result': result, 'crop_recommendation': crop})

