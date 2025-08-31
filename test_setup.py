#!/usr/bin/env python3
"""
Quick setup test for VaniPost development environment
"""

import asyncio
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))


async def test_imports():
    """Test that all imports work correctly"""
    try:
        print("🔍 Testing imports...")

        # Test FastAPI app
        from app.main import app

        print("✅ FastAPI app imports successfully")

        # Test database
        from app.db.database import engine, get_db

        print("✅ Database setup imports successfully")

        # Test models
        from app.models.post import Post

        print("✅ Post model imports successfully")

        # Test schemas
        from app.schemas.post import PostCreate, PostResponse

        print("✅ Pydantic schemas import successfully")

        # Test API endpoints
        from app.api.v1.endpoints.health import router as health_router
        from app.api.v1.endpoints.posts import router as posts_router

        print("✅ API endpoints import successfully")

        print("\n🎉 All backend imports successful!")
        return True

    except Exception as e:
        print(f"❌ Import error: {e}")
        return False


def test_frontend():
    """Test frontend setup"""
    frontend_path = Path(__file__).parent / "frontend"

    if not frontend_path.exists():
        print("❌ Frontend directory not found")
        return False

    package_json = frontend_path / "package.json"
    if not package_json.exists():
        print("❌ Frontend package.json not found")
        return False

    node_modules = frontend_path / "node_modules"
    if not node_modules.exists():
        print("⚠️  Frontend dependencies not installed (run: cd frontend && npm install)")
        return False

    print("✅ Frontend setup looks good")
    return True


def test_docker():
    """Test Docker setup"""
    docker_compose = Path(__file__).parent / "docker-compose.yml"
    if not docker_compose.exists():
        print("❌ docker-compose.yml not found")
        return False

    print("✅ Docker Compose configuration found")
    return True


def test_scripts():
    """Test development scripts"""
    scripts_dir = Path(__file__).parent / "scripts"
    if not scripts_dir.exists():
        print("❌ Scripts directory not found")
        return False

    required_scripts = ["dev.sh", "start-backend.sh", "start-frontend.sh"]
    for script in required_scripts:
        script_path = scripts_dir / script
        if not script_path.exists():
            print(f"❌ Script {script} not found")
            return False
        if not script_path.is_file() or not script_path.stat().st_mode & 0o111:
            print(f"⚠️  Script {script} is not executable")

    print("✅ Development scripts found")
    return True


async def main():
    """Run all tests"""
    print("🚀 VaniPost Development Environment Test\n")

    tests = [
        ("Backend Imports", test_imports()),
        ("Frontend Setup", test_frontend()),
        ("Docker Configuration", test_docker()),
        ("Development Scripts", test_scripts()),
    ]

    results = []
    for name, test in tests:
        print(f"\n📋 Testing {name}...")
        if asyncio.iscoroutine(test):
            result = await test
        else:
            result = test
        results.append(result)

    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)

    all_passed = all(results)
    if all_passed:
        print("🎉 All tests passed! Your VaniPost environment is ready.")
        print("\n🚀 Next steps:")
        print("1. Copy .env.example to .env and configure your settings")
        print("2. Start services: ./scripts/dev.sh")
        print("3. Run backend: ./scripts/start-backend.sh")
        print("4. Run frontend: ./scripts/start-frontend.sh")
    else:
        print("❌ Some tests failed. Please check the output above.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
