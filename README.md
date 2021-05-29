# Big Scale Analytics 2021 - Group Project
## Team Apple 

Team members:
- Agon Husejni
- Bleron Ramaj
- François Grau

## 🕵🏻‍♂️Project description

You have decided to form a startup called “LingoRank” with two of your University friends and become a millionaire. You have until June to create a proof of concept for your investors. Your startup will revolutionize the way people learn and get better at a foreign language.

To improve one’s skills in a new foreign language, it is important to read texts in that language. These text have to be at the reader’s language level. However, it is difficult to find texts that are close to someone’s knowledge level (A1 to C2). You have decided to build a model for English speakers that predicts the difficulty of a French written text. This can be then used, e.g., in a recommendation system, to recommend texts (for example, recent news articles) that are appropriate for someone’s language level. If someone is at A1 French level, it is inappropriate to present a text at B2 level, as she won’t be able to understand it. Ideally, a text should have many known words and may have a few words that are unknown so that the person can improve.
To do this would require:
1. Thinking how to model the problem and gathering data (French texts, sentences, news articles etc.) and labelling them with the relevant level,
2. Building a model that predicts the difficulty/level of a new text,
3. Evaluating how good the model is.

## ☁️ Web Application

In order to make our solution available to everyone, we decided to create a web application. 

It will be possible to type a sentence in a text field and predict the difficulty level of this sentence. The level of accuracy will also be displayed. 

Here is the link to our web application : https://unique-grid-305713.ew.r.appspot.com

### How to use them ?

It's very simple. 

There is a text box below *Write a sentence*, just write a sentence as mentioned (example : Bonjour j'ai 30 ans)

To calculate the level of the sentence, click on *Test*.

The web application will then return the level of the sentence (example: A1).

We told you, it's very simple 😉😉

### How does our solution works ?

Our solution was created with the different tools offered by Google, namely Natural Language and App Engine.

Natural Language allowed us to train our dataset and build our predictive model. It is also possible to retrieve the API of this module.

Thanks to App Engine, it allowed us to make it available to everyone. The <a href="https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service" target="_blank">Google Documentation</a> helped us to create the base of our web application. Our web application is composed of the following files:

-	Main.py
-	App.yaml
-	Requirements.txt
-	*Application* folder containing script.js et style.css
-	*Templates* folder containing index.html

The *main.py* file contains the Natural Language API that links to our prediction.

### How to deploy it ?

To deploy the web application, you need to run the command `gcloud app deploy` from the root directory of the project, where the App.yaml file is located:

```bash
gcloud app deploy
``` 

To launch the browser and access the web application, you need to enter the following command: 

```bash
gcloud app browse
```

## 1️⃣ Milestone 1
### First steps
The first week was mostly spent brainstorming, researching and discussing about the approach to take on how to solve the problem. Each member on his own spent a good amount of time gathering ideas from different articles that can be found in the last section of this document.

First we set specific and precise criteria for each category (A1-C2) and used those criteria to evaluate the texts during our data collection. The criteria grid we used can be found here :

### 💾 Collecting the Data
For each category we used different types of literature or web pages to extract sentences, you'll fin also the reprensented pourcentage of each category.
- For A1 16% - provided sentences for educational A1 level & online exams
- For A2 18% - provided sentences for educational A2 level & online exams
- For B1 19% - provided sentences for educational B1 level & online exams
- For B2 16% - articles and educational B2 level 
- For C1 17% - specialized articles and & online exams for C1 level (DALF)
- For C2 14% - mostly specialized articles or literary work and online exams for C2 level (DALF)

First label were defined based on what the website announce. Then we all individually gave for each sentences which label we thought were the most appropriate. Every member put a different color on label which wasn't right for him. At the end we debate for each label we werent's okay and discussed to agree to decide on a final label.

### 📄 Contributions 
Our dataset has a total of 1119 annotated sentences 

### 💭 Problem solving approach
To create our model we will have to use different features that would potentially increase the accuracy. One popular feature to consider is the “(log) word frequency to text difficulty ratio”. A useful tool for that can be the wordstats text analysis library in Python.
Another important aspect and feature we need to consider is the cognativity. Cognates are words that are similar in both meaning and form in two languages (example : important-important, reason-raison, etc.) Based on some articles we read, the way around cognates is to simply lower the difficulty level of the sentence in which cognates are found. We can consider cognates as words that are similarly written, but we can encounter “false friends” (words that are written similarly in Botha languages but mean different things). At the moment, we are considering going on with similarly written words as cognates, regardless of the possible differences in meaning, being aware that it can give us false positives in certain cases. We might slightly change our methodology in this aspect, in case some other way to go about this issue comes to our minds in the later stages.

We plan on solving the problem as a classification. We will model the difficulty of entire sentences, however, for special cases, like cognates, we might consider building a separate service to take into account special words and probably break them down into tokens. In the final solution we will  combine the outputs of the different analytics.

As a main tool, we will be using what we will work on throughout the semester, namely the Google Cloud resources, including AutoML. We still need to get more familiar with the detailed features that are provided there, but we have also gathered different algorithms (for the frequency, similarity, etc.) from the articles we have read, in case we might need some intervention though different tools.
The more detailed explanations of the modelling and the concrete steps of the problem solving will be provided later on in the proceeding Milestones.

## 2️⃣ Milestone 2

For this second part of the group project, we decided to use google cloud. Among the different possibilities offered by this platform we have focused on the "Natural Language". This module allowed us to upload our database containing French sentences with their respective level in order to be able to apply a text classification using AutoML. Once the model is created, it is possible to predict the level of difficulty of a randomly written sentence on the google cloud platform.

Once the prediction model has been created and tested. We used another module offered by google cloud called APP Engine. This module allowed us to create an API which will aim to link, thanks to the FLASK library, a User Interface with the web service. This User Interface will aim for any user to be able to enter a sentence in French in order to obtain the level of difficulty of this same phrase on the basis of the model offered by google cloud.

### 🔁 1st Iteration

We have imported the raw data in AutoML Google Cloud, without modification.

Confusion Matrix

|   | A1  | A2  | B1  | B2  | C1  | C2  |
|---|---|---|---|---|---|---|
| A1  | 78%  | 11%  | 6%  | 6%  | - | - |
| A2  | 42%  | 53%  | - | - | - | 5%  |
| B1  | 14%  | 18%  | 41%  | 5%  | 18%  | 5%  |
| B2  | 6%  | 6%  | 18%  | 29%  | 29%  | 12%  |
| C1  | 5%  | 16%  | 16%  | 11%  | 37%  | 16%  |
| C2  | 6%  | - | 6%  | 6%  | - | 81%  |
 
Evaluation model

Precision : 62% // Recall :    27,93%

### 🔁 2nd Iteration

In our 2nd iteration, we performed some basic modifications on the raw data. Here are the tasks we did:

 - Transformation of upper case letters into lower case letters
 - Removal of punctuation
 - Removal of numbers
 - Lemmatization

Then, we imported the data into AutoML to build the model. 

Confusion Matrix

|   | A1  | A2  | B1  | B2  | C1  | C2  |
|---|---|---|---|---|---|---|
| A1  | 39%  | 22%  | 33%  | -  | 6% | - |
| A2  | 5%  | 53%  | 21% | - | 16% | 5%  |
| B1  | 5%  | -  | 80%  | 10%  | -  | 5%  |
| B2  | 6%  | 6%  | 12%  | 47%  | 18%  | 12%  |
| C1  | 5%  | 11%  | 11%  | 11%  | 47%  | 16%  |
| C2  | -  | - | 6%  | 6%  | 6% | 81%  |

Evaluation model

Precision : 82,14% // Recall : 21,1%

## Relevant datasets 
- https://french.kwiziq.com/learn/reading
- https://lingua.com/french/reading/
- http://www.delfdalf.fr/_media/exemple-1-sujet-complet-dalf-c2-3.pdf
- https://www.francepodcasts.com/2020/04/14/dalf-c1-comprehension-ecrite/
- https://www.podcastfrancaisfacile.com/dictee-2/dictee-delf.html
- https://www.kaggle.com/devicharith/language-translation-englishfrench


## 📚 Papers and articles on the topic
- Vlachos, Michalis & Lappas, Theodoros. (2011). "Ranking German Texts by Comprehensibility for Foreign Document Retrieval."
- Uitdenbogerd, Alexandra. (2005). "Readability of French as a Foreign Language and its Uses." 
- François, Thomas. (2012). "A readability formula for French as a foreign language"
- François, Thomas. (2015). "Readability: a one-hundred-year-old field still in his teens"
- N. Ott. Information retrieval for language learning: An exploration of text difficulty measures
- A. L. Uitdenbogerd. Web readability and computer-assisted language learning.

- https://www.colorincolorado.org/article/using-cognates-develop-comprehension-english
- https://www.fluentu.com/blog/french/french-cognates/
- https://www.telc.net/en/about-telc/news/detail/the-secret-life-of-cognates.html
- http://alumni.cs.ucr.edu/~mvlachos/pubs/ENIR2011.pdf
- https://cental.uclouvain.be/cefrlex/flelex
 

## Criteria Grid for each category
- http://www.provincedeliege.be/sites/default/files/media/7476/Europass_-_European_language_levels_-_Self_Assessment_Grid.pdf
