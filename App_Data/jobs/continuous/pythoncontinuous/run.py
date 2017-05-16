import os
import sys
import platform

msg = "Using Python '{0}'".format(platform.python_version())  
print(msg)  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'env')))
from azure.storage.queue import QueueService

print(os.environ['storagekey'])

queue_service = QueueService(account_name='gytryout', account_key=os.environ['storagekey'])

messages = queue_service.get_messages('webjobqueue')
print("messages")
for message in messages:
    print(message.content)
    for property in vars(message):
        print(property)
    #queue_service.delete_message('webjobqueue', message.id, message.pop_receipt)

print("done")
