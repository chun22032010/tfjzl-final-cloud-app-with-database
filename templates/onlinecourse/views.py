from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission

def submit(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        return redirect('onlinecourse:show_exam_result', course_id=course.id)

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course, 'score': 100, 'message': "Congratulations"}
    return render(request, 'onlinecourse/exam_result.html', context)
