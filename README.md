```
						Scraping Facebook
```
## Scraping and crawling
This simple crawler helps to scrape and crawl data from Facebook based on given event,
it try to grab all photos (in the sake of simplicity) for a particular event and all related comments,
image, and post. and Store all collected data in **MongoDB** database.

## Stack and requirement
* Python3 (3.8.x recommended) 
* Preinstalled MongoDB
* And follow the pip requirements

## How to use it
You need to update the `inputs.py` file with your own credentials.
and than grab all the requirment with PIP:

```bash
pip install -r requirements.txt
```
Then you need to specify your event when passing the crawl command

```bash
scrapy crawl posts -a event="your specific event here"
```