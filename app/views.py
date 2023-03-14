from django.shortcuts import render
def greater(request):
    d={'a':10,'b':20}
    return render(request,'greater.html',context=d)
# Create your views here.
