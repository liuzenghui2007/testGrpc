/opt/ont/minknow/bin/grpcwebproxy \
  --server_tls_cert_file=/opt/ont/minknow/conf/rpc-certs/localhost.crt \
  --server_tls_key_file=/opt/ont/minknow/conf/rpc-certs/localhost.key \
  --backend_addr=127.0.0.1:9501 \
  --backend_tls_noverify \
  --backend_tls=true \
  --server_bind_address=0.0.0.0 \
  --server_http_tls_port=9502 \
  --run_http_server=false \
  --server_tls_client_cert_verification=none \
  --server_http_max_write_timeout=0 \
  --server_http_max_read_timeout=0 \
  --use_websockets \
  --allow_all_origins