from django.shortcuts import render

def main(request):
    return render(request, 'blog/tab.html', {})

def sub1(request):
    return render(request, 'blog/2016.html', {})

def sub2(request):
    return render(request, 'blog/2017.html', {})

def sub3(request):
    return render(request, 'blog/2018.html', {})

def sub4(request):
    return render(request, 'blog/all.html', {})
