import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  'phoneNumber': '9876543210',
  'message': 'New job created'
}

const job = queue.create('push_notification_code', notification).save(function (error) {
  if (!error) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', function () {
  console.log('Notification job completed');
}).on('failed', function () {
  console.log('Notification job failed');
});
