# Python-Gen-AI-Developer
Citation Finder Script
This script fetches data from a paginated API, processes each response to find its sources, and logs the citations. It handles rate limiting and provides structured output using logging.

How It Works
Fetching Data: The script fetches data from the paginated API specified in API_URL. It handles rate limiting by waiting and retrying when a 429 status code is encountered.
Processing Responses: Each response is processed to identify its citations by comparing the response text with the context of each source.
Finding Citations: Citations are identified if there's a significant similarity between the response and the source context.
Logging Results: The citations for each response are logged using Python's logging module.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Logging
The script uses the logging module to provide detailed information about its execution. By default, it logs to the console. You can adjust the logging level and format by modifying the logging.basicConfig configuration.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Error Handling
Rate Limiting: The script handles rate limiting (HTTP status code 429) by waiting and retrying after a short delay.
Network Issues: The script catches and logs requests.RequestException for network-related issues.
JSON Parsing: The script catches and logs errors related to JSON parsing.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Example Output
Here’s an example of what the logged output might look like:
2024-05-19 10:00:00 - INFO - Citations: [{'id': '71', 'link': 'https://orders.brikoven.com'}, {'id': '8', 'link': 'https://www.brikoven.com/reservations'}]
2024-05-19 10:00:01 - INFO - Citations: [{'id': '12', 'link': 'https://example.com/resource'}]
