# https://blog.csdn.net/wan212000/article/details/120762210
# chmod +x /home/zenghui/Downloads/certstrap-linux-amd64
# 设置certstrap命令的完整路径
certstrap=/home/zenghui/Downloads/certstrap-linux-amd64

# 初始化一个新的CA（证书颁发机构），使用"ExampleCA"作为通用名称，设置证书有效期为20年
$certstrap init --common-name "ExampleCA" --expires "20 years"

# 为服务器请求一个新的证书，指定通用名称为server，IP地址为127.0.0.1，并设置域名为"hello.com"
$certstrap request-cert -cn server -ip 127.0.0.1 -domain "localhost"

# 使用"ExampleCA" CA签署名为server的证书
$certstrap sign server --CA ExampleCA

# 为客户端请求一个新的证书，指定通用名称为client
$certstrap request-cert -cn client

# 使用"ExampleCA" CA签署名为client的证书
$certstrap sign client --CA ExampleCA