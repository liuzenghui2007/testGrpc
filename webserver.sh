#!/bin/bash

# 启动 grpcwebproxy
# --backend_addr 指定后端 gRPC 服务器的地址和端口
# --run_tls_server=false 表示不启用 TLS，如果您的环境需要 TLS，需要额外配置
# --allow_all_origins=true 允许所有来源的请求，出于安全考虑，生产环境应该指定具体的来源
# --server_http_max_read_timeout 和 --server_http_max_write_timeout 可以根据需要调整超时设置
python server.py &

# ./grpcwebproxy \
./grpcwebproxy-v0.15.0-osx-x86_64 \
  --allow_all_origins \
  --backend_addr=localhost:50051 \
  --server_http_debug_port=5005 \
  --server_tls_cert_file=server.crt \
  --server_tls_key_file=server.key \
  --backend_tls \
  --server_http_max_read_timeout=1h \
  --server_http_max_write_timeout=1h