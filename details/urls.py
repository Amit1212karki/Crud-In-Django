from django.urls import path
from details import views
from .views import switch_language

urlpatterns = [
    path('', views.contact_details, name='home'),
     path('add/',  views.add_details, name='add_details'),
     path('store/',  views.store_details, name='store_details'),
     path('edit/<int:id>/',  views.edit_details, name='edit_details'),
     path('update/<int:id>/',  views.update_details, name='update_details'),
     path('delete/<int:id>/',  views.delete_details, name='delete_details'),

    path('switch_language/<str:lang_code>/', switch_language, name='switch_language'),




]
