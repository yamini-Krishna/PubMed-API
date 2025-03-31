import csv
from logger_config import setup_logger
logger = setup_logger(__name__)

class CSVExporter:
    def save_to_csv(self,data, filename):
        logger.debug(f"Saving data to CSV file: {filename}")
        try:
            fieldnames = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"]
            filtered_data = [{k: v for k, v in item.items() if k in fieldnames} for item in data]

            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(filtered_data)
            logger.info(f"Results successfully saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")
