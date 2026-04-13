import logging

logger = logging.getLogger('security_audit')

class HIPAAAuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Solo registramos accesos a la API de pacientes y que sean exitosos
        if 'api/patients' in request.path and request.user.is_authenticated:
            user = request.user.username
            method = request.method
            path = request.path
            status = response.status_code
            
            # Log profesional para auditoría
            logger.info(f"AUDIT_LOG | User: {user} | Action: {method} | Resource: {path} | Status: {status}")

        return response