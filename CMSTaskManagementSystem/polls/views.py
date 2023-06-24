from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from polls.models import Boards, Tasks, Asigments
from .models import Boards
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm
from .forms import BoardForm
from django.urls import reverse
from django.contrib.auth.models import User

def index(request):
    request.user
    if request.user.is_authenticated:
        return redirect("board_selector")
    return render(request, 'polls/index.html')

@login_required
def board(request, board_id):

    
    board = Boards.objects.get(id=board_id)
    try:
        temp = Asigments.objects.filter(bid = board)
        users = []
        for x in temp:
            users.append(x.uid)

    except Asigments.DoesNotExist:
        users = []
        
    tasks_todo = Tasks.objects.filter(fcolumn=board, state=0)
    tasks_inprog = Tasks.objects.filter(fcolumn=board, state=1)
    tasks_done = Tasks.objects.filter(fcolumn=board, state=2)
    admin = False
    if request.user == board.creator:
        admin = True
    return render(request, 'polls/board.html', {'t_todo':tasks_todo, 't_inprog':tasks_inprog, 't_done': tasks_done, 'board_id' : board_id, 'users':users, 'admin': admin})
    #else:
        #return redirect('board_selector')
    

@login_required
def add_board(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.creator = request.user
            board.save()
            return redirect('board_selector')
    else:
        form = BoardForm()
    return render(request, 'polls/add_board.html', {'form': form})

@login_required
def delete_board(request , board_id):
        board = Boards.objects.filter(id=board_id)
        board.delete()
        return redirect('board_selector')

@login_required
def add_task(request):
    if request.method == 'POST':
        board_id = request.POST.get('board_id')
        task_title = request.POST.get('task_name')
        description = request.POST.get('task_descr')
        board = Boards.objects.get(id=board_id)
        task = Tasks(title=task_title, description=description, state = 0, fcolumn = board)
        task.save()
        url = reverse('board', kwargs={'board_id': board_id})
        return redirect(url)
    return render(request, 'polls/board.html')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'})

@login_required
def get_task(request, task_id):
    try:
        task = Tasks.objects.get(id=task_id)
        response = {
            'title': task.title,
            'description': task.description,
        }
        
        return JsonResponse(response)
    except Tasks.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

@login_required
def update_task_state(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        column_id = request.POST.get('column_id')

        task = Tasks.objects.get(id=task_id)
        task.state = column_id
        task.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

@login_required
def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        task.title = title
        task.description = description
        task.save()

        return JsonResponse({'status': 'success', 'message': 'Task updated successfully.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@login_required
def get_columns(request):
    if request.method == 'POST':
        board = request.POST.get('board')
        boardid = Boards.objects.filter(name=board).get(board_id=id)
        tasks_todo = Tasks.objects.filter(fcolumn_id=boardid, state=0)
        tasks_inprog = Tasks.objects.filter(fcolumn_id=boardid, state=1)
        tasks_done = Tasks.objects.filter(fcolumn_id=boardid, state=2)

    return render(request, 'polls/board.html', {'tasks_todo':tasks_todo, 'tasks_inprog': tasks_inprog, 'tasks_done': tasks_done})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})


def first_board(request):
    return render(request, 'polls/first_board.html')

def add_user(request, board_id):
    if request.method == 'POST':
        board_id = request.POST.get('board_id')
    return render(request, 'polls/add_user.html', {'board_id': board_id})

def board_selector(request):
    boards_created_by_user = Boards.objects.filter(creator=request.user)
    boards_assigned_to_user = Boards.objects.filter(asigments__uid=request.user)
    boards = (boards_created_by_user | boards_assigned_to_user).distinct()
    return render(request, 'polls/board_selector.html', {'boards': boards})


def add_user_next(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        board_id = request.POST.get('board_id')
        

        if not User.objects.filter(username=username).exists():
            error_message = "User does not exists"
            url = 'polls/add_user.html'
            print(error_message)
            return render(request, 'polls/error.html', {'error_message': error_message})
        
        user = User.objects.get(username=username)
        board = Boards.objects.get(id=board_id)

        if Asigments.objects.filter(uid=user, bid = board).exists():
            error_message = "User already added to board"
            url = 'polls/add_user.html'
            print(error_message)
            return render(request, 'polls/error.html', {'error_message': error_message})


        asigments = Asigments(bid=board, uid=user)
        asigments.save()
        url = "/board/" + board_id + "/"
        return redirect(url)
    else:
        return render(request, 'board_selector.html')

def leave_board(request, board_id):
    user = request.user
    board = Boards.objects.get(id=board_id)
    asigments = Asigments.objects.filter(uid=user)
    asigments.delete()
    return redirect('board_selector')
