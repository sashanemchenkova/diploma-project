from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    kcal = models.IntegerField(default=0.0)
    proteins = models.FloatField(default=0.0)
    fats = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class GetNote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
    note = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='all_notes')
    massa = models.FloatField(default=100.0)

    @property
    def k(self):
        return self.product.kcal * self.massa / 100


class Note(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f'id:{self.id} - {self.profile}'

    def add_product(self, product: Product):
        get_note = self.all_notes.filter(product=product).first()
        if not get_note:
            get_note = GetNote(product=product, note=self)
        get_note.save()

    @property
    def total_res(self):
        return sum(get_note.k for get_note in self.all_notes.all())


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cart = models.OneToOneField(Note, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='+')

    def __str__(self):
        return str(self.user)

    def ensure_cart(self):
        if not self.cart:
            self.cart = Note.objects.create(profile=self)
            self.save()
        return self.cart


class Gender(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Goal(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
