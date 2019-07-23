# PlannedParenthoodLocations
A public dataset of Planned Parenthood health center locations for benevolent use.

Python's Scrapy library was used to generate `health_centers.csv`, which is intended to be easily geocoded for use in GIS-based research. 

Feel free to use this dataset in any way that sheds light on healthcare in America - and to modify the code however you like. If the dataset contributes to any published work, please acknowledge the hard work of Alexandra Dawson and John C. Merfeld.

Note that this code will not run "out of the box." The scrapers need to be embedded within the `spiders` directory of a traditional Scrapy setup. First, `pp_links_scraper.py` should be run, followed by `pp_scraper.py`
