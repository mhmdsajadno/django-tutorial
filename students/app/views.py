from django.shortcuts import render, HttpResponse
from .db import database

def index(request):
    ctx = {"title": "Home 🏠", "db": database}
    return render(request, "index.html", ctx)


def menu(request, id):
    student = next((student for student in database if student.id == id), None)
    ctx = {"student": student}
    return render(request, "menu.html", ctx)


def search(request):
    q = request.GET.get('q', '').strip()
    results = []
    
    if q.isdigit():
        id_num = int(q)
        student = next((student for student in database if student.id == id_num), None)
        if student:
            results.append(student)
    
    else:
        q_lower = q.lower()
        results = [
            student for student in database
            if q_lower in student.firstname.lower() or q_lower in student.lastname.lower()
        ]
    
    ctx = {"results": results, "q": q}
    return render(request, "search.html", ctx)

