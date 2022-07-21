from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'home.html')
def results(request):
    num = int(request.GET['n1'])
    factorial = 1
    if num < 0:
        print(" Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
 
    val=(f"The factorial of {num} is {factorial}")
   
    return render(request,'home.html',{'val':val})