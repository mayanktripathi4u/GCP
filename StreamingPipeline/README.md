# Project - Create a Streaming data pipeline
The aim of this project is to create a end-to-end pipeline for streaming data.

A python code will generate synthetical data which wil acts as a streaming data and feed to Pub/Sub. Which then get processed via Dataflow jobs, and the processed data saved into BigQuery Table.

Sure, let's break down the process into steps and write Python code for each step:

Step 1: Generating Synthetic Streaming Data: [Code](/GCP/StreamingPipeline/generateStreamingData.py)
    
Make sure to install `pip3 install faker`

To validate, run command from terminal `python3 generateStreamingData.py` 

Step 2: Publishing Data to Pub/Sub Topic: [Code](/GCP/StreamingPipeline/push_to_pubsub.py)

Assuming the Pub/Sub Topic was already created, if not [Create a Topic](/GCP/StreamingPipeline/create_PubSub.py) by running command `python3 create_PubSub.py`.

Make sure to install `pip3 install google google-cloud google-cloud-pubsub` if required, and [authenticate it](/GCP/Cloud_SDK/README.md)

To Publish the message use [Code](/GCP/StreamingPipeline/push_to_pubsub.py).

Step 3: Dataflow Job to Process and Store Data into BigQuery

We can create and run a Dataflow job using the DataflowRunner provided by the Apache Beam Python SDK. [Code]()


BigQuery
`pip install google-cloud-bigquery`



`pip install 'apache-beam[gcp]'`


In Apache Beam, a collection is called a PCollection , and a transform is called a PTransform . A PCollection can be bounded or unbounded. A bounded PCollection has a known, fixed size, and can be processed using a batch pipeline.
A PCollection is a unbounded collection. Immutable, and unbounded. The main difference with a list is mainly the unbounded characteristic and it's especially powerful when you are streaming data (from a large file, or from a unbounded source, like PubSub).

