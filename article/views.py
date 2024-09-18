from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from django.contrib import messages
from .forms import NewArticleForm, EditArticleForm
from django.http import JsonResponse


def index(request):
    return render(request,"index.html")

@login_required  # Kullanıcının giriş yapmış olduğunu kontrol eder; giriş yapılmadıysa, login sayfasına yönlendirir
def new(request):
    # Eğer HTTP methodu POST ise, yani form gönderilmişse bu blok çalışır
    if request.method == 'POST':
        # POST verilerini ve varsa dosyaları alarak formu oluşturur
        form = NewArticleForm(request.POST, request.FILES)
        
        # Form validasyonunu kontrol eder, eğer form geçerliyse bu blok çalışır
        if form.is_valid():
            # Formu kaydetmeden önce commit=False kullanarak henüz veritabanına yazmaz, böylece ekstra işlemler yapabiliriz
            article = form.save(commit=False)
            
            # Oturum açmış olan kullanıcıyı makalenin yazarı olarak atar
            article.author = request.user
            
            # Şimdi tüm alanlar tamamlandığı için makaleyi veritabanına kaydeder
            article.save()

            # Eğer istek bir AJAX isteğiyse, başarılı bir JSON yanıtı döner
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Success!'})

            return redirect('article:article_list')
        
        else:
            # Eğer formda bir hata varsa, form hatalarını loglar
            print("Form errors:", form.errors)
            
            # Hataları JSON formatında geri döner
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
    
    else:
        # Eğer GET isteği yapılmışsa, yani form doldurulmamışsa boş bir form oluşturur
        form = NewArticleForm()

    # Form sayfasını render eder, kullanıcıya boş veya hatalı formu gösterir
    return render(request, 'article/form.html', {'form': form, 'title': 'Write an Article'})

@login_required
def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    #Kullanıcı admin ya da blog sahibi mi?
    if not (request.user.is_staff or article.author == request.user):
        return JsonResponse({'error': 'You do not have permission to edit this article.'}, status=403)

    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Blog updated successfully!'})
            messages.success(request, 'Blog updated successfully!')
            return redirect('index')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = EditArticleForm(instance=article)

    return render(request, 'article/edit_form.html', {
        'form': form,
        'title': 'Edit Article',
        'article': article
    })

@login_required
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if not (request.user.is_staff or article.author == request.user):
        return JsonResponse({'error': 'You do not have permission to delete this article.'}, status=403)

    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        article.delete()
        return JsonResponse({'success': True, 'message': 'Article deleted successfully.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})   

@login_required    
def article_list(request):
    # Veritabanından tüm blogları çekiyoruz
    articles = Article.objects.all().order_by('-created_date')  # Tarihe göre sıralama (en yeni bloglar en üstte)
    
    return render(request, 'article/article_list.html', {
        'articles': articles,
        'title': 'Blog List'
    })

def article_detail(request, pk):
    # PK'ye göre blogu bul ve kullanıcıya göster
    article = get_object_or_404(Article, pk=pk)
    
    return render(request, 'article/article_detail.html', {
        'article': article,
        'title': article.title
    })

