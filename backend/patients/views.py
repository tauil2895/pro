from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    # Solo usuarios autenticados pueden acceder (Seguridad mínima requerida)
    permission_classes = [permissions.IsAuthenticated]

    # Ejemplo de filtro profesional: un usuario solo ve lo que él creó (Data Privacy)
    def get_queryset(self):
        user = self.request.user
        if user.is_staff: # El staff puede ver todo
            return Patient.objects.all()
        return Patient.objects.filter(created_by=user)