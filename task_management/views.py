from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  
from django.contrib import messages
from .models import Category, Task

# home page
def home_page(request):
    return render(request, 'tasks/home.html')

#create task 
@login_required
def create_task(request):
    User = get_user_model()

    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        location = request.POST.get('location')
        assigned_to_id = request.POST.get('assigned_to')

        # Fetch related objects
        category = Category.objects.get(pk=category_id)
        assigned_to = User.objects.get(pk=int(assigned_to_id))

        # Create the Task
        task = Task.objects.create(
            name=name,
            category=category,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            description=description,
            location=location,
            organizer=request.user,  
            assigned_to=assigned_to
        )

        return redirect('category_list')
    else:
        categories = Category.objects.all()
        users = User.objects.all()  
        return render(request, 'tasks/create_task.html', {'categories': categories, 'users': users})


#create category
def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        messages.success(request, "Category created successfully!")
        return redirect('home')
    return render(request, 'tasks/create_category.html')