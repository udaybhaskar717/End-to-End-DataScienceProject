from  src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from pathlib import Path
from src.datascience import logger

STAGE_NAME ="Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status = f.read().split(" ")[-1]
                print(status)
            if status.strip() == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_Transformation = DataTransformation(config=data_transformation_config)
                data_Transformation.train_test_splitting()
            else:
                raise Exception("Your data scheme is not valid")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> stage{STAGE_NAME} STARTED <<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>>>> stage{STAGE_NAME} Completed <<<<<<\n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e
    