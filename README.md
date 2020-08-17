# snobby_yelp_project

## Objective: 
Filter out 4.5 ratings or better using yelp's api (currently not possible with yelp's browser)

## Motivation: 
Call me snobby (I admit) but sometimes one just wants to search for the best of the best.  At a certain point, 4 stars just becomes the norm (really depends on your location, but I've been duped many times for average or mediocre quality, when in fact it should have been at least above average. 

Furthermore, when my fiance and I are searching for dinner in the local area, we usually end up scrolling through the same 40 or so restaurants and don't end up going to the next page. As we are moving to a new city, I wanted to come up with a creative (and efficient) way to filter out good places we can check out. 

Of course the caveat is that reviews can be heavily skewed (through manipulation) and can miss some gems (bad service but awesome food, would still like to give that a shot).

Currently wrote this project mainly for food only, but can certainly use it for other services as well. 

## How-to:

To use this, you will need to sign up for a api_key at https://www.yelp.com/fusion (literally took 10 seconds).  Then, create a new python file named config.py and type/save the following: 

api_key = 'insert_api_key_here'

Then, run 'elite_yelp_browser.py'. Output will be:
1. CSV file saved to directory (matching search criteria) for future browsing. 
2. Open up tabs on your browser for immediate browsing. 

## Future plans:
Will definitely be adding to this repository as I go as I see fit.  This is just the first iteration of this project. 
