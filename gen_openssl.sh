# server.key：用于签名和验证公钥的 RSA 私钥
# server.pem/ server.crt：用于分发的自签名X.509公钥
# rootca.crt：用于签署 .csr 文件的证书颁发机构公钥
# host.csr：访问 CA 的证书签名请求


# 生成 2048 位 RSA 密钥
openssl genrsa -out server.key 2048

# 生成自签名证书
openssl req -new -x509 -sha256 -key server.key -out server.crt -days 3650

# 生成证书签名请求
openssl req -new -sha256 -key server.key -out server.csr

# 使用CA签名证书
openssl x509 -req -sha256 -in server.csr -signkey server.key -out server.crt -days 3650