#!/bin/bash

# 启动 grpcwebproxy
# --backend_addr 指定后端 gRPC 服务器的地址和端口
# --run_tls_server=false 表示不启用 TLS，如果您的环境需要 TLS，需要额外配置
# --allow_all_origins=true 允许所有来源的请求，出于安全考虑，生产环境应该指定具体的来源
# --server_http_max_read_timeout 和 --server_http_max_write_timeout 可以根据需要调整超时设置

#!/bin/bash

# 检测操作系统类型
if [[ "$OSTYPE" == "darwin"* ]]; then
  # 如果是 macOS，使用 grpcwebproxy-v0.15.0-osx-x86_64
  GRPCWEBPROXY="./grpcwebproxy-v0.15.0-osx-x86_64"
  CERT_FILE="$HOME/testGrpc/ssl/service.pem"
  KEY_FILE="$HOME/testGrpc/ssl/service.key"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # 如果是 Ubuntu，使用相应的 grpcwebproxy
  GRPCWEBPROXY="./grpcwebproxy"  # 假设在当前目录下有 grpcwebproxy 可执行文件
  CERT_FILE="$HOME/polyseq/testGrpc/ssl/service.pem"
  KEY_FILE="$HOME/polyseq/testGrpc/ssl/service.key"
else
  echo "Unsupported operating system."
  exit 1
fi

# 启动后端 gRPC 服务器
python server3.py &

# 启动 grpcwebproxy
"$GRPCWEBPROXY" \
  --server_tls_cert_file="$CERT_FILE" \
  --server_tls_key_file="$KEY_FILE" \
  --backend_addr=127.0.0.1:50051 \
  --backend_tls_noverify \
  --backend_tls=true \
  --server_bind_address=0.0.0.0 \
  --server_http_tls_port=5005 \
  --run_http_server=false \
  --server_tls_client_cert_verification=none \
  --server_http_max_write_timeout=0 \
  --server_http_max_read_timeout=0 \
  --use_websockets \
  --allow_all_origins