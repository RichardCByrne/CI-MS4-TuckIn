from django.http import response
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from django.db.models import Q
from .models import FoodItem, Restaurant, MenuSection, Cuisine


def all_restaurants(request):
    restaurants = Restaurant.objects.all()
    all_restaurants = None
    query_cuisine = None
    query_search = None
    cuisine = None

    if request.GET:
        # Sorting by Cuisine (referenced Boutique Ado)
        if 'cuisine' in request.GET:
            cuisine = request.GET['cuisine']
            restaurants = restaurants.filter(Q(cuisine__name__icontains=cuisine))
            # Turns list of strings from url to cuisine object for use in template
            cuisine = Cuisine.objects.filter(Q(name=cuisine))

        # Search Request (referenced Boutique Ado)
        if 'q' in request.GET:
            query_search = request.GET['q']
            if not query_search:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('restaurants'))
            # Referenced book for advanced queries https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query.html
            queries = Q(name__icontains=query_search) | Q(friendly_name__icontains=query_search) | Q(
                description__icontains=query_search) | Q(cuisine__name__icontains=query_search) | Q(
                    menusection__name__icontains=query_search) | Q(
                        menusection__friendly_name__icontains=query_search) | Q(
                        menusection__fooditem__name__icontains=query_search) | Q(
                            menusection__fooditem__friendly_name__icontains=query_search) | Q(
                                menusection__fooditem__description__icontains=query_search)
            restaurants = restaurants.filter(queries).distinct()
    
    all_cuisines = Cuisine.objects.all()

    context =  {
        'restaurants': restaurants,
        'search_term': query_search,
        'all_cuisines': all_cuisines,
        'current_cuisine': cuisine,
    }
    return render(request, 'restaurants/restaurants.html', context)


def restaurant_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu_sections = MenuSection.objects.all().filter(restaurant=restaurant)

    food_items = []
    for section in menu_sections:
        food_items += FoodItem.objects.all().filter(menu_section=section)

    context = {
        'restaurant': restaurant,
        'menu_sections': menu_sections,
        'food_items': food_items,
    }
    return render(request, 'restaurants/restaurant_menu.html', context)
