from django.shortcuts import get_object_or_404
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(http_method_names=["GET", "PATCH"])
def agendamento_detalhes(request, id):
    if request.method == "GET":
        agendamento = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(agendamento)
        return JsonResponse(serializer.data)
    
    if request.method == "PATCH":
        agendamento = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            agendamento.data_horario = validated_data.get("data_horario", agendamento.data_horario)
            agendamento.nome_cliente = validated_data.get("nome_cliente",agendamento.nome_cliente)
            agendamento.email_cliente = validated_data.get("email_cliente", agendamento.email_cliente)
            agendamento.telefone_cliente = validated_data.get("telefone_cliente", agendamento.telefone_cliente)
            agendamento.save()
            return JsonResponse(validated_data, status=200)
        return JsonResponse(serializer.erros, status=400)


@api_view(http_method_names=["GET", "POST"])
def agendamento_lista(request):
    if request.method == "GET":
        #qs = Agendamento.objects.all()
        qs = Agendamento.objects.filter().exclude(cancelado=True)
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

@api_view(http_method_names=["DELETE"])
def agendamento_deletar(request, id):
    if request.method == "DELETE":
        agendamento = get_object_or_404(Agendamento, id=id)
        agendamento.delete()
        return Response(status=204)

@api_view(http_method_names=["PATCH"])
def agendamento_cancelar(request, id):
    if request.method == "PATCH":
        agendamento = get_object_or_404(Agendamento, id=id)
        agendamento.cancelado = True
        agendamento.save()
    return Response(status=204)
    