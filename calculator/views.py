from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html', {'name': 'Python'})


# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     sumnum = val1 + val2
#     return render(request, 'result.html', {'result': sumnum})


def perform_two_numbers(request):
    try:
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        action = ''
        result_value = 0

        if request.POST.get('add_num'):
            action = 'added'
            result_value = val1 + val2
        if request.POST.get('subtract_num'):
            action = 'subtracted'
            result_value = val1 - val2
        if request.POST.get('multiply_num'):
            action = 'multiplied'
            result_value = val1 * val2
        if request.POST.get('divide_num'):
            action = 'divided'
            result_value = val1 / val2
    except Exception:
        action = 'has no action performed.'
        result_value = None
    return render(request, 'result.html', {'result': result_value, 'action_performed': action})


def index(request):
    return render(request, 'index.html')