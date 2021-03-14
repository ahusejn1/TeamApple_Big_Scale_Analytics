# Big Scale Analytics 2021 - Group Project
## Team Apple

Team members:
- Agon Husejni
- Bleron Ramaj
- François Grau

## Project description

You have decided to form a startup called “LingoRank” with two of your University friends and become a millionaire. You have until June to create a proof of concept for your investors. Your startup will revolutionize the way people learn and get better at a foreign language.

You have noticed that, to improve one’s skills in a new foreign language, it is important to read texts in that language. These text have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2). You have decided to build a model for English speakers that predicts the difficulty of a French written text. This can be then used, e.g., in a recommendation system, to recommend texts (for example, recent news articles) that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.
To do this would require:
1. Thinking how to model the problem and gathering data (French texts, sentences, news articles etc.) and labelling them with the relevant level,
2. Building a model that predicts the difficulty/level of a new text,
3. Evaluating how good the model is.


## Milestone 1
### First steps
The first week was mostly spent brainstorming, researching and discussing about the approach to take on how to solve the problem. Each member on his own spent a good amount of time gathering ideas from different articles that can be found in the last section of this document.

First we set specific and precise criteria for each category (A1-C2) and used those criteria to evaluate the texts during our data collection. The criteria grid we used can be found here :

### Collecting the Data
For each category we used different types of literature or web pages to extract sentences
- For A1
- For A2
- For B1
- For B2 
- For C1
- For C2

### Contributions 
Our dataset has a total of 1124 annotated sentences 

### Problem solving approach
To create our model we will have to use different features that would potentially increase the accuracy. One popular feature to consider is the “(log) word frequency to text difficulty ratio”. A useful tool for that can be the wordstats text analysis library in Python.
Another important aspect and feature we need to consider is the cognativity. Cognates are words that are similar in both meaning and form in two languages (example : important-important, reason-raison, etc.) Based on some articles we read, the way around cognates is to simply lower the difficulty level of the sentence in which cognates are found. We can consider cognates as words that are similarly written, but we can encounter “false friends” (words that are written similarly in Botha languages but mean different things). At the moment, we are considering going on with similarly written words as cognates, regardless of the possible differences in meaning, being aware that it can give us false positives in certain cases. We might slightly change our methodology in this aspect, in case some other way to go about this issue comes to our minds in the later stages.

We plan on solving the problem as a classification. We will model the difficulty of entire sentences, however, for special cases, like cognates, we might consider building a separate service to take into account special words and probably break them down into tokens. In the final solution we will  combine the outputs of the different analytics.

As a main tool, we will be using what we will work on throughout the semester, namely the Google Cloud resources, including AutoML. We still need to get more familiar with the detailed features that are provided there, but we have also gathered different algorithms (for the frequency, similarity, etc.) from the articles we have read, in case we might need some intervention though different tools.
The more detailed explanations of the modelling and the concrete steps of the problem solving will be provided later on in the proceeding Milestones.


## Papers and articles on the topic
