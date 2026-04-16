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
RUN generate-font
RUN generate-glyphs

# ------------------------
# 2. Frontend Dev
# ------------------------

FROM node:20 AS frontend-dev

WORKDIR /app/frontend

COPY frontend .

RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# ------------------------
# 3. Frontend Prod
# ------------------------

FROM node:20 AS frontend-prod

WORKDIR /app/frontend

COPY frontend .
COPY --from=backend /app/assets ./public

RUN npm install
RUN npm run build

RUN npm install -g serve

CMD ["serve", "-s", "dist", "-l", "5173"]