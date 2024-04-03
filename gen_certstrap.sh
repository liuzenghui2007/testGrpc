
# https://www.5axxw.com/wiki/content/p9c11u

# 定义变量
CA_NAME="umd.fluidfs.com"
IP_ADDRESS="192.168.1.18"

# 初始化一个新的CA（证书颁发机构），使用变量中的通用名称
certstrap init --common-name "$CA_NAME"

# 为变量中的IP地址请求一个新的证书
certstrap request-cert -ip "$IP_ADDRESS"

# 使用变量中的CA签署变量中的IP地址的证书
certstrap sign "$IP_ADDRESS" --CA "$CA_NAME"