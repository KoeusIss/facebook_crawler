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
And here a sample from MongoDB

```json
{
	"_id":"a6655f45-7176-4d02-bbb6-ad118c92e1f4",
	"post_text":"Décès de l'ancien Président Français Valéry Giscard d'Estaing, le deuxième ex-Président Français qui disparaît au cours du mandat d'Emmanuel Macron après Jacques Chirac en fin  2019.",
	"image":"https://scontent.fnbe1-2.fna.fbcdn.net/v/t1.6435-0/cp0/e15/q65/s320x320/129555757_3613863322011039_7848826003306537405_n.jpg?_nc_cat=105&ccb=1-3&_nc_sid=110474&efg=eyJpIjoiYiJ9&_nc_ohc=twVrgdhoGK0AX868_Cq&_nc_ht=scontent.fnbe1-2.fna&tp=9&oh=a894d6f9a46cded47cddda34748d8fdf&oe=60DB5E4E","comments":[
		"Paix a son âme toute mes condoléances à sa famille ",
		"Jamais deux sans trois tu mise sur qui Sarko ou Mouloud ? Lol",
		" hhhh c vrai, on verra si le dicton sera respecté hhhhh. Bon on souhaite longue vie à tous les autres encore en vie, mais il doivent faire attention, d'après quelques infos il'm est mort du covid . Alors il fait qu'ils fassent attention, surtout Hollande il est a retrouvé son surpoids hhh",
		" d'après sa famille, il est mort des suites du covid. ",
		" hadher imanikh . Lol",
		"Paix à son âme",
		" puis c'est lui qui a révélé ça à propos de notre ex cher président hhhh"
	]
}
```