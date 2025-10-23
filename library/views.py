from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

from .models import Category, Item, Post

def home(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        library_name = request.POST.get("library_name")
        url = request.POST.get("url")
        description = request.POST.get("description")
        category_id = request.POST.get("category")

        category = Category.objects.get(id=category_id)

        post = Post(
            full_name=full_name,
            email=email,
            library_name=library_name,
            url=url,
            description=description,
            category=category
        )

        post.save()

        messages.success(request, "¡Gracias por tu sugerencia! La revisaremos pronto.")

        return redirect(reverse("home") + "#contact")

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