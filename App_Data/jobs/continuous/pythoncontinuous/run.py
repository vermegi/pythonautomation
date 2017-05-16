import os
from azure.storage.queue import QueueService

print(os.environ['storagekey'])

queue_service = QueueService(account_name='gytryout', account_key=os.environ['storagekey'])

messages = queue_service.get_messages('webjobqueue')
for message in messages:
    print(message.content)
    queue_service.delete_message('webjobqueue', message.id, message.pop_receipt)

