#!/usr/bin/env bash
set -e

echo "🚀 Starting secret-font project..."

# ----------------------------
# Check Docker
# ----------------------------
if ! command -v docker &> /dev/null; then
  echo "❌ Docker is not installed."

  echo ""
  echo "👉 Install Docker first:"
  echo "   macOS: https://www.docker.com/products/docker-desktop/"
  echo "   Ubuntu: sudo apt install docker.io docker-compose-plugin"
  echo ""

  exit 1
fi

# ----------------------------
# Check Docker daemon
# ----------------------------
if ! docker info &> /dev/null; then
  echo "❌ Docker is installed but not running."
  echo "👉 Start Docker Desktop or run: sudo systemctl start docker"
  exit 1
fi

# ----------------------------
# Commands
# ----------------------------
COMMAND=${1:-up}

case "$COMMAND" in
  up)
    echo "🏗️ Building and starting project (docker compose)..."
    docker compose up --build
    ;;

  dev)
    echo "🏗️ Starting dev environment..."
    docker compose up --build
    ;;

  debug)
    echo "🐞 Building backend debug image..."
    docker build --target backend -t backend-debug .

    echo "🐚 Opening backend shell..."
    docker run -it --entrypoint bash backend-debug
    ;;

  build)
    echo "🏗️ Building Docker images..."
    docker compose build
    ;;

  clean)
    echo "🧹 Cleaning containers and images..."
    docker compose down --volumes --remove-orphans
    docker system prune -f
    ;;

  *)
    echo "❌ Unknown command: $COMMAND"
    echo ""
    echo "Available commands:"
    echo "  up     - build + run full project"
    echo "  dev    - run dev environment"
    echo "  debug  - open backend shell"
    echo "  build  - build images only"
    echo "  clean  - remove containers/volumes"
    exit 1
    ;;
esac