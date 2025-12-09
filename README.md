# 🔗 QR Code Generator – DevOps Demo

A containerized web application that transforms URLs into QR codes. Built with FastAPI and modern DevOps practices, this project demonstrates microservices architecture, Docker containerization, and container orchestration with Docker Compose.

**Key Features:** 
- ⚡ Fast, lightweight backend API
- 🎨 Responsive frontend UI
- 🐳 Full containerization with Docker
- 🚀 Easy local deployment with Docker Compose

---

## 📋 Architecture

### 🔧 Backend
- **Language:** Python (FastAPI)
- **Port:** 8000
- **Endpoint:** `POST /qr`
- **Request:** JSON body `{"url": "<some URL>"}`
- **Response:** PNG image (binary)

**Implementation:**
- Generates QR codes in-memory using the `qrcode` library
- Serves responses with `image/png` MIME type
- CORS middleware configured for frontend cross-origin requests
- Fast, lightweight, and production-ready

### 🎭 Frontend
- **Port:** 3000
- **Server:** nginx (Alpine Linux)
- **Technology:** Vanilla HTML/CSS/JavaScript (no frameworks)

**Features:**
- Single-page interface with responsive design
- User input field for URL submission
- "Generate QR" button to trigger QR code generation
- Real-time QR code display with image preview
- Client-side blob URL conversion for instant rendering

### 🐳 Containerization & Orchestration

**Backend Container:**
- Base image: `python:3.11-slim` (lightweight, security-focused)
- Installs dependencies from `requirements.txt` via pip
- Runs: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Exposes port 8000 internally

**Frontend Container:**
- Base image: `nginx:alpine` (minimal, fast)
- Copies `index.html` to `/usr/share/nginx/html`
- Default nginx configuration for static file serving
- Exposes port 3000 internally

**Docker Compose Orchestration:**
- Defines both services with shared networking
- Maps ports to host machine (8000 → backend, 3000 → frontend)
- Builds images from local Dockerfiles
- Enables service-to-service communication via service names

## 📦 Prerequisites

- ✅ Docker and Docker Compose installed
- ⚙️ (Optional) Python and virtual environment for local backend development

---

## 🚀 Quick Start

### Running with Docker Compose

From the project root (`qr-app/`):

```bash
docker compose up --build
```

This command will:
- Build backend from `./backend`
- Build frontend from `./frontend`
- Start containers with mappings:
  - **Backend:** `http://localhost:8000`
  - **Frontend:** `http://localhost:3000`

### Using the Application

1. Open browser to: **http://localhost:3000**
2. Enter any URL (e.g., `https://example.com`)
3. Click **Generate QR**
4. View the generated QR code

### Stopping the Application

Press `Ctrl + C` in the Docker Compose terminal, then run:

```bash
docker compose down
```

This stops and removes containers.

---

## 📂 Project Structure

```
qr-app/
├─ backend/
│  ├─ main.py              # FastAPI app with /qr endpoint
│  ├─ requirements.txt     # Python dependencies
│  └─ Dockerfile           # Backend container definition
├─ frontend/
│  ├─ index.html           # Static HTML + JS frontend
│  └─ Dockerfile           # Frontend (nginx) container definition
└─ docker-compose.yml      # Service orchestration & configuration
```

---

## 📝 License

This project is provided as-is for educational and DevOps demonstration purposes.
