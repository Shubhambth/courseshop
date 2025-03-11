from django.db import models
from main.models import CustomUser
from django.utils.text import slugify


    
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50, choices=[("Beginner", "Beginner"), ("Intermediate", "Intermediate"), ("Advanced", "Advanced")])
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    rating = models.FloatField(default=4.5)
    video_url = models.URLField(blank=True, null=True)
    learning_points = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="course_images/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=255)
    content = models.TextField()  # Lesson details (could be HTML)
    video_url = models.URLField(blank=True, null=True)  # Optional video link
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"] 

    def __str__(self):
        return self.title
    

class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevent duplicate enrollments

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"

