#!/bin/bash

# Start the gRPC server
python3 server/server.py &

# Wait for the server to start
sleep 2

# Start grpcwebproxy
grpcwebproxy \
    --backend_addr=localhost:50051 \
    --backend_tls_noverify \
    --server_http_debug_port=5001 \
    --run_tls_server=false \
    --allow_all_origins
