from google.cloud import pubsub_v1

def create_pubsub_topic(project_id, topic_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print("Topic created: {}".format(topic.name))
    except Exception as e:
        print("Failed to create topic: {}".format(e))


def pubsub_topic_exists(project_id, topic_name):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    try:
        topic = publisher.get_topic(request={"topic": topic_path})
        print("Topic exists: {}".format(topic.name))
        return True
    except Exception as e:
        print("Topic does not exist: {}".format(e))
        return False


# Replace "project_id" and "topic_name" with your actual project ID and topic name
project_id = "proud-climber-421817"
topic_name = "streamingPubSubTopic"

if not pubsub_topic_exists(project_id, topic_name):
    print(f"Pub/Sub Topic with the given name \"{topic_name}\" is in process to create.")
    create_pubsub_topic(project_id, topic_name)
else:
    print(f"Pub/Sub Topic with the given name \"{topic_name}\" exists. Try with different name if required.")