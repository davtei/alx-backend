import redis from 'redis';

const client = redis.createClient();

client.on('error', function (err) {
  console.log('Redis client not connected to the server: ' + err);
});

client.on('connect', function () {
  console.log('Redis client connected to the server');
}).on('error', function (err) {
  console.log('Redis client not connected to the server: ' + err);
});

client.subscribe('holberton school channel');

client.on('message', function (channel, message) {
  if (channel === 'holberton school channel') {
    if (message === 'KILL SERVER') {
      client.unsubscribe('holberton school channel');
      console.log(message);
      client.quit();
    } else {
      console.log(message);
    }
  }
});
