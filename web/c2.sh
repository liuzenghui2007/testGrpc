# https://www.npmjs.com/package/ts-protoc-gen
rm -rf ./client/*
# Path to this plugin, Note this must be an abolsute path on Windows (see #15)
PROTOC_GEN_TS_PATH="./node_modules/.bin/protoc-gen-ts"

# Directory to write generated code to (.js and .d.ts files)
OUT_DIR="./client"

protoc --plugin=./node_modules/.bin/protoc-gen-ts --ts_out=service=grpc-web:${OUT_DIR} **.proto