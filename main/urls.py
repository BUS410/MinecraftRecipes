from django.urls import path

from . import views


urlpatterns = [
    path('', views.RecipesListView.as_view(), name='home'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipe'),
    path('category/<int:cat_id>', views.CategoryListView.as_view(), name='category'),
]