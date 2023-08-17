import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)


# view the raw HTML returned
# print(page.text)

# page.content holds raw bytes, which is better than page.text
# for parsing to avoid character encoding issues
soup = BeautifulSoup(page.content, "html.parser")

# select the div that contains all the listings
results = soup.find(id="ResultsContainer")

# prettify() adds the indentation to make the html more presentable
# print(results.prettify())

"""
Find All Jobs
# separate by jobs
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    # print the html elements of the job
    # print(job_element.prettify(), end="\n"*2)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
"""

# Find Python Jobs only
# to ignore case, use a lambda function to process the text before checking
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# find the parent elements to find the other relevant information
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    # print the html elements of the job
    # print(job_element.prettify(), end="\n"*2)
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

    # get the links and their URL inside the div
    links = job_element.find_all("a")
    link_url = links[1]["href"]
    print(f"Apply here: {link_url}\n")
    print()
