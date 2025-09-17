from pathlib import Path

from src.config_loader import get_config


def upload_files(cursor, data_folder="files/data"):
    config = get_config()
    data_folder = Path(data_folder)
    stage_name = config["etl"]["stage_name"]

    for file in data_folder.glob("*.csv.gz"):
        uri_path = str(file.resolve()).replace("\\", "/")
        print(f"Uploading: {file.name}")
        cursor.execute(f"PUT 'file://{uri_path}' @{stage_name} AUTO_COMPRESS=FALSE OVERWRITE=TRUE")
