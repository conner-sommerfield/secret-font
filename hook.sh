#!/bin/bash
set -e

echo "Deploy triggered..."

HOME_DIR="/home/ubuntu"
APP_DIR="$HOME_DIR/secret-font"
REPO="$HOME_DIR/secret-font.git"

mkdir -p "$APP_DIR"

GIT_DIR="$REPO" \
GIT_WORK_TREE="$APP_DIR" \
git checkout -f main

cd "$APP_DIR"

echo "Building and starting containers..."

bash setup.sh prod

echo "✅ Deploy complete"