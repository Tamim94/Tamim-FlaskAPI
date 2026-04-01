# Minimal DevSecOps Flask API
This will create a Deployment and a LoadBalancer Service exposing the API on port 80.
```
kubectl apply -f k8s.yaml
```bash
Apply the manifest file to your Kubernetes cluster:

## Deploying to Kubernetes

   ```
   docker run -d -p 5000:5000 --name devsecops-api flask-api:latest
   ```bash
2. Run the Docker container:
   ```
   docker build -t flask-api:latest .
   ```bash
1. Build the Docker image:

## Running with Docker

   ```
   python app.py
   ```bash
3. Run the application:
   ```
   pip install -r requirements.txt
   ```bash
2. Install dependencies:
   ```
   # Or on Windows: venv\Scripts\activate
   source venv/bin/activate
   python -m venv venv
   ```bash
1. Create a virtual environment and activate it:

## Running Locally

- `POST /api/v1/users` - Create a new user (requires JSON with `username` and `email`).
- `GET /api/v1/users/<id>` - Retrieve a specific user.
- `GET /api/v1/users` - Retrieve all users.
- `GET /health` - Liveness/Readiness probe endpoint.
## Endpoints

2. **Insecure Kubernetes Configuration**: The `k8s.yaml` deployment explicitly configures `runAsUser: 0` (running the container as root).
1. **Outdated Dependencies**: `requirements.txt` uses older versions of `Flask` and `Werkzeug` with known CVEs.
To provide actionable findings for your security scanners (e.g., Trivy, Snyk, Checkov, Conftest), this baseline intentionally includes:
## Intentional Security Flaws (For Practice)

This is a baseline repository designed for practicing the implementation of a DevSecOps CI/CD pipeline. It consists of a minimal Python Flask API with basic endpoints, along with Docker and Kubernetes configurations.


