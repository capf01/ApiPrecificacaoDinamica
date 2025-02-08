from celery import shared_task
from .models import Tarefa
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def enviar_notificacao(tarefa_id):
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        assunto = f"Tarefa {tarefa.titulo} criada"
        mensagem = f"A tarefa '{tarefa.titulo}' foi criada com sucesso."
        send_mail(assunto, mensagem, 'seu_email@gmail.com', ['destinatario_email@gmail.com'])
    except Tarefa.DoesNotExist:
        pass  # Pode adicionar um log de erro aqui

@shared_task
def atualizar_tarefa(tarefa_id):
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.atualizado_em = datetime.now()
        tarefa.save()
        enviar_notificacao(tarefa_id)
    except Tarefa.DoesNotExist:
        pass  # Pode adicionar um log de erro aqui
