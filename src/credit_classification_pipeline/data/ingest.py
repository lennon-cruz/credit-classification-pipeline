import os
import kagglehub
import logging
from pathlib import Path
from dotenv import load_dotenv
from credit_classification_pipeline.config import get_absolute_path, load_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

def download_kaggle_dataset(dataset_name: str, output_dir: Path) -> Path:
    """Downloads a dataset via kagglehub and returns the local path."""
    logging.info(f"Downloading dataset {dataset_name}...")
    saved_path = kagglehub.dataset_download(
        dataset_name, output_dir=str(output_dir), force_download=True
    )
    return Path(saved_path)


if __name__ == "__main__":
    config = load_config("data.yaml")

    for source_key, source_details in config["sources"].items():
        target_dir = get_absolute_path(source_details["local_dir"])
        target_dir.mkdir(parents=True, exist_ok=True)

        download_kaggle_dataset(
            dataset_name=source_details["kaggle_path"], output_dir=target_dir
        )

