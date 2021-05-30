# Big Scale Analytics 2021 - Group Project

<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/apple-think-diff.svg" width="350" height="250"//>
</p>

## Team Apple 

Team members:
- Agon Husejni
- Bleron Ramaj
- François Grau

## 🕵🏻‍♂️Project description

You have decided to form a startup called *LingoRank* with two of your University friends and become a millionaire. You have until June to create a proof of concept for your investors. Your startup will revolutionize the way people learn and get better at a foreign language.

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

### How does our solution work ?

Our solution was created with the different tools offered by *Google*, namely *Natural Language* and *App Engine*.

*Natural Language* allowed us to train our dataset and build our predictive model. It is also possible to retrieve the API of this module.

Thanks to *App Engine*, it allowed us to make it available to everyone. The <a href="https://cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service" target="_blank">Google Documentation</a> helped us to create the base of our web application. Our web application is composed of the following files:

-	Main.py
-	App.yaml
-	Requirements.txt
-	*Application* folder containing script.js et style.css
-	*Templates* folder containing index.html

The *main.py* file contains the *Natural Language* API that links to our prediction.

### How to deploy it ?

To deploy the web application, you need to run the command `gcloud app deploy` from the root directory of the project, where the App.yaml file is located:

```bash
gcloud app deploy
``` 

To launch the browser and access the web application, you need to enter the following command: 

```bash
gcloud app browse
```

## Milestones

In order to be able to lead this project correctly, it was necessary to work it in 3 milestones director:

  1. The first step was mostly spent brainstorming, researching and discussing about the approach to take on how to solve the problem. Develop a model of the general objective, collect the necessary data (French sentences with their associated level ranging from A1 to C1).
  2. For this second part of the group project, we decided to use *Google Cloud*. The *Natural Language* module allowed us to upload our database containing Frenc sentences with their respective level in order to be able to apply text classification using *AutoML*. The aim was to link this service to an endpoint which will be able to predict the difficulty of an entry text.
  3. Work on the data (pre-processing, tackle cognates, etc...) find other ways to improve the model.

## Predictive models

### Personnalized model

XXXXXXXXXXXXXXXXXXXXXXXXx

### *CamemBERT* model

After experimenting with the two previous models, we found it interesting to experiment with a third one, which also represented an opportunity to improve precision.

Our choice on the model calle *CamemBERT*

<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/camembert.jpg" width="230" height="150"//>
</p>

###### Why this choice ?

*CamemBERT* is a tool that allows you to determine, based on written data based on text written in natural language, the feeling it returns. This very used model at first glance makes perfect sense when you know that it is pre-trained on 138GB of French text.

*CamemBERT* chooses the words to be predicted dynamically, that is to stay, not during the pre-processing of the input data, but during forward pass, by randomly masking certain words in a sequence.

###### Putting the model into practice

As for each model, we therefore decide to do three iterations of the model while trying to improve its precision. However, we faced a complication. Indeed, we have run our pie chart model on *Google Colab*. Our very first iteration, unfortunately, could not be completed, because not having enough resources on *Google Colab*, the model could not finish its run.

Within the models, the difficulty levels have been converted into numbers with the following coresspondence:

  - A1 = 0
  - A2 = 1
  - B1 = 2
  - B2 = 3
  - C1 = 4
  - C2 = 5
  
Finally, it is important to mention that this template contains two parameters to configure which are as follows :

  - Batch size: number of examples analyzed by the model during an iteration. The larger the batch size, the more memory it consumes.
  - Epoch: expression to say how many times the model should cycle through all the training data. An epoch can contain multiple iterations. The number of iterations depends on the batch size.

For example, let's say we have 2000 training examples that we are going to use. We can divide the dataser of 2000 examples into batches of 500 then it will take 4 iterations to complete 1 epoch.

###### 🔁 1st iteration

Below, we find the result of the first iteration, which consisted in uploading into the model dataset train provided on AIcrowd of 4800 lines. In order to allow the model to be able to finish its run and obtain these results, we have taken the decision to proportionally reduce (that is to say by increasing the same proportion of data from the different levels) these 4800 lines into 1200 lines.

<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/1.1.png" width="230" height="150"//>
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/1.2.png" width="250" height="200"/>
</p>

  - The general accuracy of the model is 48%
  - As we can see, on the summary of the results of precision, recall and F1, it is important to note that for the score 5 which corresponds to level C2, the model is not able to predict data.
  - For level 0 and 2 (A1 and B1), the model is quite goodbecause we can see a balanced balance between precision, recall and F1.

###### 🔁 2nd iteration

This second test consisted of uploading into the model the same dataset train as the first iterations, therefore the dataset of 1200 lines.

the only element on which we tried to play in order to obtain a better precision was the Batch size. Indeed, having reduced the size of the dataset by 75%, we said to ourselves that it was justifiable to reduce the size of the Batch as well. We therefore decided to run an iteration with a batch size reduced to 5.

<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/2.1.png" width="230" height="150"//>
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/2.2.png" width="250" height="200"/>
</p>

  - The general accuracy of the model is 59%
  - The results of this iteration shows us that for the value 1 (corresponding to level A2), unfortunately we have no precision, no recall as well as a F1 score of 0. However, for the rest of values (A1, B1, B2, C1, C2), we have a balance between precision, recall and F1 which is fairly balanced with in particular a clear improvement in scores of C2.

###### 🔁 3rd iteration

For this third, we decided to upload another dataset which is the one used for the other iterations to which we applied the preprocessing explained in the corresponding part.

<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/3.1.png" width="230" height="150"//>
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/3.2.png" width="250" height="200"/>
</p>

  - The general accuracy of the model is 60%
  - Batch size 5 and Epoch 3
  - This improvement is principally due to the fact that for the value 1 (corresponding to level A2), we obtain scores contrary to the 2nd iteration.

### *AutoML* model

The 3rd model, we decided to use the tool presented in class, i.e. *AutoML*.

The advantage it has is that it is simple to use. You just have to upload the database and the *Google* service will train and create the model by itself.

However, it does have one negative point. It is not possible to modify the parameters as we wish. 


<p align="center">
  <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/GCP-logo.png" width="280" height="150"//>
</p>

###### 🔁 1st iteration

We have imported the raw data in *AutoML*, without modification.

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

Accuracy: 52% // Precision: 62% // Recall: 28%

###### 🔁 2nd iteration

In our 2nd iteration, XXXXXXXXXXXX

Confusion Matrix

|   | A1  | A2  | B1  | B2  | C1  | C2  |
|---|---|---|---|---|---|---|
| A1  | 79%  | 11%  | 10%  | -  | - | - |
| A2  | 26%  | 40%  | 31% | 1% | 1% | -  |
| B1  | 8%  | 20%  | 50%  | 16%  | 3%  | 4%  |
| B2  | -  | 1%  | 9%  | 51%  | 18%  | 22%  |
| C1  | 1%  | -  | 3%  | 30%  | 47%  | 19%  |
| C2  | -  | 4% | 6%  | 19%  | 20% | 51%  |

Evaluation model

Accuracy: 53% // Precision: 70% // Recall: 22%

###### 🔁 3rd Iteration

In our 3rd iteration, we performed some modifications on the raw data. Here are the tasks we did:

 - Transformation of upper case letters into lower case letters
 - Removal of punctuation
 - Removal of numbers
 - Lemmatization

Then, we imported the data into *AutoML* to build the model. 

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

Accuracy : 58% // Precision : 82% // Recall : 21%

###### 🔁 4th Iteration

In our 4th iteration, we used an existing dataset from CEFRLex. 

"FLELex is a lexicon for French as a foreign language (FFL) that reports the normalized frequencies of words (lemmas) across each level of the CEFR (Common European Framework of Reference for Languages). The frequencies have been estimated on a corpus of FFL textbooks and FFL simplified readers. More details on the corpus, the computation and normalization of the word frequencies, and the ressource itself can be found in"

*François, T., Gala, N., Watrin, P. & Fairon, C. FLELex: <a href="http://www.lrec-conf.org/proceedings/lrec2014/pdf/1108_Paper.pdf" target="_blank">a graded lexical resource for French foreign learners.</a> In the 9th International Conference on Language Resources and Evaluation (LREC 2014). Reykjavik, Iceland, 26-31 May.*

Then, we imported the data into *AutoML* to build the model. 

Confusion Matrix

|   | A1  | A2  | B1  | B2  | C1  | C2  |
|---|---|---|---|---|---|---|
| A1  | 18%  | -  | 36%  | -  | 41% | 5% |
| A2  | 8%  | -  | 40% | 3% | 43% | 6%  |
| B1  | 4%  | 1%  | 35%  | 3%  | 50%  | 7%  |
| B2  | 2%  | 1%  | 37%  | 4%  | 49%  | 7%  |
| C1  | 3%  | -  | 26%  | 1%  | 62%  | 7%  |
| C2  | 4%  | - | 16%  | 1%  | 60% | 19%  |

Evaluation model

Accuracy : 33% // Precision : 50% // Recall : 2%

## AIcrowd <img src="https://raw.githubusercontent.com/ahusejn1/TeamApple_Big_Scale_Analytics/main/Data/brwzrtijgulc12ow1ohb.png" width="25" height="25">

In order to evaluate the different models mentioned above and to obtain a neutral level of precision without having modified any parameters, we based ourselves on the *AIcrowd* results of these models in order to make the final choice of the kept model.

## 👨🏻‍💻 Team work repartition

Agon
 - Text cleaning and prepocessing
 - UI dealing
 - Personnalized model
 - *ReadMe* contributor

Bleron
 - *Google Auto-ML* manager
 - *App Engine* handling
 - Cognates issue solving
 - *ReadMe* contributor

François
 - Literature research
 - UI builder
 - *CamenBERT* model
 - *ReadMe* contributor

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
- https://ledatascientist.com/analyse-de-sentiments-avec-camembert/
- https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9
- https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9
- https://medium.com/@vitalshchutski/french-nlp-entamez-le-camembert-avec-les-librairies-fast-bert-et-transformers-14e65f84c148
 

## Criteria Grid for each category
- http://www.provincedeliege.be/sites/default/files/media/7476/Europass_-_European_language_levels_-_Self_Assessment_Grid.pdf
