我在学习grpc-web，首先请帮我实现一个proto，实现一个unary接口和stream接口，unary接口每次返回一个随机📄，stream接口持续返回随机uuid流

请帮我用python脚本实现这个proto作为server



pip install grpcio grpcio-tools

brew install protobuf
protoc --versioin

cnpm i google-protobuf @types/google-protobuf @improbable-eng/grpc-web --save
cnpm i ts-protoc-gen
bash compile.sh


RandomizerClient.js:1 Uncaught SyntaxError: Cannot use import statement outside a module 

安装Live server
该插件安装完成后，在index.html页面右键选择Open with Live Server