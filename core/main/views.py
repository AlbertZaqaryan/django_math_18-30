from django.shortcuts import render

# Create your views here.

def math(request):
    return render(request, 'math.html')

def calculator(request):
    return render(request, 'calculator.html')

def factorial(request):
    return render(request, 'factorial.html')

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    char = str(request.POST['char'])
    if char == '+':
        res = num1 + num2
    elif char == '-':
        res = num1 - num2
    elif char == '*':
        res = num1 * num2
    elif char == '/':
        res = num1 / num2
    return render(request, 'result.html', {'res':res})

def fact(request):
    n = int(request.POST['n'])
    res = 1
    for i in range(1, n + 1):
        res *= i
    return render(request, 'fact.html', {'res':res})

