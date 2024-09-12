#!/bin/bash

# 创建编译输出目录
mkdir -p ./compiled_proto

# 使用 gRPC 工具编译 Protocol Buffers 文件
python -m grpc_tools.protoc \
    -I../proto \
    --python_out=./compiled_proto \
    --grpc_python_out=./compiled_proto \
    ../proto/*.proto

# 详细说明：
# 1. python -m grpc_tools.protoc: 调用 Python 的 gRPC 工具来编译 .proto 文件
# 2. -I../proto: 指定 .proto 文件的搜索路径为上级目录的 proto 文件夹
# 3. --python_out=./compiled_proto: 生成的 Python 消息类代码输出到 ./compiled_proto 目录
# 4. --grpc_python_out=./compiled_proto: 生成的 gRPC Python 服务类代码输出到 ./compiled_proto 目录
# 5. ../proto/*.proto: 编译 ../proto 目录下的所有 .proto 文件

# 注意事项：
# - 确保已安装 grpcio-tools（可通过 pip install grpcio-tools 安装）
# - 每个 .proto 文件会生成两个 Python 文件：
#   * _pb2.py: 包含消息类型定义
#   * _pb2_grpc.py: 包含服务类型定义
# - 编译后的文件将直接保存在 ./compiled_proto 目录中，不会创建额外的子目录