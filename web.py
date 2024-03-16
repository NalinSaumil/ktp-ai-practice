import requests
from bs4 import BeautifulSoup
import pdfkit

path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

def convert_to_pdf(url):
    # retrieve HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # remove unwanted elements from HTML
    for script in soup(["script", "style"]):
        script.extract()

    # get text content from HTML
    text = soup.get_text()

    # create a PDF file
    pdfkit.from_string(text, 'output.pdf', configuration=config)
    
    print("PDF generated successfully!")


convert_to_pdf("https://engineering.utdallas.edu/academics/undergraduate-majors/undergrad-advising/advising-faq/")