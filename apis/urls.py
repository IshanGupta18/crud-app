from django.urls import path
from .views import add_box, update_box, list_boxes, list_my_boxes, delete_box

urlpatterns = [
    path('boxes/', list_boxes, name='list_boxes'),
    path('my-boxes/', list_my_boxes, name='list_my_boxes'),
    path('boxes/add/', add_box, name='add_box'),
    path('boxes/<int:box_id>/update/', update_box, name='update_box'),
    path('boxes/<int:box_id>/delete/', delete_box, name='delete_box'),
]
