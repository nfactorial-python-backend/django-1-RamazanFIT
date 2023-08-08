from django.shortcuts import render
from django.http import HttpResponse


def app(request):
    return HttpResponse("Hello, nfactorial school!")


def plus(request, first : int, second : int) -> int:
    return HttpResponse(first + second)

def do_upper(request, text : str) -> str:
    return HttpResponse(text.upper())


def check_palindrome(request, word : str) -> bool:
    if word == word[::-1]:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def calculator(request, first : int, operation : str, second : int) -> int | float:
    if operation == "add":
        return HttpResponse(first + second)
    elif operation == "sub":
        return HttpResponse(first - second)
    elif operation == "mult":
        return HttpResponse(first * second)
    else:
        return HttpResponse(first / second)