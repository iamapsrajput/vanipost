#!/bin/bash

# VaniPost Development Setup Script

echo "🚀 Starting VaniPost development environment..."

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Start services with Docker Compose
echo "📦 Starting services with Docker Compose..."
docker-compose up -d postgres redis

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Check if we're in a virtual environment or have poetry
if command -v poetry &> /dev/null; then
    echo "📚 Using Poetry for backend dependencies..."
    cd backend && poetry install && cd ..
elif [ -n "$VIRTUAL_ENV" ]; then
    echo "🐍 Using pip in virtual environment..."
    pip install -r backend/requirements.txt 2>/dev/null || echo "No requirements.txt found, using poetry..."
else
    echo "⚠️  No virtual environment detected. Consider using poetry or creating a venv."
fi

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
cd frontend && npm install && cd ..

echo "✅ Development environment setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Start the backend: cd backend && poetry run uvicorn app.main:app --reload"
echo "2. Start the frontend: cd frontend && npm run dev"
echo "3. Or use Docker: docker-compose up backend frontend"
echo ""
echo "🌐 URLs:"
echo "- Frontend: http://localhost:3000"
echo "- Backend API: http://localhost:8000"
echo "- API Docs: http://localhost:8000/docs"