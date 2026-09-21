from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category
from .forms import CategoryForm

# Create your views here.


def category_list(request):
    categories = Category.objects.annotate(tasks_count=Count('tasks'))
    return render(request, 'categories/category_list.html', {'categories': categories})


def category_details(request, pk):
    category = get_object_or_404(Category.objects.annotate(
        tasks_count=Count('tasks')), pk=pk)
    return render(request, 'categories/category_details.html', {'category': category})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('categories:category_details', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'categories/category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            return redirect('categories:category_details', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:category_list')
    return render(request, 'categories/category_delete_confirmation.html', {'category': category})
