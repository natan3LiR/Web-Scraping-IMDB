import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ["https://www.imdb.com/chart/top/"]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        for filmes in response.css('.ipc-metadata-list-summary-item__c'):
            anosBruto = filmes.css('div.hVarDB span.cli-title-metadata-item::text').getall() 
            yield {
                'Titulos': filmes.css('.ipc-title__text::text').get(),
                'Ano': [item for item in anosBruto if item.isdigit() and len(item) == 4],
                'Avaliacao': filmes.css('.ipc-rating-star--rating::text').get()
            }