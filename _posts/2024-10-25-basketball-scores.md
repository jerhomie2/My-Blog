---
layout: post
title:  "The Rundown: APIs and College Basketball"
description: A guide to NCAA men's basketball stats and API data collection
image: /assets/img/firebasketball.jpg
---

APIs are becoming increasingly common as a way of gathering information. They are simple, efficient, and secure. Sports data is widely viewable, but it can be difficult to ethically find and use for personal analyses. This is why APIs like "TheRundown" (linked [here](https://apilayer.com/marketplace/therundown-api)), are so useful. Using data collected from TheRundown, I will answer the question, which NCAA men's basketball teams and conferences outperformed the rest in the 2023 season?

## Disclaimer
This blog post is totally legal. In gathering data from this website, I made sure to follow several general princibles of ethical data collection. I checked for any terms and policies and was lucky to find that there weren't too many barriers. I signed up for a free subscription which allows me 750 requests per month. This is much more than I needed for this project, so that's been an easy guideline to follow. This API also allows me to share all of the data I collected from it. For transparency purposes, know that all data in my final dataset come from TheRundown, an API found through apilayer.com.

## API Connection
For this project, I imported the requests library for connecting to the api, the pandas library for structuring my final dataset, and the matplotlib library to visualize my results.

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
```

Following the documentation found on APILayer, I wrote out the url that would connect me to exactly what I wanted. TheRundown has information on many sports and many aspects of each sport, so I made sure to include documentation that would get me to men's college basketball (5), and an endpoint that gives information about specific teams (/teams).

```python
# API url
base_url = "https://api.apilayer.com/therundown/sports/5" #id 5 is for NCAA men's basketball
endpoint = "/teams" # I'm separating this in case I want to look at something else later
url = base_url+endpoint
```

To keep my personal API key private, I used the following documentation to extract said key from a hidden file in my repository, rather than writing it out explicitly. 

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
After connecting successfully to the API, I had to clean up the data that I got from it. I'll spare you the details, but if you're interested, you can follow [this link](https://github.com/jerhomie2/api/blob/main/code.ipynb) to see my full code. Essentially, there was much more information than I needed and some info I did want was embedded weird or not formatted in the most useful way.

Ultimately, I ended up with a final dataframe that contains the team name, mascot, record, and conference name for all 362 teams that were part of a conference last year. Here's just a snippet of that dataframe.

![Teams Dataframe]({{site.url}}/{{site.baseurl}}/assets/img/teams.png) 

## Summaries/Statistics
The results are in...
Based solely on the number of wins and losses of each team, 
The top team is the Uconn Huskies with 37 wins and only 3 losses.
![Top 5]({{site.url}}/{{site.baseurl}}/assets/img/bestteams.png)
The bottom team is the Detroit Mercy Titans with only a single win and 31 losses.
![Bottom 5]({{site.url}}/{{site.baseurl}}/assets/img/worstteams.png)
And the top performing conference is BYU's own Big 12!
![conferences]({{site.url}}/{{site.baseurl}}/assets/img/conferences.png)

To see the full code and summaries, view my full repository [here](https://github.com/jerhomie2/api/blob/main/code.ipynb)

## Conclusion


TheRundown is a very up-to-date API with constatly changing data.