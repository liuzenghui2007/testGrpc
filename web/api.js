// 导入 RandomizerServiceClient
import { RandomizerServiceClient } from "./client/es6/client/randomizer_pb_service.js";

// 创建服务客户端实例
const serviceHost = "http://localhost:5005"; // 请根据实际情况调整服务地址
const client = new RandomizerServiceClient(serviceHost);

// 定义异步函数，用于获取随机字符串
const getOne = async () => {
  // 创建请求对象
  const req = new proto.randomizer.Empty();
  console.log("req", req);

  // 调用 gRPC 服务，并等待响应
  const response = client.getRandomString(req, {}, function (err, response) {
    if (err) {
      console.log(err.code);
      console.log(err.message);
    } else {
      console.log(response.toObject());
    }
  });
};

// 导出函数
export { getOne };
