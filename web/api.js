// 导入 RandomizerServiceClient
import { RandomizerServiceClient } from "./client/es6/client/randomizer_pb_service.js";

// 创建服务客户端实例
const serviceHost = "https://localhost:5005"; // 请根据实际情况调整服务地址
const client = new RandomizerServiceClient(serviceHost);

// 定义异步函数，用于获取随机字符串
const getOne = () => {
  const req = new proto.randomizer.Empty();
  return new Promise((resolve, reject) => {
    client.getRandomString(req, {}, (err, response) => {
      if (err) {
        reject(err);
      } else {
        resolve(response.toObject());
      }
    });
  });
};

// 定义函数，用于获取随机UUID流
const getStream = () => {
  const req = new proto.randomizer.Empty();
  const stream = client.getRandomUUIDStream(req, {});
  return stream; // 返回流对象，以便外部可以监听数据和结束事件
};

// 导出函数
export { getOne, getStream };
