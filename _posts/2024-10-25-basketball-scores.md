---
layout: post
title:  "The Rundown: APIs and College Basketball"
description: A guide to NCAA men's basketball stats and API data collection
image: /assets/img/firebasketball.jpg
---

APIs are becoming increasingly common as a way of gathering information. They are simple, efficient, and secure. Sports data is widely viewable, but it can be difficult to ethically find and use for personal analyses. This is why APIs like "TheRundown" (linked [here](https://apilayer.com/marketplace/therundown-api)), are so useful. Using data collected from TheRundown, I will answer the question: Which NCAA men's basketball teams and conferences outperformed the rest in the 2023 season?

## Ethics
This blog post is totally legal. In gathering data from this website, I made sure to follow several general principles of ethical data collection. I checked for any terms and policies and was lucky to find that there weren't too many barriers. I signed up for a free subscription which allows me 750 requests per month. This is much more than I needed for this project, so that's been an easy guideline to follow. This API also allows me to share all of the data I collected from it. For transparency purposes, please know that all data in my final dataset comes from TheRundown, an API found through apilayer.com.

## API Connection
For this project, I imported the requests library to connect to the API, the pandas library to structure my final dataset, and the matplotlib library to visualize my results.

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
```

Following the documentation found on APILayer, I wrote out the url that would connect me to exactly what I wanted. TheRundown has information on many sports and many aspects of each sport, so I made sure to include documentation that would get me to men's college basketball (5) and an endpoint that gives information about specific teams (/teams).

```python
# API url
base_url = "https://api.apilayer.com/therundown/sports/5" #id 5 is for NCAA men's basketball
endpoint = "/teams" # I'm separating this in case I want to look at something else later
url = base_url+endpoint
```

To keep my personal API key private, I used the following code to extract said key from a hidden file in my repository, rather than writing it out explicitly. 

```python
# Pull in my api key without disclosing it
with open('rundown_api.txt', 'r') as file: 
    rundown_key = file.read()

headers= {
  "apikey": rundown_key
}
```

Finally, I used the requests library's "get" function to connect to the url, and made sure that the connection was secure.

```python
# Call api and ensure connection
r = requests.request("GET", url, headers=headers)
r.status_code # code of 200 means it successfully connected
```

## Final Model
After connecting successfully to the API, I cleaned up the data I got from it and put it into a pandas DataFrame. I'll spare you the data wrangling details, but if you're interested, you can follow [this link](https://github.com/jerhomie2/api/blob/main/code.ipynb) to see my full code.

Ultimately, I ended up with a final DataFrame that contains the team name, mascot, record, and conference name for all 362 teams that were part of a conference last year. Here's just a snippet of that DataFrame.

![Teams Dataframe]({{site.url}}/{{site.baseurl}}/assets/img/teams.png) 

## Summaries/Statistics
The results are in...
Based solely on the number of wins and losses of each team...

The top team is the Uconn Huskies, with 37 wins and 3 losses.
![Top 5]({{site.url}}/{{site.baseurl}}/assets/img/bestteams.png)
The bottom team is the Detroit Mercy Titans, with only 1 win and 31 losses.
![Bottom 5]({{site.url}}/{{site.baseurl}}/assets/img/worstteams.png)
And the top performing conference is BYU's own Big 12!
![conferences]({{site.url}}/{{site.baseurl}}/assets/img/conferences.png)
*Conference rankings based on average wins to account for different conference sizes

**Only every third conference is named to preserve readability

DISCLAIMER: TheRundown is a very up-to-date API with constantly changing data, so when (not if) you try it for yourself, your results will probably look quite a bit different from mine.

## Conclusion
Data is everywhere, just waiting for us to use it. Try using this API for yourself. Or if you aren't as big on sports, find one that can connect you to something you are interested in, and let me know what you find! Whether it be sports, movies, or literally anything else, API's can give us access to a world of knowledge, so let's go collect some data.

To see all of my code and summaries, view my full repository [here](https://github.com/jerhomie2/api)
