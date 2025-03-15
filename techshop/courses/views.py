from django.shortcuts import render , get_object_or_404 , redirect
from .models import Course , Enrollment , Lesson
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from payments.models import Payment


def course(request):
    data = Course.objects.all()
    return render(request,'course.html',{'data':data})

@login_required
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    is_enrolled = Enrollment.objects.filter(user=request.user, course=course).exists()
    return render(request, 'course_detail.html', {'course': course,"is_enrolled": is_enrolled})



@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Check if student is already enrolled
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)

    if created:
        messages.success(request, f"You have successfully enrolled in {course.title}!")
    else:
        messages.info(request, "You are already enrolled in this course.")

    return redirect("course_detail", slug=course.slug)


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    # Get all lessons for the same course, ordered by ID
    lessons = list(lesson.course.lessons.order_by("id"))

    has_paid = Payment.objects.filter(user=request.user, course=lesson.course, status="COMPLETED").exists()

    if not has_paid:
        return redirect('course_detail', slug=lesson.course.slug)

    # Find the index of the current lesson
    current_index = lessons.index(lesson) if lesson in lessons else -1

    # Get previous and next lesson
    previous_lesson = lessons[current_index - 1] if current_index > 0 else None
    next_lesson = lessons[current_index + 1] if current_index < len(lessons) - 1 else None

    return render(request, 'lesson_detail.html', {
        'lesson': lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson
    })
