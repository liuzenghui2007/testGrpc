// 导入必要的模块和服务客户端
import { RandomizerServiceClient } from "./client/es6/client/randomizer_pb_service.js";

// 创建服务客户端实例
const serviceHost = "http://localhost:5005"; // 请根据实际情况调整服务地址
const client = new RandomizerServiceClient(serviceHost);

const oneCallback = (data) => {
  console.log(data);
};
const getOne = () => {
  const req = new proto.randomizer.Empty();
  console.log("req", req);
  const res = client.getRandomString(req, oneCallback);
  console.log("getOne", res);
};

// 导出函数
export { getOne };
