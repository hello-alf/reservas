from django.urls import re_path
from reservas.rooms.views import list_rooms

app_name = "rooms"
urlpatterns = [
    re_path(r'^v1/rooms/', view=list_rooms),
]
