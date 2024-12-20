from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movie
    path('', views.movies, name='movies'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # review
    path('<int:movie_pk>/reviews/create', views.review_create, name='review_create'),
    path('<int:movie_pk>/reviews/<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    
    # 영화 추천
    path('for-you/<int:movie_pk>/', views.for_you, name='for_you'),
    path('for-you2/<int:movie_pk>/', views.for_you2, name='for_you2'),
    path('for-you3/<int:movie_pk>/', views.for_you3, name='for_you3'),
    path('for-you4/<int:movie_pk>/', views.for_you4, name='for_you4'),
    path('for-you5/', views.for_you5, name='for_you5'),
]