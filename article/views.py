from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib import messages
from .forms import NewArticleForm#, EditDroneForm, RentalForm
from django.http import JsonResponse


def index(request):
    return render(request,"index.html")

@login_required
def new(request):
    if request.method=='POST':
        form=NewArticleForm(request.POST)
        
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Giriş yapan kullanıcıyı yazar olarak ayarla
            article.save()
                        
            return redirect('index')
    
    else:
        form=NewArticleForm()
    
    return render(request, 'article/form.html',{
        'form':form,
        'title':'New Article'
    })