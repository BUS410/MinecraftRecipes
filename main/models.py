from django.db import models
from django.utils.text import slugify

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=128, verbose_name='Имя предмета', unique=True)
	image = models.ImageField(upload_to='items/', verbose_name='Изображение')
	item_category = models.ForeignKey('ItemCategory', on_delete=models.PROTECT,
		null=True, verbose_name='Категория')
	slug = models.SlugField(max_length=256, null=False, unique=True, db_index=True,
		verbose_name='URL')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предметы'

class ItemCategory(models.Model):
	name = models.CharField(max_length=128, verbose_name='Имя категории', unique=True)
	slug = models.SlugField(max_length=256, null=False, unique=True, db_index=True,
		verbose_name='URL')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория предмета'
		verbose_name_plural = 'Категории предметов'

class Recipe(models.Model):
	result = models.ForeignKey('Item', on_delete=models.CASCADE,
		verbose_name='Результ', related_name='result_items')
	left_up_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Левый верхний предмет', related_name='left_up_items')
	up_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Верхний предмет', related_name='up_items')
	right_up_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Правый верхний предмет', related_name='right_up_items')
	left_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Левый предмет', related_name='left_items')
	middle_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Средний предмет', related_name='middle_items')
	right_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Правый предмет', related_name='right_items')
	left_down_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Левый нижний предмет', related_name='left_down_items')
	down_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True, verbose_name='Нижний предмет', related_name='down_items')
	right_down_item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True,
		blank=True,verbose_name='Правый нижний предмет', related_name='right_down_items')
	slug = models.SlugField(max_length=256, null=False, unique=True,db_index=True,
		verbose_name='URL')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(f'{self.result.name}-recipe')
		return super().save(*args, **kwargs)

	def __str__(self):
		return f'{self.result.name} рецепт'

	class Meta:
		verbose_name = 'Рецепт'
		verbose_name_plural = 'Рецепты'
