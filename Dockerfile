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

WORKDIR /app

COPY frontend .
COPY --from=backend /app/assets ./public

RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]

# ------------------------
# 3. Frontend Prod
# ------------------------

FROM node:20 AS frontend-prod

WORKDIR /app/frontend
COPY frontend .
COPY --from=backend /app/assets ./public
RUN npm install && npm run build

FROM nginx:alpine AS server
RUN apk add --no-cache apache2-utils
COPY --from=frontend-prod /app/frontend/dist /usr/share/nginx/html
RUN touch /etc/nginx/.htpasswd

COPY /etc/secret-font/zix_pass.txt /run/zix_pass.txt
COPY /etc/secret-font/cat_pass.txt /run/cat_pass.txt

RUN htpasswd -bc /etc/nginx/.htpasswd zix "$(cat /run/zix_pass.txt)" \
 && htpasswd -b /etc/nginx/.htpasswd cat "$(cat /run/cat_pass.txt)"

RUN cat > /etc/nginx/conf.d/default.conf <<'EOF'
server {
    listen 80;

    location / {
        auth_basic "Private Site";
        auth_basic_user_file /etc/nginx/.htpasswd;

        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }
}
EOF

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]