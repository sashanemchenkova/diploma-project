from django.urls import path

from . import views


app_name = 'diet_diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('daily_norm', views.daily_norm, name='daily_norm'),
    path('food_ration', views.food_ration, name='food_ration'),
    path('category_detail/<int:category_id>', views.category_detail, name='category_detail'),
    path('product_view/<int:product_id>', views.product_view, name='product_view'),
    path('results', views.results, name='results'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('edit_m/', views.edit_m, name='edit_m'),
    # path('repeat/<int:note_id>/', views.repeat, name='repeat'),
    path('finish_my_day/', views.finish_my_day, name='finish_my_day'),
    path('del_all/', views.del_all, name='del_all'),
    path('del_note/', views.del_note, name='del_note'),
    path('previous_days/', views.prev_d, name='previous_days'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_profile/update_profile/', views.update_profile, name='update_profile'),
    path("register/", views.register_request, name="register"),


]