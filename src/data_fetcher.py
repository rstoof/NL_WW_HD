import time
import requests
import pandas as pd
from .config import BASE_URL, ROWS_PER_REQUEST, NUM_REQUESTS
import logging
logger=logging.getLogger(__name__)


class DataFetcher:
    def __init__(self, base_url=BASE_URL, rows_per_request=ROWS_PER_REQUEST, num_requests=NUM_REQUESTS):
        self.base_url = base_url
        self.rows_per_request = rows_per_request
        self.num_requests = num_requests
        self.data = []
        self.df = None
    
    def fetch_data(self):
        urls = [f"{self.base_url}&rows={self.rows_per_request}&offset={str(i*self.rows_per_request)}" for i in range(self.num_requests)]
        datas=[]
        for url in urls:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


            data=requests.get(url,headers=headers)
            #retry if request fails
            delay_time=0.2
            retries=10
            while data.status_code!=200 and retries>0:

                logger.error(f"""Request failed with status code {data.status_code}. 
                             for url: {url}.
                             Retrying in {delay_time} seconds""")
                time.sleep(delay_time)
                delay_time*=2
                retries-=1
                data=requests.get(url,headers=headers)

            data_json=data.json()
            datas.append(data_json)
        self.data=datas
        # self.data = [requests.get(url).json() for url in urls]
    
    def process_data(self):
        flattened_data = [item for sublist in self.data for item in sublist]
        self.df = pd.DataFrame(flattened_data)
    
    def get_dataframe(self):
        return self.df
    
    def run(self):
        self.fetch_data()
        self.process_data()


class CountryData:
    def __init__(self, country_name, dataurl):
        self.country_name = country_name
        self.dataurl=dataurl

    
    def get_dataurl_contents(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        data=requests.get(self.dataurl+"?output=json",headers=headers)
        self.json=data.json()

    def get_map_pdf_url(self):
        data=self.json
        for item in data.get("content", []):
            if "paragraph" in item and "href" in item["paragraph"]:
                start = item["paragraph"].find("https://opendata.nederlandwereldwijd.nl/documents/")
                end = item["paragraph"].find(".pdf", start) + 4  # 4 is the length of ".pdf"
                if start != -1 and end != -1:
                    return item["paragraph"][start:end]
        return None