import scrapy
#to permit venv on power shell
# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
#make sure interpretor is set to venv
# run from command line: scrapy crawl ebook    make sure youre in venv and right file


class EbookSpider(scrapy.Spider):
    name="ebook"
    start_urls=["https://books.toscrape.com/"]
    
    def parse(self,response):
        print("[Our Response]")
        # print(response)

        ebooks=response.css("article")   #not .get because then it is a string
        for ebook in ebooks:
            title=ebook.css("a::text").get()
            price=ebook.css("p.price_color::text").get()
            print(title,price)
        # print(response.css("h3 a::text").get())