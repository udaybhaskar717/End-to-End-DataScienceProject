from  src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer


from src.datascience import logger

STAGE_NAME ="Model Trainer stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def initiate_model_Trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_tarin_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>> stage{STAGE_NAME} STARTED <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_Trainer()
        logger.info(f">>>>>>>> stage{STAGE_NAME} Completed <<<<<<\n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e
    