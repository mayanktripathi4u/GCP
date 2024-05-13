import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions

project_id = "proud-climber-421817"
topic_id = "streamingPubSubTopic"
 
dataset_id = "streamingDataSet"
table_id = "customers"
 
input_topic = "projects/{}/topics/{}".format(project_id, topic_id)
output_table = f"{project_id}:{dataset_id}.{table_id}"

# create and run a Dataflow job using the DataflowRunner provided by the Apache Beam Python SDK.
"""
This code will create and run a Dataflow job using the specified parameters such as project ID, 
input Pub/Sub topic, output BigQuery table, and other options. 
Make sure to replace "your-project-id", "your-bucket", "your_dataset.your_table", and other placeholders 
with your actual project ID, bucket, dataset, and table names. Adjust other options such as staging_location, 
temp_location, and region according to your requirements.
"""
def run_dataflow_job():
    print("We are now inside the run_dataflow_job......")
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = project_id
    google_cloud_options.job_name = "streaming-dataflow-job"
    google_cloud_options.staging_location = "gs://mt_devops_bkt_01/streaming_data_devops"
    google_cloud_options.temp_location = "gs://mt_devops_bkt_01/temp"
    google_cloud_options.region = "us-central1"
    options.view_as(StandardOptions).runner = "DataflowRunner"
    
    print("All options and config are set.")

    with beam.Pipeline(options=options) as p:
        print("Inside with loop -----> ")

        # (p | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=input_topic)
        #    | "Write to BigQuery" >> beam.io.WriteToBigQuery(
        #        table=output_table,
        #        schema="customer_name:STRING,address:STRING,dob:STRING,email:STRING,purchase_date:STRING,purchase_amount:STRING,purchased_product:STRING,order_id:STRING",
        #        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        #        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
        #     # | "Group by key" >> beam.GroupByKey()
        #     # | "Group by key" >> GroupByKey()
        # )

        # ##### FIX for ValueError: GroupByKey ......
        # # Read from Pub/Sub and apply windowing
        # windowed_data = (p | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=input_topic)
        #                     | "Window into fixed intervals" >> beam.WindowInto(beam.window.FixedWindows(10))
        #                 )
        
        # # Process and aggregate data
        # processed_data = (windowed_data | "Key by some criteria" >> beam.Map(lambda x: (x["key"], x["value"]))
        #                                 | "Group by key" >> beam.GroupByKey()
        #                 )
        
        # # Write to BigQuery
        # (processed_data | "Write to BigQuery" >> beam.io.WriteToBigQuery(
        #     table=output_table,
        #     schema="key:STRING, value:STRING",
        #     create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        #     write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
        # )


        ####### ReWriting the Code.
        (
            p 
            | "Read from Pub/Sub " >> beam.io.ReadFromPubSub(topic=input_topic)
            | "Messages from Pub/Sub Topic are Read " >> beam.Map(print)
        )

# Run the Dataflow job
run_dataflow_job()


"""
If got 
ValueError: GroupByKey cannot be applied to an unbounded PCollection with global windowing and a default trigger

Solution:
    The error you're encountering suggests that you're trying to apply a GroupByKey transformation on an unbounded PCollection with global windowing and a default trigger. This combination is not supported because it could potentially lead to unbounded data accumulation in memory, which is not feasible for streaming data processing.

To resolve this issue, you can modify your Dataflow pipeline to apply windowing and triggering before the GroupByKey operation. This involves defining a windowing strategy for your data, which partitions the data into finite chunks over which aggregations can be performed. Additionally, you may need to define triggers to control when data is emitted from the windows.

Here's an updated version of the Dataflow pipeline with windowing and triggering applied:

In this example, I've used a fixed window of 10 seconds (beam.window.FixedWindows(10)) as an example. You can adjust the window size based on your specific use case and data stream characteristics. Additionally, you may need to define triggers using beam.Triggering() according to your requirements.

"""