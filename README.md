# Quote API: CI/CD Pipeline and Kubernetes Deployment

A small Flask REST API used to demonstrate a full DevOps pipeline: **code → build → deploy → scale**.

Built for the DevOps course (25CIAEC59 / 25CYAEC59).

## Tech stack

Python, Flask, pytest, Git/GitHub, Jenkins, Docker, Ansible, Kubernetes

## API endpoints

| Endpoint | Description |
|---|---|
| `GET /quote` | Returns a random quote |
| `GET /health` | Returns `{"status": "ok"}` |
| `GET /hello` | Returns a greeting message |

## Project structure

```
quote-api/
├── app.py               # Flask application
├── test_app.py          # pytest unit tests
├── requirements.txt     # Python dependencies
├── Jenkinsfile          # Jenkins CI pipeline
├── Dockerfile           # Multi-stage Docker build
├── deployment.yaml      # Kubernetes Deployment (3 replicas, probes)
├── service.yaml         # Kubernetes Service (NodePort 30080)
├── ansible/
│   ├── inventory
│   ├── playbook.yml
│   └── roles/quote_app/ # Role with tasks, handler, variables, template
└── repo_link.txt
```

## Run locally

```
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000/quote

Run the tests:

```
python -m pytest
```

## Component 1: CI with Git and Jenkins

- Work is done on feature branches and merged into `main` through pull requests.
- A Jenkins pipeline polls the repository every minute and starts a build automatically.
- Pipeline stages: **Checkout → Install → Test → Package**.
- Tests (3 pytest tests) run before packaging.
- The artifact is versioned with the build number, for example `quote-api-5.tar.gz`, and archived by Jenkins.

## Component 2: Ansible, Docker and Kubernetes

### Ansible

The `quote_app` role installs Python, copies the app, installs dependencies in a virtualenv, and runs the app as a systemd service. It uses a variable (`app_port`) and a handler that restarts the service only when something changed.

```
cd ansible
sudo ansible-playbook -i inventory playbook.yml -e ansible_become=false
curl localhost:5001/quote
```

### Docker

```
docker build -t quote-api:1.0 .
docker run -d --name quote-test -p 5000:5000 quote-api:1.0
```

The Dockerfile is multi-stage: a build stage installs dependencies and a slim runtime stage runs the app with gunicorn.

### Kubernetes

```
kubectl apply -f deployment.yaml -f service.yaml
kubectl get pods
kubectl get svc
```

Open http://localhost:30080/quote

Scale up and down:

```
kubectl scale deployment quote-api --replicas=5
kubectl scale deployment quote-api --replicas=3
```

## Enhancements

- **CI:** automated tests in the Jenkins pipeline and build-number versioning of artifacts.
- **Deployment:** liveness and readiness probes on `/health`, and a multi-stage Dockerfile.

## Environment used

Windows 11, Docker Desktop (Kubernetes v1.36.1, kubeadm single node), Ubuntu on WSL2 with Ansible core 2.20.1, Jenkins LTS in Docker.

## Author

Rupesh Holkar
