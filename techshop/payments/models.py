from django.db import models
from django.contrib.auth.models import User
from main.models import CustomUser
from courses.models import Course , Enrollment

 # Assuming courses is your course app

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')], default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)



    def enroll_user(self):
        """Enroll the user in the course after successful payment."""
        enrollment, created = Enrollment.objects.get_or_create(user=self.user, course=self.course)
        return enrollment
    
    def __str__(self):
        return f"Payment by {self.user.username} for {self.course.title}"
    


