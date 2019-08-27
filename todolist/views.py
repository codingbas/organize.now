# Create your views here. 
# This codesnippet is from https://medium.com/fbdevclagos/how-to-build-a-todo-app-with-django-17afdc4a8f8c 

from django.shortcuts import render,redirect, reverse
from .models import TodoList, Category
from django.contrib.auth.models import User

def index(request): #the index view
    #redirect of not authenticated
    if not request.user.is_authenticated():
        return redirect(reverse('login'))
    
    # get the user
    user = User.objects.filter(email=request.user.email).first()
    
    # @TODO: curerntly we fetch all todo's, only fetch 10 if user.userprofile.is_premium = false
    if user.userprofile.is_premium:
        todos = TodoList.objects.all()
    else:
        todos = TodoList.objects.all()[:10]

    # get current todo_count 
    todo_count = TodoList.objects.count()
    
    # if user is not_premium and todo_count > 10 set a variable show_premium_message to true
    show_premium_message = False
    if user.userprofile.is_premium == False and todo_count > 10:
        show_premium_message = True
    
    
    
        
    
    
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        #checking if there is a request to add a todo
        if "taskAdd" in request.POST: 
            # todo data
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            
            # reload after todo addition
            return redirect("/")
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "todolist.html", {
        "todos": todos,
        "categories":categories,
        "show_premium_message": show_premium_message
    })
    
