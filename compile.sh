#!/bin/bash

# 使用 gRPC 工具编译 Protocol Buffers 文件

# 参数说明：
# -I. : 指定 .proto 文件的搜索路径为当前目录
# --python_out=./server : 生成的 Python 代码输出到 ./server 目录
# --grpc_python_out=./server : 生成的 gRPC Python 代码输出到 ./server 目录
# ./protos/*.proto : 编译 ./protos 目录下的所有 .proto 文件

# 编译所有 .proto 文件
python -m grpc_tools.protoc \
    -I. \
    --python_out=./server \
    --grpc_python_out=./server \
    ./protos/*.proto

# 注意：
# 1. 此命令会编译 ./protos 目录下的所有 .proto 文件
# 2. 编译后的文件将保存在 ./server 目录中
# 3. 每个 .proto 文件都会生成两个对应的 Python 文件：
#    - *_pb2.py（消息类型）
#    - *_pb2_grpc.py（服务类型）
# 4. 确保 grpc_tools.protoc 已经安装（可以通过 pip install grpcio-tools 安装）
# 5. 如果 ./server 目录不存在，请先创建它