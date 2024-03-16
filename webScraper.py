import pandas as pd
import pdfkit as pdf
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\saumi\\Desktop\\Spring-2023\\KTP\\KTP-AI\\WebDriver\\chromedriver.exe')
driver.get('https://engineering.utdallas.edu/academics/undergraduate-majors/undergrad-advising/advising-faq/')

results = []
content = driver.page_source
soup = BeautifulSoup(content)

driver.quit()

#print(soup.findAll(attrs = 'accordion ui-accordion ui-widget ui-helper-reset'))

for element in soup.findAll(attrs = 'accordion ui-accordion ui-widget ui-helper-reset'):
    questions = element.find('h4')
    if questions not in results:
        results.append(questions.text)
    answers = element.find('p')
    if answers not in results:
        results.append(answers.text)

#print(results)

df = pd.DataFrame({'ans' : results})
df.to_html('ans.html')

path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
config = pdf.configuration(wkhtmltopdf = path_wkhtmltopdf)

saumil = 'url.pdf'
pdf.from_url('https://engineering.utdallas.edu/academics/undergraduate-majors/undergrad-advising/advising-faq/', saumil, configuration=config)
