# Tweetimental
Hack Arizona Code and slides

## Inspiration
The increasing number of suicides and depressed people has become a major cause of concern. Being able to identify such individuals and help them out before it is too late would be valuable. 
Previous research did not focus on the cause of mental illness. We wanted our model to provide personalized help by understanding the cause(not just predict the illness) and analyzing the networks and connection of those individuals. 

## What it does
We analyzed tweets to find depressed individuals and predict the cause of their depression (education, relationship or money) 

## How we built it
We found tweets with keywords indicating that the user was depressed - the individuals who published these tweets were potentially depressed. But the depressed tweets may be a one time event and might not prove that the individual is depressed. 
So, we looked at the latest 200 tweets of these users and found the possibility of those tweets being negative. If majority of the tweets were found to be depressing, the probability of the individual suffering from a mental condition would be high. Those tweets were further analysed individually to identify if they were related to relationship, money or education. We aggregated all the negative tweets for each of the categories for a specific user. This helped us identify the major cause of their depression.  

## Challenges we ran into
All of us participated in our first hackathon. Staying up for 36 hours at a stretch was our first experience and the biggest challenge. We are new to python and all the mining we did for the analysis was through python. We ran into issues while mining the data. These issues took some time to be resolved. 
Learning new technologies in extremely short span of time. Dealing with data poses unpredictable challenges. It is especially tough for us as psychology is not our expertise and understanding this data took a lot of time.

## Accomplishments that we're proud of
The visualizations look amazing. We could identify tweets which were clearly not normal. in less than 2 days we managed to make good progress with the analysis. 
Being new to Python, mining the huge dataset was an achievement.

## What we learned
Technical: Python, gephi, NLP
Management: Creative thinking, time management(completed a semester project in 2 days), perseverance, commitment  

## What's next for Tweetimental
We are planning to design an app to provide real time analytics, so that this issue can be solved before it gets chronicle. 
Improve the efficiency of the algorithm by using paid softwares and tools to get real time data which does not limit the number of tweets we collect and analyze.  

