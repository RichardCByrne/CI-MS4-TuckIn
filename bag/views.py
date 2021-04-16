from restaurants.models import FoodItem, MenuSection, Restaurant
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages


def view_bag(request):
    bag = request.session.get('bag', {})
    context = {
        'bag': bag,
    }
    return render(request, 'bag/bag.html')


def add_to_bag(request):
    # Get data
    food_id = request.POST.get('this_food')
    food = get_object_or_404(FoodItem, pk=food_id)
    menu_section = get_object_or_404(MenuSection, fooditem__name=food.name)
    restaurant = get_object_or_404(Restaurant, menusection__name=menu_section.name)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    additional_details = request.POST.get('additional-details')
    bag = request.session.get('bag', {})
    bag_keys = list(bag.keys())

    # If bag has something in it
    if bag_keys:
        # If food from this restaurant is already in the bag
        if bag_keys[0] == restaurant.name:
            # If the same food exists in the bag, update quantity
            if food_id in list(bag[restaurant.name].keys()):
                bag[restaurant.name][food_id]['quantity'] += quantity
                bag[restaurant.name][food_id]['additional_details'] += ", " + additional_details
                messages.success(request, f"Updated quantity of {food.friendly_name} to {bag[restaurant.name][food_id]['quantity']}")
            # Else add food and set quantity
            else:
                bag[restaurant.name][food_id] = {"quantity": quantity, "additional_details": additional_details}
                messages.success(request, f"Added {bag[restaurant.name][food_id]['quantity']} {food.friendly_name} to your cart")
        # Else if there is food from another restaurant in the bag, throw error (elif used for extra verification)
        elif bag_keys[0] != restaurant.name:
            messages.error(request, "There is already food from another restaurant in your cart.")
    # Else add food to bag
    else:
        bag[restaurant.name] = {food_id: {"quantity": quantity, "additional_details": additional_details}}
        # If quantity being added is more than 1, say quantity in toast
        if quantity > 1:
            messages.success(request, f"Added {quantity} of {food.friendly_name} to your cart")
        else:
            messages.success(request, f"Added {food.friendly_name} to your cart")
        

    request.session['bag'] = bag

    return redirect(redirect_url)
