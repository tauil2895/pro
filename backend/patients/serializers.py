from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # Exponemos todos los campos, pero 'id' y fechas son de solo lectura por seguridad
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'created_by')
        # Definimos el campo explícitamente para cambiar el formato de entrada/salida
        date_of_birth = serializers.DateField(input_formats=['%m-%d-%Y', '%Y-%m-%d'])

    def create(self, validated_data):
        # Asignamos automáticamente el usuario que hace la petición (Auditoría HIPAA)
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)