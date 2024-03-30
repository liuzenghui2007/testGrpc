import { RandomizerServiceClient } from "./client/randomizer_pb_service.js";
// import { Empty } from "./client/randomizer_pb.js";

const client = new RandomizerServicePromiseClient(
  "http://localhost:8080",
  null,
  null
);

function getRandomString() {
  return client.getRandomString({}, {});
}

function getRandomUUIDStream() {
  const stream = client.getRandomUUIDStream({});
  stream.on("data", (response) => {
    console.log(response.getUuid());
  });
  stream.on("end", () => {
    console.log("Stream ended.");
  });
}

export { getRandomString, getRandomUUIDStream };
