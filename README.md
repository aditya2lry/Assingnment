# Documentation

## Setup Instructions:
Install Python and necessary libraries as mentioned above.
Set up MySQL database and update db_config with your database credentials.

## Running the Solution:
### Run the script using the command:
"python extract_urls.py"

The script will perform a Google search, extract the URLs, and save them in a CSV file and a MySQL database.

# Report
## Approach:
Used Selenium for automating the Google search and BeautifulSoup for parsing the HTML content.
Extracted URLs from the search results and filtered them based on the given pattern.
Saved the extracted URLs to both a CSV file and a MySQL database.

## Challenges:
Handling pagination in Google search results to extract a sufficient number of URLs.
Ensuring the headless browser runs efficiently and captures all relevant URLs.

## Code Quality:
Organized the code into functions for better readability and maintainability.
Provided clear documentation and setup instructions.
