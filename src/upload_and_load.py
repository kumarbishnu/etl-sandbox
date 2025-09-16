from pathlib import Path
from urllib.parse import quote

from src.config_loader import get_config


def upload_files(cursor):
    config = get_config()
    data_folder = Path(config["etl"]["data_folder"])
    stage_name = config["etl"]["stage_name"]

    for file in data_folder.glob("*.csv.gz"):
        uri_path = str(file.resolve()).replace("\\", "/")
        print(f"Uploading: {file.name}")
        cursor.execute(f"PUT 'file://{uri_path}' @{stage_name} AUTO_COMPRESS=FALSE OVERWRITE=TRUE")