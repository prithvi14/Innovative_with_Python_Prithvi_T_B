from django.shortcuts import render,get_object_or_404,redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    student = Student.objects.all()
    return render(request,'BLOG_POSTS/POST_LIST.html',{'object_list':student})

def detailed_view(request,pk):
    student = get_object_or_404(Student,pk = pk)
    return render(request,'BLOG_POSTS/POST_DETAIL.html',{'object':student})

def update_view(request,pk):
    student = get_object_or_404(Student,pk = pk)
    form = StudentForm(request.POST or None,instance = student)
    if form.is_valid(): 
        form.save()
        return redirect('student_list')
    return render(request,'BLOG_POSTS/POST_FORM.html',{'form':form})

def delete(request,pk):
    student = get_object_or_404(Student,pk = pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request,'BLOG_POSTS/POST_DELETE.html',{'object':student})

def create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'BLOG_POSTS/POST_FORM.html',{'form':form})