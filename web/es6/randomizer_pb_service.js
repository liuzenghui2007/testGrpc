"use strict";

// package: randomizer
// file: randomizer.proto

var randomizer_pb = require("./randomizer_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;
var RandomizerService = function () {
  function RandomizerService() {}
  RandomizerService.serviceName = "randomizer.RandomizerService";
  return RandomizerService;
}();
RandomizerService.GetRandomString = {
  methodName: "GetRandomString",
  service: RandomizerService,
  requestStream: false,
  responseStream: false,
  requestType: randomizer_pb.Empty,
  responseType: randomizer_pb.RandomStringResponse
};
RandomizerService.GetRandomUUIDStream = {
  methodName: "GetRandomUUIDStream",
  service: RandomizerService,
  requestStream: false,
  responseStream: true,
  requestType: randomizer_pb.Empty,
  responseType: randomizer_pb.RandomUUIDResponse
};
exports.RandomizerService = RandomizerService;
function RandomizerServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}
RandomizerServiceClient.prototype.getRandomString = function getRandomString(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(RandomizerService.GetRandomString, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function onEnd(response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function cancel() {
      callback = null;
      client.close();
    }
  };
};
RandomizerServiceClient.prototype.getRandomUUIDStream = function getRandomUUIDStream(requestMessage, metadata) {
  var listeners = {
    data: [],
    end: [],
    status: []
  };
  var client = grpc.invoke(RandomizerService.GetRandomUUIDStream, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onMessage: function onMessage(responseMessage) {
      listeners.data.forEach(function (handler) {
        handler(responseMessage);
      });
    },
    onEnd: function onEnd(status, statusMessage, trailers) {
      listeners.status.forEach(function (handler) {
        handler({
          code: status,
          details: statusMessage,
          metadata: trailers
        });
      });
      listeners.end.forEach(function (handler) {
        handler({
          code: status,
          details: statusMessage,
          metadata: trailers
        });
      });
      listeners = null;
    }
  });
  return {
    on: function on(type, handler) {
      listeners[type].push(handler);
      return this;
    },
    cancel: function cancel() {
      listeners = null;
      client.close();
    }
  };
};
exports.RandomizerServiceClient = RandomizerServiceClient;