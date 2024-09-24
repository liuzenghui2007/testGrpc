#!/bin/bash

# Determine the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    GRPCWEBPROXY="./grpcwebproxy-v0.15.0-linux-x86_64"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    GRPCWEBPROXY="./grpcwebproxy-v0.15.0-osx-x86_64"
else
    echo "Unsupported operating system"
    exit 1
fi

# Check if the grpcwebproxy exists
if [ ! -f "$GRPCWEBPROXY" ]; then
    echo "grpcwebproxy not found: $GRPCWEBPROXY"
    exit 1
fi

# Ensure the grpcwebproxy is executable
chmod +x "$GRPCWEBPROXY"

# Start the Python server in the background
python3 server.py &

# Wait for the server to start (adjust the sleep time if needed)
sleep 2

# Start the grpcwebproxy
"$GRPCWEBPROXY" \
    --backend_addr=localhost:50051 \
    --run_tls_server=false \
    --allow_all_origins \
    --server_http_debug_port=5001

# Kill the Python server when the script exits
trap "kill $!" EXIT