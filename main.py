from app.logger import setup_logger
from app.api_integration import FreelancerAPI
from app.data_storage import DataStorage

def main():
    logger = setup_logger()
    api = FreelancerAPI(logger)
    data = api.fetch_ai_projects()

    if data:
        logger.info("Saving data to JSON and CSV formats...")
        DataStorage.save_to_json(data)
        DataStorage.save_to_csv(data)
        logger.info("Data saved successfully!")
    else:
        logger.warning("No data to save.")

if __name__ == "__main__":
    main()
