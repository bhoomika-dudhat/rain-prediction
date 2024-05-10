from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'index.html')

def predictor_page(request):
    return render(request,'predictor.html')



def after_rainy_page(request):
    if request.method == 'POST':
        nitrogen = int(request.POST.get('Nitrogen'))
        phosphorus = int(request.POST.get('Phosphorus'))
        if 1 <= nitrogen and phosphorus <= 20:
            result = 1
        else:
            result = 2
    else:
        result = 3

    return render(request, 'after_rainy.html', {'result': result})
