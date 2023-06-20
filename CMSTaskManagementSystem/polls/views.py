from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from polls.models import Boards, Tasks, Asigments
import logging
from django.conf import settings
from django.contrib.auth import get_user_model
from builtins import print
from .models import Boards

logger = logging.getLogger(__name__)

def home(request):
    
    return render(request, 'polls/home.html')

@login_required
def board(request):
    current_user = request.user
    boards = Boards.objects.filter(creator=current_user)

    return render(request, 'polls/board.html', {'boards': boards})

@login_required
def add_board(request):
    if request.method == 'POST':
        board_name = request.POST.get('board_name')
        creator = request.user
        board = Boards(name=board_name, creator=creator)
        board.save()
        return redirect('board')
    return render(request, 'board.html')



class CustomLoginView(LoginView):
    template_name = 'polls/login.html'
