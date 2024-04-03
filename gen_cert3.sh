
certstrap=/home/zenghui/Downloads/certstrap-linux-amd64
$certstrap init --cn "MyCA"
$certstrap request-cert --cn "localhost" --domain "localhost"
$certstrap sign --CA "MyCA" localhost