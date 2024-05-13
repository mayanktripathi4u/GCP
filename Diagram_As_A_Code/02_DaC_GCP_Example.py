from diagrams import Diagram, Cluster
from diagrams.gcp.security import Iam
# from diagrams.gcp.storage.Storage import gcp_storage
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import Functions
from diagrams.gcp.analytics import Bigquery, Dataflow

from diagrams.custom import Custom

with Diagram("Data Pipeline", show=False):
    gcs = GCS("Cloud Storage")
    fun = Functions("Cloud Function")
    df = Dataflow("Dataflow Job")
    bq = Bigquery("BigQuery")

    with Cluster("Pipeline"):
        gcs >> fun >> df >> bq 





