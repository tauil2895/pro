# Management API 🏥 backend

This is a robust patient management system developed using **Django Rest Framework (DRF)** and orchestrated with **Docker**. The project is designed according to professional standards, including JWT security, access auditing (HIPAA compliance), and real-time monitoring.

## 🚀 Key Technologies
* **Backend:** Python 3.11+, Django 4.2, DRF.
* **Database:** PostgreSQL 15.
* **Autentication:** SimpleJWT (JSON Web Tokens).
* **Monitoring:** Prometheus & Grafana.
* **Infrastructure:** Docker & Docker Compose.

## 🛠️ Implemented Features
- **Secure Autentication:** Complete flow of `access` y `refresh` tokens.
- **Data Management:** CRUD completo con validación de datos y formatos de fecha regionales ($MM-DD-YYYY$).
- **HIPAA Audit:** Custom middleware that logs every access to sensitive data in `hipaa_audit.log`.
- **Observability:** Integrated metrics endpoint for performance telemetry.
- **Dockerized:** Identical development environment for all collaborators.

## 📦 Project Structure

/backend          # Django Application (Core and App Patients)
/prometheus       # Metrics Collector Configuration
docker-compose.yml # Service Orchestration (App, DB, Prom, Grafana)
.env              # Environment Variables (Not included in Git)

⚙️ Installation and Configuration
Clone the repository:
git clone https://github.com/tauil2895/pro.git
cd pro

Configure environment variables:
Create a .env file in the /backend folder with:

# .env file content
DEBUG=True
SECRET_KEY=tu_llave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1,backend
DATABASE_URL=postgres://app_user:password123@db:5432/app_db

Run the stack with Docker:
docker-compose up -d --build

📊 Monitoring and Access
API: http://localhost:8000/api/patients/
Metrics (Prometheus): http://localhost:9070
Dashboards (Grafana): http://localhost:3100 (User: admin / Pass: admin)

Note: Import Dashboard ID 9528 to view Django statistics.

🔒 Security and Auditing
The system automatically generates an audit file in the backend's root directory. Every request to the patient API is logged—including the user, HTTP method, and status code—thereby meeting basic medical traceability requirements.

Developed by Alí Almeida Tauil - 2026.
