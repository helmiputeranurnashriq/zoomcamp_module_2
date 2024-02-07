from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow.fs import GcsFileSystem

@data_loader
def load_data(*args, **kwargs):
    bucket_name = 'mage-zoomcamp-hputera'
    blob_prefix = 'nyc_taxi_data'
    root_path = f"{bucket_name}/{blob_prefix}"    
    pa_table = pq.read_table(
        source=root_path,
        filesystem=GcsFileSystem(),   
   
    )

    return pa_table.to_pandas()
