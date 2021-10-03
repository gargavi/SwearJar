from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import User, Log, Jar
from .forms import AddPenalty


def index(request):
    user_list = User.objects.all()
    if request.method == "POST":
        form = AddPenalty(request.POST)
        if form.is_valid():
            jar_object = get_object_or_404(Jar, pk = form.cleaned_data["jar"])
            jar_object.create_log(
                content = form.cleaned_data["what"],
                penalty = form.cleaned_data["amount"],
                submitter = form.cleaned_data["submitter"]
            )
            jar_object.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AddPenalty()

    context = {
        "users": user_list,
        "form": form,
    }

    return render(request, 'jar/index.html', context)

def return_jar(request, jar_index):
    return HttpResponse(f"This is where jar_index {jar_index} is")

def user_page(request, user_id, jar_id = None):
    try:
        user = User.objects.get(pk = user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if jar_id is not None:
        try:
            jar = user.jar_set.get(pk = jar_id)
        except Jar.DoesNotExist:
            raise Http404("Jar Does not Exist")
        context = {
            'user': user,
            'jar': jar
        }
    else:
        context = {
            'user': user,
            'jar': None
        }

    return render(request, 'jar/user.html', context = context)


def jar_page(request, jar_id):
    try:
        jar = Jar.objects.get(pk = jar_id)
    except Jar.DoesNotExist:
        raise Http404("Jar does not exist")

    return render(request, "jar/jar.html", context = {"jar": jar})

# def submit(request):
#     user_list = User.objects.all()
#     if request.method == "POST":
#         form = AddPenalty(request.POST)
#         if form.is_valid():
#             jar_object = get_object_or_404(Jar, pk = form.cleaned_data["jar"])
#             jar_object.create_log(
#                 content = form.cleaned_data["what"],
#                 penalty = form.cleaned_data["amount"])
#             jar_object.save()
#             return HttpResponseRedirect(reverse('index'))
#     else:
#         form = AddPenalty()
#
#     context = {
#         "users": user_list,
#         "form": form,
#     }
#
#     return render(request, 'jar/index.html', context)
