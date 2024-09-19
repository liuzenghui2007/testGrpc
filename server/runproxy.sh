#!/bin/bash

# Start the gRPC server
python3 server.py &

# Wait for the server to start
sleep 2

# Start grpcwebproxy
./grpcwebproxy-v0.15.0-linux-x86_64 \
    --backend_addr=localhost:50051 \
    --backend_tls_noverify \
    --server_http_debug_port=5001 \
    --run_tls_server=false \
    --allow_all_origins \
    --server_http_max_read_timeout=1h \
    --server_http_max_write_timeout=1h