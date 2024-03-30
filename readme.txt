我在学习grpc-web，首先请帮我实现一个proto，实现一个unary接口和stream接口，unary接口每次返回一个随机📄，stream接口持续返回随机uuid流

请帮我用python脚本实现这个proto作为server




brew install protobuf
protoc --versioin

protoc ../randomizer.proto --js_out=import_style=commonjs:./client --grpc-web_out=import_style=commonjs,mode=grpcwebtext:./client