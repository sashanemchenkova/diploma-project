from django.contrib import messages
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *


def index(request):
    return render(request, 'diet_diary/index.html')


def daily_norm(request):
    if request.method == 'POST':
        form = UserDailyNorm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserDailyNorm()
    return render(request, 'diet_diary/daily_norm.html',
                  context={'form': form})


def food_ration(request):
    return render(request, 'diet_diary/food_ration.html', {
        'categories': Category.objects.order_by('name'),
        'title': 'Food ration',
    })


def category_detail(request, category_id: int):
    return render(request, 'diet_diary/category_detail.html', {
        'category': get_object_or_404(Category, id=category_id),
    })


def product_view(request, product_id: int):
    return render(request, 'diet_diary/product_view.html', {
        'product': get_object_or_404(Product, id=product_id),
    })


def search(request):
    products = Product.objects.filter(name__icontains=request.POST['search'])
    pagin = Paginator(products, 5)
    page = request.GET.get('page')
    obj = pagin.get_page(page)
    return render(request, 'diet_diary/search.html', {
        'products': products, 'page': obj,
    })


def results(request):
    user_result = 0.0
    p = 0.0
    f = 0.0
    c = 0.0
    form = UserDailyNorm(request.POST or None)
    if form.is_valid():
        current_weight = form.cleaned_data.get('current_weight')
        current_height = form.cleaned_data.get('current_height')
        age = form.cleaned_data.get('age')
        gender = form.cleaned_data.get('gender')
        activity_level = form.cleaned_data.get('activity_level')
        goal = form.cleaned_data.get('goal')
        if gender.name == 'Male':
            user_result = 88.36 + (13.4 * current_weight) + (4.8 * current_height) - (5.7 * age)
        else:
            if gender.name == 'Female':
                user_result = 447.6 + (9.2 * current_weight) + (3.1 * current_height) - (4.3 * age)
        if activity_level.name == 'Low activity':
            user_result *= 1.2
        elif activity_level.name == 'Workout 1 - 3 times a week':
            user_result *= 1.375
        elif activity_level.name == 'Workout 3 - 5 times a week':
            user_result *= 1.55
        elif activity_level.name == 'Daily workouts':
            user_result *= 1.725
        elif activity_level.name == 'Daily intense workouts':
            user_result *= 1.9
        if goal.name == 'Lose weight':
            user_result -= 0.175 * user_result
        elif goal.name == 'Weight gain':
            user_result += 0.175 * user_result
        p = user_result * 0.3 / 4
        f = user_result * 0.3 / 9
        c = user_result * 0.4 / 4
    context = {'user_result': round(user_result, 1), 'title': 'Results', 'p': round(p, 1), 'f': round(f, 1),
               'c': round(c, 1)}
    return render(request, 'diet_diary/results.html', context)


def add_to_cart(request):
    assert request.method == 'POST'
    product_id = request.POST['product_id']
    product = get_object_or_404(Product, id=product_id)
    request.user.profile.ensure_cart().add_product(product)
    return redirect('diet_diary:product_view', product_id)


def cart(request):
    k = 0.0
    p = 0.0
    f = 0.0
    c = 0.0
    all_notes = Note.objects.all()
    for get_note in all_notes:
        k = get_note.total_res
        p = get_note.total_p
        f = get_note.total_f
        c = get_note.total_c
    context = {
        'all_notes': all_notes,
        'k': k,
        'p': p,
        'f': f,
        'c': c,
    }
    request.user.profile.ensure_cart()
    return render(request, 'diet_diary/cart.html', context)


@login_required()
def edit_m(request):
    cart = request.user.profile.cart.all_notes.get(id=request.POST['a'])
    cart.massa = request.POST['new_massa']
    cart.save()
    return redirect('diet_diary:cart')


@login_required
def finish_my_day(request):
    profile = request.user.profile
    note = profile.cart
    note.save()
    profile.cart = Note.objects.create(profile=profile)
    profile.save()
    messages.success(request, "You have completed the diet diary for today!")
    return render(request, 'diet_diary/finish.html', {'note': note})


def del_all(request):
    assert request.method == "POST"
    note = request.user.profile.cart
    note.delete()
    note.save()
    return redirect('diet_diary:cart')


@login_required()
def del_note(request):
    cart = request.user.profile.cart
    cart.all_notes.filter(id=request.POST['a']).delete()
    cart.save()
    messages.success(request, "Product delete")
    return redirect('diet_diary:cart')


@login_required
def prev_d(request):
    all_notes = request.user.profile.notes.all().order_by('id').reverse()[:7]
    pagination = Paginator(all_notes, 7)
    page = request.GET.get('page')
    obt = pagination.get_page(page)
    return render(request, 'diet_diary/previous_days.html', {'all_notes': all_notes, 'page': obt, })


@login_required
def user_profile(request):
    user = request.user
    notes = request.user.profile.notes.all().order_by('id').reverse()[:5]
    context = {'user': user, 'notes': notes}
    return render(request, 'diet_diary/user_profile.html', context)


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = request.user
            user.username = username
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request, "You have changed information ;)")
            return redirect('diet_diary:update_profile')
    else:
        form = UserForm(instance=request.user)
    return render(request, 'diet_diary/update_profile.html', {'form': form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('diet_diary:index')
        messages.error(request, "Invalid information.")
    form = NewUserForm()
    return render(request, "registration/register.html", context={"form": form})
