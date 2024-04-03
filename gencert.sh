openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt

# 检查证书和私钥是否匹配
openssl x509 -noout -modulus -in server.crt | openssl md5
openssl rsa -noout -modulus -in server.key | openssl md5