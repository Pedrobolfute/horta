from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *


# Create your views here.

def registerMe(request):
    if request.method == "GET":
        return render(request, 'create_account_screen.html')
    elif request.method == "POST":
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user_confirm_pass = request.POST.get('user_confirm_pass')
        user_job = request.POST.get('my_job') or None
        user_job_position = request.POST.get('my_job_position') or None
        user_job_salary = request.POST.get('my_job_salary') or None
        user_document = request.POST.get('my_document_type') or None
        user_document_number = request.POST.get('my_document_number') or None

        if user_name and user_pass and user_confirm_pass != '':
            if user_pass != user_confirm_pass:
                return JsonResponse({"message": "Senhas não coincidem!", "status": "ok"})
            else:
                if User.objects.filter(name_user=user_name).exists():
                    return JsonResponse({"message": "Usuário já existe", "status": "exist"})
                else:
                    user = User(name_user=user_name, password_user=user_pass)
                    user.save()
    
                    job = Job(company_job=user_job, position_job=user_job_position, salary_job=user_job_salary, owner=user)
                    job.save()
    
                    document = Document(type_document=user_document, number_document=user_document_number, owner=user)
                    document.save()
    
                    return JsonResponse({"message": f"Usuário {user_name} criado com sucesso!", "status": "created"})
        else:
            return JsonResponse({"message": "Preencha campos de Login, senha e confirmação da senha", "status": "ok"})

            ## quando salva user sem passar um animal, tabela animal da BO