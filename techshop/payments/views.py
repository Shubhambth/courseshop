import razorpay
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from courses.models import Course
from .models import Payment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

# Initialize Razorpay Client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@login_required
def create_order(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Create an order on Razorpay
    amount = int(course.price * 100)  # Razorpay works with paisa, so multiply by 100
    order_data = {
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1",
    }
    order = client.order.create(data=order_data)

    # Save payment details
    payment = Payment.objects.create(
        user=request.user,
        course=course,
        amount=course.price,
        razorpay_order_id=order["id"],
        status="PENDING"
    )

    return JsonResponse(order)

@csrf_exempt
def verify_payment(request):
    if request.method == "POST":
        data = request.POST
        try:
            payment = Payment.objects.get(razorpay_order_id=data["razorpay_order_id"])
            payment.razorpay_payment_id = data["razorpay_payment_id"]
            payment.razorpay_signature = data["razorpay_signature"]
            payment.status = "COMPLETED"
            payment.save()
            payment.enroll_user()
            return JsonResponse({"status": "success"})
        except Payment.DoesNotExist:
            return HttpResponseBadRequest("Invalid payment request")
    return HttpResponseBadRequest("Invalid request")
