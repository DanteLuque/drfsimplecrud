from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # traer todos los registros
    permission_classes = [permissions.AllowAny] # AllowAny (cualquiera puede consultar), puede aplicarse autenticacion 
    serializer_class = ProjectSerializer