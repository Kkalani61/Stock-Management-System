from django.db import models

# Create your models here.

# category_choice = (('', 'Electronics'), ('', 'Furniture'), ('IT Equipment', 'IT Equipment'), ('Stationary', "Stationary"))
# We are supposed to give two values, either way we can give that.

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	# subcategory = models.CharField(max_length=50,blank=True,null=True)

	def __str__(self):
		return self.name

class Subcategory(models.Model):
	subcategory = models.CharField(max_length=50,blank=True,null=True)

	def __str__(self):
		return self.subcategory
	



class Product(models.Model):
	prod_id = models.CharField(max_length=10,unique=True)
	prod_price = models.FloatField(blank=True,null=True)
	name = models.CharField(max_length=50,blank=True,null=True)
	category = models.ForeignKey(Category,blank=True,on_delete=models.CASCADE)
	

	def __str__(self):
		return self.name

	

class Stock(models.Model):
	category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE,null=True)
	subcategory = models.ForeignKey(Subcategory, blank=True, on_delete=models.CASCADE,null=True)
	# category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='1', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

<<<<<<< HEAD
	prod_id = models.CharField(max_length=20,blank=True,null=True)
=======

>>>>>>> 68cabe46be1757c39b6dec93ab5fb38ddea2ec90
	shipMode = models.CharField(max_length=50, blank=True,null=True)
	market = models.CharField(max_length=50, blank=True, null=True)
	sales = models.FloatField(default='0', blank=True, null=True)
	discount = models.FloatField(default='0', blank=True, null=True)
	profit = models.FloatField(default='0', blank=True, null=True)
	shipping_cost = models.FloatField(default='0', blank=True, null=True)
	order_priority = models.IntegerField(default='0', blank=True, null=True)
	shipday = models.IntegerField(blank=True, null=True)
	shipmonth = models.IntegerField(blank=True, null=True)
	shipyear = models.IntegerField(blank=True, null=True)
	orderday = models.IntegerField(blank=True, null=True)
	ordermonth = models.IntegerField(blank=True, null=True)
	orderyear = models.IntegerField(blank=True, null=True)
	prod_price = models.FloatField(default='0', blank=True, null=True)

	def __str__(self):
		return self.item_name


class StockHistory(models.Model):
	category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

	# shipMode = models.IntegerField(blank=True,null=True)
	# market = models.CharField(max_length=50,blank=True,null=True)
	# sales = models.FloatField(default='0',blank=True,null=True)
	# discount = models.FloatField(default='0',blank=True,null=True)
	# profit = models.FloatField(default='0',blank=True,null=True)
	# shipping_cost = models.FloatField(default='0',blank=True,null=True)
	# order_priority = models.IntegerField(default='0',blank=True,null=True)
	# shipday = models.IntegerField(blank=True,null=True)
	# shipmonth = models.IntegerField(blank=True,null=True)
	# shipyear = models.IntegerField(blank=True,null=True)
	# orderday = models.IntegerField(blank=True,null=True)
	# ordermonth = models.IntegerField(blank=True,null=True)
	# orderyear = models.IntegerField(blank=True,null=True)
	# prod_price = models.FloatField(default='0', blank=True, null=True)
