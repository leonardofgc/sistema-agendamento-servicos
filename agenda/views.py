from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse

from rest_framework.decorators import api_view

# Create your views here.
@api_view(http_method_names=["GET"])
def agendamento_detalhes(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    serializer = AgendamentoSerializer(agendamento)
    return JsonResponse(serializer.data)


@api_view(http_method_names=["GET", "POST"])
def agendamento_lista(request):
    if request.method == "GET":
        qs = Agendamento.objects.all()
        serizalizer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serizalizer.data, safe=False)
    if request.method == "POST":
        data = request.data
        serizalizer = AgendamentoSerializer(data=data)
        if serizalizer.is_valid():
            validated_data = serizalizer.validated_data
            Agendamento.objects.create(
                data_horario = validated_data["data_horario"],
                nome_cliente = validated_data["nome_cliente"],
                email_cliente = validated_data["email_cliente"],
                telefone_cliente = validated_data["telefone_cliente"]
            )
            return JsonResponse(serizalizer.data, status=201)
        return JsonResponse(serizalizer.errors, status=400)
    