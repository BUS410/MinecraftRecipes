from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models


# Create your views here.
class RecipesListView(ListView):
	model = models.Recipe
	template_name = 'index.html'
	context_object_name = 'recipes'


class CategoryListView(ListView):
	model = models.Recipe
	template_name = 'index.html'
	context_object_name = 'recipes'

	def get_queryset(self):
		return models.Recipe.objects.filter(result__item_category=self.kwargs['cat_id'])


class RecipeDetailView(DetailView):
	model = models.Recipe
	template_name = 'recipe.html'
	context_object_name = 'recipe'
