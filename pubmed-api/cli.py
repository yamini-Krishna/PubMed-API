import argparse
from pubmed_api_client import PubMedAPIClient
from paper_parser import PaperParser
from csv_exporter import CSVExporter
from logger_config import setup_logger
logger = setup_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Fetch research papers from PubMed with non-academic authors.')
    parser.add_argument('query', type=str, help='Search query for PubMed')
    parser.add_argument('-f', '--file', type=str, help='Output CSV file name')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()

    if args.debug:
        logger.debug(f"Debug Mode: ON")
        logger.debug(f"Search Query: {args.query}")

    client = PubMedAPIClient()
    parser = PaperParser()
    exporter = CSVExporter()

    pubmed_ids = client.fetch_pubmed_ids(args.query)
    if not pubmed_ids:
        logger.info("No PubMed IDs found for the query.")
        return

    if args.debug:
        logger.info(f"Fetched {len(pubmed_ids)} PubMed IDs.")

    xml_data = client.fetch_paper_details(pubmed_ids)
    if not xml_data:
        logger.info("No data retrieved from PubMed.")
        return

    papers = parser.parse_paper_details(xml_data)
    if not papers:
        logger.info("No papers with non-academic authors found.")
        return

    if args.debug:
        logger.info(f"Found {len(papers)} papers with non-academic authors.")
        logger.info("Sample data:", papers[0] if papers else 'No Data')

    if args.file:
        exporter.save_to_csv(papers, args.file)
    else:
        logger.info("Results:")
        for paper in papers:
            logger.info(paper)

if __name__ == '__main__':
    main()
