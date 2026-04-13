import uuid
from django.db import models

class Patient(models.Model):
    # Usamos UUID para que los IDs no sean predecibles (Seguridad)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Datos sensibles (PII)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    
    # Campo para auditoría (Requisito HIPAA/GDPR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Para saber quién creó el registro (Compliance)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.id}"