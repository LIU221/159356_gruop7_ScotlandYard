from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def choose_view(request, *args, **kwargs):
    if request.method=="GET":
        return render(request,"choose.html")
    else:
        number = request.POST.get("number")
        role = request.POST.get("role")
        dic={"a":"/static/Mrx.jpg"}
        if role == "mrx":
            return render(request,"board.html",dic)
        else:
            return render(request, "board.html", dic)

@login_required
def board_view(request):

    """View for the basic board.

    GET /boards/ returns a JSON representation of the game board.
    """
    #return HttpResponse("Sunck is a good man")
    return render(request, "board.html")