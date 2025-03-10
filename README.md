# assignment-1
# CS & CC

# Distributed System Using Docker and Kubernetes

## Project Overview
This project is a distributed system that includes:
- *Frontend:* A simple HTML/CSS/JavaScript application.
- *Backend:* A Flask-based REST API.
- *Database:* A PostgreSQL database.
- *Containerization:* All services are Dockerized.
- *Orchestration:* Deployed using Kubernetes with Minikube.
- *Monitoring:* Integrated with Prometheus and Grafana.

## Tech Stack
- *Frontend:* HTML, CSS, JavaScript, Nginx
- *Backend:* Python (Flask)
- *Database:* PostgreSQL
- *Containerization:* Docker, Docker Compose
- *Orchestration:* Kubernetes (Minikube)
- *Monitoring:* Prometheus, Grafana
## Features
- Users can submit their *name* and *email* via the frontend.
- The backend *validates and stores* the data in PostgreSQL.
- *Docker* ensures isolated environments.
- *Kubernetes* enables scalability and reliability.
- *Monitoring* allows tracking of system health.

## Project Setup & Execution

### *1. Clone the Repository*
sh
git clone https://github.com/dhruvi001/assignment-1.git
cd distributed-system

2. Run with Docker

docker-compose up --build

3. Run with Kubernetes
minikube start
kubectl apply -f k8s/

4. Open the Frontend

Access the frontend in the browser:

http://localhost:8080

5. API Testing

Use Postman or cURL to test:

curl -X POST http://backend-service:5000/api/data -H "Content-Type: application/json" -d '{"name": "Alice", "email": "alice@example.com"}'

Project Structure
Project Structure

distributed-system/
│── frontend/        # Frontend application (HTML, CSS, JavaScript)
│── backend/         # Backend API (Flask)
│── database/        # Database setup (PostgreSQL)
│── k8s/             # Kubernetes configuration
│── monitoring/      # Monitoring setup (Prometheus, Grafana)
│── docker-compose.yml # Docker Compose for local setup
│── README.md        # Project documentation
│── .gitignore       # Files to ignore in Git

Contributors

	•	[Your Name] - GitHub Profile
	•	Team Members (if applicable)

License

This project is licensed under the MIT License.

---
