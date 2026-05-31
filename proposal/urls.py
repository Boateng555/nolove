from django.urls import path

from . import dashboard_views, views

urlpatterns = [
    path('', views.ask, name='ask'),
    path('yay/', views.yay, name='yay'),
    path('food/', views.food, name='food'),
    path('schedule/', views.schedule, name='schedule'),
    path('final/', views.final, name='final'),
    path('api/track-click/', views.track_click, name='track_click'),
    path('preview/ask/', views.preview_ask, name='preview_ask'),
    path('preview/yay/', views.preview_yay, name='preview_yay'),
    path('preview/food/', views.preview_food, name='preview_food'),
    path('preview/schedule/', views.preview_schedule, name='preview_schedule'),
    path('preview/final/', views.preview_final, name='preview_final'),
    path('dashboard/login/', dashboard_views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', dashboard_views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/api/live/', dashboard_views.live_activity, name='live_activity'),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
]
