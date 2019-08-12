from django.shortcuts import render

# Create your views here.
def info(request):
    teacher = ['NAME']
    students = ['홍길동','김길동','박길동']
    context = {
        'teacher': teacher,
        'students': students,
    }
    return render(request,'classroom.html',context)

def student(request, name):
    students = {'홍길동': 25,'김길동': 27,'박길동': 28}
    context = {
        'age': students[name],
        'name': name
    }
    return render(request,'student.html',context)