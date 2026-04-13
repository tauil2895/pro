from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    # Solo mostramos campos necesarios para evitar exposición innecesaria
    list_display = ('id', 'full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('id', 'created_at', 'updated_at')