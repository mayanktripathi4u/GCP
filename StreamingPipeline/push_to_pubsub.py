from google.cloud import pubsub_v1
# from . import generateStreamingData as gsd
import generateStreamingData as gsd

project_id = "proud-climber-421817"
topic_id = "streamingPubSubTopic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_message(message):
    future = publisher.publish(topic_path, message.encode())
    print(future.result())

# Example usage:
for data in gsd.generate_streaming_data():
    publish_message(data)
