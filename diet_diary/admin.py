from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Category, Product, Gender, Activity, Goal, GetNote, Note, Profile

# class ProductAdmin(admin.ModelAdmin):
# readonly_fields = ('kcal', )


admin.site.register(Gender)
admin.site.register(Activity)
admin.site.register(Goal)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductInLine(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInLine]


class NoteInline(admin.TabularInline):
    model = Note
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [NoteInline]


@admin.register(GetNote)
class GetNoteAdmin(admin.ModelAdmin):
    pass


class GetNoteInline(admin.TabularInline):
    model = GetNote
    extra = 0


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    inlines = [GetNoteInline]


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
