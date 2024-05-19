# -*- coding: utf-8 -*-
"""Python Gen-AI Developer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19DtJcveOaMKFxQ_6ylLXU0S-c29Rti55
"""

import requests
import time
import difflib
import logging

API_URL = 'https://devapi.beyondchats.com/api/get_message_with_sources'

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data(api_url):
    """Fetch data from the paginated API."""
    data = []
    page = 1
    while True:
        try:
            response = requests.get(api_url, params={'page': page})
            if response.status_code == 429:
                logging.warning(f"Rate limit reached at page {page}. Retrying after delay.")
                time.sleep(5)  # Delay before retrying
                continue
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to retrieve data from page {page}: {e}")
            break

        try:
            page_data = response.json()
            if not isinstance(page_data, list):
                logging.error(f"Unexpected data format at page {page}: {page_data}")
                break
        except ValueError as e:
            logging.error(f"Failed to parse JSON from page {page}: {e}")
            break

        if not page_data:
            break

        data.extend(page_data)
        page += 1
        time.sleep(1)  # Adding a delay between requests to prevent rate limiting
    return data

def find_citations(response, sources):
    """Identify sources that contributed to the response."""
    citations = []
    response_set = set(response.split())
    for source in sources:
        source_set = set(source['context'].split())
        similarity_ratio = difflib.SequenceMatcher(None, response, source['context']).ratio()
        if response_set & source_set or similarity_ratio > 0.8:
            citation = {'id': source['id']}
            if 'link' in source and source['link']:
                citation['link'] = source['link']
            citations.append(citation)
    return citations

def process_responses(data):
    """Process each response and find its citations."""
    results = []
    for item in data:
        if not isinstance(item, dict):
            logging.error(f"Unexpected item format: {item}")
            continue
        response = item.get('response')
        sources = item.get('sources')
        if response is None or sources is None:
            logging.error(f"Missing 'response' or 'sources' in item: {item}")
            continue
        citations = find_citations(response, sources)
        results.append(citations)
    return results

def main():
    data = fetch_data(API_URL)
    if data:
        results = process_responses(data)
        for result in results:
            logging.info(f"Citations: {result}")

if __name__ == "__main__":
    main()