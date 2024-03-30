const {
  RandomizerServicePromiseClient,
} = require("./client/randomizer_pb_service");
const { Empty } = require("./client/randomizer_pb");

const client = new RandomizerServicePromiseClient(
  "http://localhost:8080",
  null,
  null
);

function getRandomString() {
  return client.getRandomString(new Empty(), {});
}

function getRandomUUIDStream() {
  const stream = client.getRandomUUIDStream(new Empty());
  stream.on("data", (response) => {
    console.log(response.getUuid());
  });
  stream.on("end", () => {
    console.log("Stream ended.");
  });
}

module.exports = { getRandomString, getRandomUUIDStream };
