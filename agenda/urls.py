from django.urls import path
from agenda.views import agendamento_detalhes, agendamento_lista

urlpatterns = [
    path('agendamentos/', agendamento_lista),
    path('agendamentos/<int:id>', agendamento_detalhes)
]
