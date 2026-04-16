# ------------------------
# 1. Backend
# ------------------------
FROM ubuntu:22.04 AS backend

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    fontforge \
    python3-fontforge \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -c "import fontforge"

WORKDIR /app

COPY backend ./backend
COPY pyproject.toml .

RUN mkdir -p /app/assets

RUN python3 -m pip install --upgrade pip setuptools wheel

RUN pip install .

# Run font generator
# RUN python3 -m backend.main
# RUN python3 -m backend.glyphs.cli

# ------------------------
# 2. Frontend
# ------------------------
FROM node:20 AS frontend

WORKDIR /app

COPY frontend ./frontend

COPY --from=backend /app/backend/assets ./frontend/public

WORKDIR /app/frontend

RUN npm install
RUN npm run build