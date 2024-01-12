#!/bin/bash

image_name="chat"
container_name="chat"
port_host=3000
port_guest=8080

docker build -t "$image_name" .
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p 127.0.0.1:"$port_host":"$port_guest" \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    "$image_name"

docker image prune -f
