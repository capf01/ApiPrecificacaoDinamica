from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaView(APIView):
    def get(self, request):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarefaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarefaDetailView(APIView):
    def get(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(tarefa)
            return Response(serializer.data)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            serializer = TarefaSerializer(tarefa, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            tarefa = Tarefa.objects.get(pk=pk)
            tarefa.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tarefa.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)