from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse

class PermissionMiddleware:
    """
    Bu middleware, 403 (Forbidden) hatalarını yakalar ve kullanıcıyı uygun şekilde yönlendirir.
    AJAX istekleri için JSON yanıtı döndürür, normal istekler için kullanıcıyı ana sayfaya yönlendirir.
    """
    #Middleware'i başlatır.
    def __init__(self, get_response):       
        self.get_response = get_response
        
    # Her istek için çağrılır.
    def __call__(self, request):      
        # İsteği işle ve yanıtı al
        response = self.get_response(request)

        # Eğer yanıt 403 (Forbidden) ise, özel işlem yap
        if response.status_code == 403:
            # AJAX isteği kontrolü
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # AJAX isteği için JSON yanıtı döndür
                return JsonResponse({
                    "success": False, 
                    "message": "You do not have permission to perform this action."
                }, status=403)
            
            # Normal istek için hata mesajı ekle ve ana sayfaya yönlendir
            messages.error(request, "You do not have permission to perform this action.")
            return redirect('index')

        # Diğer tüm durumlar için orijinal yanıtı döndür
        return response