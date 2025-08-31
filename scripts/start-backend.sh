#!/bin/bash

# Start VaniPost Backend

echo "🚀 Starting VaniPost Backend..."

# Check if we're in the backend directory
if [ ! -f "app/main.py" ]; then
    if [ -d "backend" ]; then
        cd backend
    else
        echo "❌ Backend directory not found. Run from project root or backend directory."
        exit 1
    fi
fi

# Start with poetry if available, otherwise use uvicorn directly
if command -v poetry &> /dev/null; then
    echo "📚 Starting with Poetry..."
    poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
else
    echo "🐍 Starting with uvicorn..."
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
fi