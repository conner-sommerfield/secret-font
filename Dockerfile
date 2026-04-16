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
COPY --from=backend /app/assets ./public

RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# ------------------------
# 3. Frontend Prod
# ------------------------

FROM node:20 AS frontend-prod

WORKDIR /app
COPY frontend .
RUN npm install && npm run build

FROM nginx:alpine
COPY --from=frontend-prod /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]