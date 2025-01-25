from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME ="Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_Validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME ="Model Trainer stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> stage{STAGE_NAME} STARTED <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_Trainer()
        logger.info(f">>>>>>>> stage{STAGE_NAME} Completed <<<<<<\n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME ="Model Evaluation stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> stage{STAGE_NAME} STARTED <<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_Evaluation()
        logger.info(f">>>>>>>> stage{STAGE_NAME} Completed <<<<<<\n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e
    

    