from django.contrib import admin
from django.urls import path


from app.views import hello_view, hey_view, age_in_view, order_total_view

urlpatterns = [
    path("hello/", hello_view),
    path("hey/<str:name>/", hey_view),
    path("age-in/<int:end>/<int:birthday>/", age_in_view),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>/", order_total_view),
    path("admin/", admin.site.urls),
]
