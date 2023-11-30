import { createClient } from 'redis';

function connectServer() {
  const client = createClient();

  client.on('connect', function () {
    console.log('Redis client connected to the server');
  });

  client.on('error', function (err) {
    console.log('Redis client not connected to the server: Error: Redis connection to ' + err.address + ':' + err.port + ' failed - ', err.message);
  });
}

connectServer();
