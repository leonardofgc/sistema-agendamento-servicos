from django.urls import path
from agenda.views import agendamento_detalhes, agendamento_lista, agendamento_deletar, agendamento_cancelar

urlpatterns = [
    path('agendamentos/', agendamento_lista),
    path('agendamentos/<int:id>', agendamento_detalhes),
    path('agendamento/delete/<int:id>', agendamento_deletar),
    path('agendamento/cancelar/<int:id>', agendamento_cancelar)
]
