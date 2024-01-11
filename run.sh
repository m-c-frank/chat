#!/bin/bash

image_name="chat"
container_name="chat"
port=3000

docker build -t "$image_name" .
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$port":"$port" \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    "$image_name"

docker image prune -f
