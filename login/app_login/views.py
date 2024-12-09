from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User
global_user = ''
# Create your views here.

def loginMe(request):
    if request.method == "GET":
        return render(request, 'login_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')

        if user_name and user_pass != '':
            try:
                db_user_name = User.objects.get(name_user=user_name)
                db_user_pass = db_user_name.password_user
                if str(db_user_name) == str(user_name) and str(db_user_pass) == str(user_pass):
                    request.session['user_name'] = user_name
                    return JsonResponse({'message': f'{user_name}', 'status':'success'})
                # Proxima tela...
                else:
                    return JsonResponse({"message": "*credenciais inválidas!", "status":"invalid"})
            except User.DoesNotExist:
                return JsonResponse({"message": "*Usuário não existe!", "status":"invalid"})
        else:
            return JsonResponse({"message":"*Preencha todos os campos!", "status":"empty"})
        