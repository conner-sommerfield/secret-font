#!/usr/bin/env bash
set -e

echo " Starting secret-font project..."

# ------------------------
# 1. Check Docker
# ------------------------
if ! command -v docker &> /dev/null; then
  echo "Docker not found. Installing..."

  sudo apt-get update
  sudo apt-get install -y ca-certificates curl gnupg

  sudo install -m 0755 -d /etc/apt/keyrings

  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

  sudo chmod a+r /etc/apt/keyrings/docker.gpg

  echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

  sudo apt-get update

  sudo apt-get install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin

  echo "✅ Docker installed"
else
  echo "✅ Docker already installed"
fi

# ----------------------------
# Check Docker daemon
# ----------------------------
if ! docker info &> /dev/null; then
  echo "❌ Docker is installed but not running."
  echo "Start Docker Desktop or run: sudo systemctl start docker"
  echo "On Ubuntu you may have to run: sudo usermod -aG docker ubuntu and newgrp docker for permissions"
  echo "Get information with: docker info"
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

    SECRET=$(cat /etc/secret-font/secret.key)

    mkdir -p ./generated

    sed "s|SECRET_PLACEHOLDER|$SECRET|g" \
    nginx.conf.template > ./generated/nginx.conf

    # If you use compose overrides:
    if [ -f docker-compose.prod.yml ]; then
      docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
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