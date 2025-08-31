#!/bin/bash

# Start VaniPost Frontend

echo "🚀 Starting VaniPost Frontend..."

# Check if we're in the frontend directory
if [ ! -f "package.json" ]; then
    if [ -d "frontend" ]; then
        cd frontend
    else
        echo "❌ Frontend directory not found. Run from project root or frontend directory."
        exit 1
    fi
fi

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start the development server
echo "🌐 Starting development server..."
npm run dev