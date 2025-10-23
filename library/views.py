from django.shortcuts import render
from django.core.paginator import Paginator
from math import ceil

from .models import Category, Item

def home(request):
    categories = Category.objects.all()
    items = Item.objects.all().order_by("-created_at")
    latest_items = items[:4]

    search = request.GET.get("search", "")
    category = request.GET.get("category", "")

    if search:
        items = items.filter(name__icontains=search) | items.filter(description__icontains=search)

    if category:
        items = items.filter(categories__id=category)

    paginator = Paginator(items, 20)
    page_number = request.GET.get("page")
    items = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "items": items,
        "latest_items": latest_items
    }

    return render(request, "index.html", context)