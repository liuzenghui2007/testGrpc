// 导入必要的模块和服务客户端
import { RandomizerServiceClient } from "./client/es6/client/randomizer_pb_service.js";

// 创建服务客户端实例
const serviceHost = "http://localhost:5005"; // 请根据实际情况调整服务地址
const client = new RandomizerServiceClient(serviceHost);

// 修改后的调用 getRandomString API
function callGetRandomString() {
  return new Promise((resolve, reject) => {
    const request = new proto.randomizer.Empty();
    client.getRandomString(request, {}, (err, response) => {
      if (err) {
        console.error("Error calling getRandomString:", err);
        reject(err);
      } else {
        console.log("getRandomString response:", response);
        resolve(response);
      }
    });
  });
}

// 修改后的调用 getRandomUUIDStream API
function callGetRandomUUIDStream() {
  return new Promise((resolve, reject) => {
    const request = new proto.randomizer.Empty();
    const stream = client.getRandomUUIDStream(request, {});
    stream.on("data", (response) => {
      console.log("Received UUID from stream:", response);
      resolve(response); // 可能需要调整以处理多个值
    });
    stream.on("error", (err) => {
      console.error("Stream error:", err);
      reject(err);
    });
    // 注意：如果流可以发送多个值，可能需要其他逻辑来处理
  });
}

// 导出函数
export { callGetRandomString, callGetRandomUUIDStream };
