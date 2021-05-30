import scrapy
from scrapy import Spider
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
import inputs as inp
import uuid


class PostsSpider(Spider):
    name = "posts"
    start_urls = [
        'https://mbasic.facebook.com/login/'
    ]

    def parse(self, response):
        """Parsing entry point
        """
        return FormRequest.from_response(
            response,
            formdata={
                "email": inp.email,
                "pass": inp.password
            },
            callback=self.make_search
        )
    
    def make_search(self, response):
        link = 'https://mbasic.facebook.com/search/photos/?q={}'.format(self.event)
        next_page = response.urljoin(link)
        yield scrapy.Request(next_page, callback=self.parse_page)

    def parse_page(self, response):
        container = response.css('#BrowseResultsContainer > div > div')
        links = container.css('a::attr(href)').extract()
        yield from response.follow_all(links, self.parse_post)

        next_page = response.css('#see_more_pager a')
        yield from response.follow_all(next_page, self.parse_page)

    def parse_post(self, response):
        _id = uuid.uuid4()
        _post = response.css('._2vj8::text').get() or ''
        _image = response.css('#objects_container img::attr(src)').get() or ''
        _comments = response.css('._14ye::text').getall() or ''

        yield {
            "_id": str(_id),
            "post_text": _post,
            "image": _image,
            "comments": _comments
        }