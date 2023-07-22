from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import movie
from .forms import MovieForm

# Create your views here.
def index(request):
    mov=movie.objects.all()
    context={
        'movie_list':mov
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'mv':m})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc= request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        m=movie(name=name,desc=desc,year=year,img=img)
        m.save()
    return render(request,'add.html')

def update(request,id):
    mov=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'m':mov})
def delete(request,id):
    if request.method=="POST":
        mov=movie.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')


