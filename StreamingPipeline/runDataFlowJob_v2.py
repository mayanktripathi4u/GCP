import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions
from apache_beam.options.pipeline_options import StandardOptions

project_id = "your-project-id"
input_topic = "projects/{}/topics/{}".format(project_id, topic_id)
output_table = "your-project-id:your_dataset.your_table"

def run_dataflow_job():
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = project_id
    google_cloud_options.job_name = "streaming-dataflow-job"
    google_cloud_options.staging_location = "gs://your-bucket/staging"
    google_cloud_options.temp_location = "gs://your-bucket/temp"
    google_cloud_options.region = "us-central1"
    options.view_as(StandardOptions).runner = "DataflowRunner"
    
    with beam.Pipeline(options=options) as p:
        # Read from Pub/Sub and apply windowing
        windowed_data = (p | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(topic=input_topic)
                            | "Window into fixed intervals" >> beam.WindowInto(beam.window.FixedWindows(10)))
        
        # Process and aggregate data
        processed_data = (windowed_data | "Key by some criteria" >> beam.Map(lambda x: (x["key"], x["value"]))
                                        | "Group by key" >> beam.GroupByKey())
        
        # Write to BigQuery
        (processed_data | "Write to BigQuery" >> beam.io.WriteToBigQuery(
            table=output_table,
            schema="key:STRING, value:STRING",
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND))

# Run the Dataflow job
run_dataflow_job()
