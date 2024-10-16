import scrapy


class BmuspiderSpider(scrapy.Spider):
    name = "bmuSpider"
    allowed_domains = ["www.bmu.edu.in"]
    start_urls = ["https://www.bmu.edu.in/"]

    def parse(self, response):
        # Extract all the links on the page
        for href in response.css('a::attr(href)').getall():
            # Join the URL if it's relative
            url = response.urljoin(href)
            
            # Only process pages within the domain
            if "www.bmu.edu.in" in url:
                yield scrapy.Request(url, callback=self.parse_page)
        
        # Follow pagination or other dynamic content if needed
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_page(self, response):
        # Save the page content or scrape specific data
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'content': response.css('body').get(),
        }
