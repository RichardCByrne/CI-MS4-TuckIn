from django.shortcuts import get_object_or_404, render
from bag.contexts import bag_contents
from restaurants.models import Restaurant
from checkout.forms import OrderForm
from profiles.models import CustomerProfile


def checkout_address(request):
    # Create instance of order form
    address_form = OrderForm()

    context = {
        'address_form': address_form,
    }
    return render(request, 'checkout/checkout-address.html', context)


def checkout_time(request):
    # Add address data to session
    if request.method == "POST":
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
        }
        request.session['address'] = form_data

        # Add restuarant name to session
        bag = request.session.get('bag', {})
        restaurant = list(bag.keys())
        request.session['restaurant'] = restaurant[0]

    # Get variables
    address_form = request.session.get('address')

    context = {
        'address_form': address_form,
    }
    return render(request, 'checkout/checkout-time.html', context)


def checkout_payment(request):
    # Add selected delivery time to session
    bag = request.session.get('bag', {})
    if request.method == "POST" and 'delivery_time' in request.POST:
        delivery_time = request.POST.get('delivery_time')
        request.session['delivery_time'] = delivery_time
    
    restaurant = request.session.get('restaurant')
    order_restaurant = get_object_or_404(Restaurant, name=restaurant)
    
    # Generate Order Form
    if request.user.is_authenticated:
        profile = get_object_or_404(CustomerProfile, customer=request.user)
        # Put saved details into fields
        order_form = OrderForm(initial={
            'full_name': profile.full_name,
            'email': profile.customer.email,
            'phone_number': profile.default_phone_number,
            'postcode': profile.default_postcode,
            'address_1': profile.default_address_1,
            'address_2': profile.default_address_2,
            'order_restaurant': order_restaurant,
        })
        order_form.save(commit=False)
    else:
        # Create order form using session data
        address_form = request.session.get('address')
        order_form = OrderForm(initial={
            'full_name': address_form.full_name,
            'email': address_form.customer.email,
            'phone_number': address_form.default_phone_number,
            'postcode': address_form.default_postcode,
            'address_1': address_form.default_address_1,
            'address_2': address_form.default_address_2,
            'order_restaurant': order_restaurant,
        })
        order_form.save(commit=False)

    # Get variables
    delivery_time = request.session.get('delivery_time')
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    context = {
        'order_form': order_form,
        'delivery_time': delivery_time,
    }
    return render(request, 'checkout/checkout-payment.html', context)


def order_confirmation(request):
    context = {}
    return render(request, 'checkout/order_confirmation.html', context)
