from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def studs(request):
    users = [
        'student1', 'student2', 'student3', 'student4', 'student5', 'student6', 'student7',
    ]
    return render(request, 'studs.html')
def groups(request):
    groups = [
        'group1','group2','group3','group4','group5','group6',
    ]
    return render(request, 'groups.html')
def marks(request):
    return render(request, 'marks.html')
def others(request):
    return render(request, 'other.html')
