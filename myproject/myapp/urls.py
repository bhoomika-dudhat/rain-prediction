from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('index_page/',views.index_page),
   path('predictor_page/',views.predictor_page,name='predictor_page'),
   path('after_rainy_page/',views.after_rainy_page,name='after_rainy_page')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)