import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions

def run_dataflow_job(project_id, input_topic, output_table):
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = project_id
    google_cloud_options.job_name = "streaming-dataflow-job"
    google_cloud_options.staging_location = "gs://mt_devops_bkt_01/staging"
    google_cloud_options.temp_location = "gs://mt_devops_bkt_01/temp"
    google_cloud_options.region = "us-central1"
    options.view_as(StandardOptions).runner = "DataflowRunner"
    
    with beam.Pipeline(options=options) as p:
        (p | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=input_topic)
           | "Write to BigQuery" >> beam.io.WriteToBigQuery(
               table=output_table,
               schema="customer_name:STRING,address:STRING,dob:DATE,email:STRING,purchase_date:TIMESTAMP,purchase_amount:FLOAT,purchased_product:STRING,order_id:STRING",
               create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
               write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

# Example usage:

project_id = "proud-climber-421817"
topic_id = "streamingPubSubTopic"
 
dataset_id = "streamingDataSet"
table_id = "customers"
 
input_topic = "projects/{}/topics/{}".format(project_id, topic_id)
output_table = f"{project_id}:{dataset_id}.{table_id}"

# run_dataflow_job("your-project-id", "projects/proud-climber-421817/topics/streamingPubSubTopic", "your-project-id:streamingDataSet.tbl_streamingData")
run_dataflow_job(project_id, input_topic, output_table)