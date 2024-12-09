from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app_create_account.models import User, Horta, HortaNutriente
from django.db.models import Count

# Create your views here.

def welcome(request):
    if request.method == "GET":
         # Obter o ID do usuário a partir do sessionStorage (passado pelo frontend)
        owner_id = request.session.get('user_name')
        hortas = []  # Inicializar variável para evitar erro se `owner_id` não for encontrado
        species_totals = {}  # Inicializar o dicionário
        if owner_id:
            try:
                owner = User.objects.get(name_user=owner_id)
                hortas = Horta.objects.filter(owner=owner)  # Filtrar animais do usuário

                # Contar os animais por espécie
                species_counts = hortas.values('specie_horta').annotate(total=Count('id'))
                species_totals = {entry['specie_horta']: entry['total'] for entry in species_counts}
            except User.DoesNotExist:
                return JsonResponse({'error': 'Usuario nao encontrado.'}, status=404)
        return render(request, 'welcome_screen.html', {'hortas': hortas, 'species_totals': species_totals})
    
    elif request.method == "POST":
        # Mapeamento fixo de nutrientes
        ANIMAL_FOOD_MAP = {
            'boi': ['Capim', 'Silagem'],
            'vaca': ['Capim', 'Ração'],
            'cavalo': ['Feno', 'Aveia'],
            'porco': ['Milho', 'Farelo de Soja'],
            'galinha': ['Milho', 'Farelo de Trigo'],
            'peixe': ['Alga', 'Larvas'],
        }
        # Receber os dados do front-end
        specie_horta = request.POST.get('horta')
        color_horta = request.POST.get('color')
        owner_id = request.POST.get('owner')  # ID do usuário que será o dono

        # Validar dados obrigatórios
        if not specie_horta or not color_horta or not owner_id:
            return JsonResponse({'error': 'Dados incompletos.'}, status=400)

        try:
            # Obter o usuário
            owner = User.objects.get(name_user=owner_id)
            owner.save()

            # Contar o número de animais já cadastrados para o usuário
            horta_count = Horta.objects.filter(owner=owner).count()

            # Criar o horta
            horta = Horta.objects.create(
                specie_horta=specie_horta,
                color_horta=color_horta,
                owner=owner
            )
            horta.save()

            # Associar nutrientes ao horta criado
            food_list = ANIMAL_FOOD_MAP.get(specie_horta.lower(), [])
            for food in food_list:
                horta_food = HortaNutriente(horta=horta, food_name=food)
                horta_food.save()  # Salvando cada alimento no banco

            # Resposta com ID do horta e nutrientes
            response_data = {
                'message': 'Horta e nutrientes adicionados com sucesso!',
                'new_horta_id': horta_count+1,
                'food_list': food_list,  # Passar os nutrientes para o frontend
            }

            return JsonResponse(response_data, status=201)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método não permitido.'}, status=405)
    
