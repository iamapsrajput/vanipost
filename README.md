# VaniPost

VaniPost is a social media automation platform that helps you create, schedule,
and manage posts across multiple social media platforms.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- Poetry (recommended) or pip

### Development Setup

1. **Clone and setup the project:**

   ```bash
   git clone <repository-url>
   cd vanipost
   ```

2. **Run the setup script:**

   ```bash
   ./scripts/dev.sh
   ```

3. **Start the services:**

   **Option A: Using scripts**

   ```bash
   # Terminal 1 - Backend
   ./scripts/start-backend.sh

   # Terminal 2 - Frontend
   ./scripts/start-frontend.sh
   ```

   **Option B: Using Docker Compose**

   ```bash
   docker-compose up
   ```

4. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🏗️ Architecture

### Backend (FastAPI)

- **Framework:** FastAPI with async/await
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Cache:** Redis for session management
- **API:** RESTful API with automatic OpenAPI docs

### Frontend (React + TypeScript)

- **Framework:** React 18 with TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **State Management:** React hooks

### Infrastructure

- **Containerization:** Docker & Docker Compose
- **Database:** PostgreSQL 15
- **Cache:** Redis 7
- **Development:** Hot reload for both frontend and backend

## 📁 Project Structure

```
vanipost/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API routes
│   │   ├── core/           # Configuration
│   │   ├── db/             # Database setup
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── main.py         # FastAPI app
│   └── Dockerfile
├── frontend/               # React frontend
│   ├── src/
│   │   ├── App.tsx         # Main component
│   │   └── index.css       # Tailwind styles
│   ├── package.json
│   └── Dockerfile
├── scripts/                # Development scripts
├── docker-compose.yml      # Docker services
└── README.md
```

## 🔧 Development

### Backend Development

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

### Database Migrations

```bash
# TODO: Add Alembic migrations
```

## 🧪 Testing

```bash
# Backend tests
cd backend
poetry run pytest

# Frontend tests
cd frontend
npm run test
```

## 📝 API Endpoints

- `GET /health` - Health check
- `GET /api/v1/health/detailed` - Detailed health with DB status
- `GET /api/v1/posts/` - List posts
- `POST /api/v1/posts/` - Create post
- `GET /api/v1/posts/{id}` - Get post by ID
- `PUT /api/v1/posts/{id}` - Update post
- `DELETE /api/v1/posts/{id}` - Delete post

## 🌟 Features

- ✅ FastAPI backend with async support
- ✅ React frontend with TypeScript
- ✅ PostgreSQL database with SQLAlchemy
- ✅ Redis caching
- ✅ Docker containerization
- ✅ Hot reload development
- ✅ API documentation
- ✅ CORS configuration
- 🚧 Post scheduling (coming soon)
- 🚧 Multi-platform posting (coming soon)
- 🚧 User authentication (coming soon)
