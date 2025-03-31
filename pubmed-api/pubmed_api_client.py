import requests
from typing import List, Optional
from logger_config import setup_logger
logger = setup_logger(__name__)

class PubMedAPIClient:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def fetch_pubmed_ids(self,query: str) -> List[str]:
        logger.debug(f"Fetching PubMed IDs for query: {query}")
        try:
            params = {
                'db': 'pubmed',
                'term': query,
                'retmax': 100,
                'retmode': 'json'
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('esearchresult', {}).get('idlist', [])
        except requests.RequestException as e:
            logger.error(f"Error fetching PubMed IDs: {e}")
            return []

    def fetch_paper_details(self,paper_ids: List[str]) -> Optional[str]:
        try:
            params = {
                "db": "pubmed",
                "id": ",".join(paper_ids),
                "retmode": "xml"
            }
            response = requests.get(self.EFETCH_URL, params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching paper details: {e}")
            return None