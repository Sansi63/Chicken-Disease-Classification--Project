from cnnClassifier.constants import *
from cnnClassifier.utils.common import create_directories,read_yaml
from dataclasses import dataclass
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self,
                 config=CONFIG_FILE_PATH,
                 params=PARAMS_FILE_PATH):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    