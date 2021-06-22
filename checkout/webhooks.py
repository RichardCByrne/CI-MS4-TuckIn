import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from stripe.api_resources import payment_intent
from .webhook_handler import StripeWH_Handler
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Referenced https://stripe.com/docs/webhooks/build#example-code
@csrf_exempt  # Stripe doesn't send CSRF tokens
@require_POST  # Only react to post requests, reject GET requests
def webhook(request):
    # Set variables
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify its signature
    payload = request.data
    event = None

    try:
        # Get webhook from Stripe
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload exception handler
        return HttpResponse(content=e, status=400)
    except Exception as e:
        # Generic exception handler
        return HttpResponse(content=e, status=400)

    # Setup webhook handler
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }

    # Get webhook type from Stripe
    event_type = event['type']
    # Use generic handler if not available
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return HttpResponse(content=response, status=200)
