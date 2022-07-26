from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('add_book/',views.add,name='add_book'),
    path('add_book/addbook/',views.add_book,name="addbook"),
    path('add_book/delete/<int:id>',views.delete,name='delete'),
    path('add_book/update/<int:id>',views.update,name='update'),
    path('add_book/update/updatebook/<int:id>',views.update_book,name='updatebook')
]