import re
import xml.etree.ElementTree as ET
from typing import List, Dict
from logger_config import setup_logger
logger = setup_logger(__name__)

class PaperParser:
    ACADEMIC_KEYWORDS = re.compile(r"\b(university|college|institute|school|academy|research center|labs)\b", re.IGNORECASE)
    NON_ACADEMIC_KEYWORDS = re.compile(r"\b(pharma|biotech|biosciences|corporation|inc|llc|gmbh|therapeutics|laboratories)\b", re.IGNORECASE)

    
    def parse_paper_details(self,xml_data: str) -> List[Dict[str, str]]:
        logger.debug("Parsing XML data for paper details.")
        papers = []
        root = ET.fromstring(xml_data)

        for article in root.findall(".//PubmedArticle"):
            paper_data = {
                'PubmedID': article.findtext(".//PMID", 'N/A'),
                'Title': article.findtext(".//ArticleTitle", 'N/A'),
                'Publication Date': self.extract_publication_date(article)
            }

            authors, non_academic_authors, company_affiliations = self.extract_authors_and_affiliations(article)
            paper_data.update({
                'Authors': ', '.join(authors) if authors else 'N/A',
                'Non-academic Author(s)': ', '.join(non_academic_authors) if non_academic_authors else 'N/A',
                'Company Affiliation(s)': ', '.join(company_affiliations) if company_affiliations else 'N/A',
                'Corresponding Author Email': 'N/A'
            })

            if non_academic_authors:
                papers.append(paper_data)

        return papers

    def extract_publication_date(self, article):
        pubdate_element = article.find(".//PubDate")
        if pubdate_element is not None:
            return f"{pubdate_element.findtext('Year', 'N/A')}-{pubdate_element.findtext('Month', 'N/A')}-{pubdate_element.findtext('Day', 'N/A')}"
        return 'N/A'

    def extract_authors_and_affiliations(self, article):
        authors = []
        non_academic_authors = []
        company_affiliations = []

        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName", '')
            fore_name = author.findtext("ForeName", '')
            full_name = f"{fore_name} {last_name}".strip()

            affiliation_element = author.find(".//AffiliationInfo/Affiliation")
            affiliation = affiliation_element.text if affiliation_element is not None else 'N/A'
            authors.append(full_name)

            if self.NON_ACADEMIC_KEYWORDS.search(affiliation) and not self.ACADEMIC_KEYWORDS.search(affiliation):
                non_academic_authors.append(full_name)
                company_affiliations.append(affiliation)
        
        return authors, non_academic_authors, company_affiliations