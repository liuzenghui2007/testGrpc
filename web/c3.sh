# https://www.npmjs.com/package/ts-protoc-gen

# sudo snap install protobuf --classic
# yarn add ts-protoc-gen
# 
rm -rf ./client/*
# Path to this plugin, Note this must be an absolute path on Windows (see #15)
PROTOC_GEN_TS_PATH="./node_modules/.bin/protoc-gen-ts"

# Directory to write generated code to (.js and .d.ts files)
OUT_DIR="./client"

protoc \
  --plugin=protoc-gen-ts=${PROTOC_GEN_TS_PATH} \
  --ts_out=service=grpc-web:${OUT_DIR} \
  **.proto

# npx babel ${OUT_DIR} --out-dir es6
