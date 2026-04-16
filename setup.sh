#!/usr/bin/env bash
set -e

echo " Starting secret-font project..."

# ----------------------------
# Check Docker
# ----------------------------
if ! command -v docker &> /dev/null; then
  echo "❌ Docker is not installed."

  echo ""
  echo "  Install Docker first:"
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
  echo "Start Docker Desktop or run: sudo systemctl start docker"
  exit 1
fi

# ----------------------------
# Commands
# ----------------------------
COMMAND=${1:-up}

case "$COMMAND" in

  # ----------------------------
  # DEV MODE
  # ----------------------------
  dev)
    echo "Starting DEV environment (Vite + backend)..."
    docker compose up --build
    ;;

  # ----------------------------
  # PROD
  # ----------------------------
  prod)
    echo "Starting PROD environment (built assets)..."

    # If you use compose overrides:
    if [ -f docker-compose.prod.yml ]; then
      docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build
    else
      echo "⚠️ No docker-compose.prod.yml found, falling back to normal compose"
      docker compose up --build
    fi
    ;;

  # ----------------------------
  # DEFAULT
  # ----------------------------
  up)
    echo "Starting project (default = dev)..."
    docker compose up --build
    ;;

  # ----------------------------
  # DEBUG BACKEND
  # ----------------------------
  debug)
    echo "Building backend debug image..."
    docker build --target backend -t backend-debug .

    echo "Opening backend shell..."
    docker run -it --entrypoint bash backend-debug
    ;;

  # ----------------------------
  # BUILD ONLY
  # ----------------------------
  build)
    echo "Building Docker images..."
    docker compose build
    ;;

  # ----------------------------
  # CLEAN
  # ----------------------------
  clean)
    echo "Cleaning containers and images..."
    docker compose down --volumes --remove-orphans
    docker system prune -f
    ;;

  # ----------------------------
  # HELP
  # ----------------------------
  *)
    echo "❌ Unknown command: $COMMAND"
    echo ""
    echo "Available commands:"
    echo "  dev    - run development environment (hot reload)"
    echo "  prod   - run production build"
    echo "  up     - same as dev"
    echo "  build  - build images only"
    echo "  debug  - backend shell"
    echo "  clean  - remove containers/volumes"
    exit 1
    ;;
esac