from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User

# Create your views here.

def changeMe(request):
    if request.method == "GET":
        return render(request, 'change_account_screen.html')
    elif request.method == "POST":

        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user_new_pass = request.POST.get('user_new_pass')

        if user_name and user_pass and user_new_pass != '':
            try:
                db_user_name = User.objects.get(name_user=user_name)
                db_user_pass = db_user_name.password_user
                if str(db_user_name) == str(user_name) and str(db_user_pass) == str(user_pass):
                    if user_new_pass == user_pass:
                        return JsonResponse({'message': 'Senha não pode ser igual a anterior', 'status':'invalid'})
                    else:
                        db_user_name.password_user = user_new_pass
                        db_user_name.save()
                        return JsonResponse({'message': 'Senha modificada!', 'status':'success'})
                        # Proxima tela...
                else:
                    return JsonResponse({"message": "credenciais inválidas!", "status":"invalid"})
            except User.DoesNotExist:
                return JsonResponse({"message": "Usuário não existe!", "status":"invalid"})
        else:
            return JsonResponse({"message":"Preencha todos os campos!", "status":"empty"})
