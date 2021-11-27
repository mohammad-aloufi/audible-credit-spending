# Project Overview

[Audible](https://audible.com) is a very well-known service among those who love books like myself. They provide audio books and podcasts on their platform.

Audible offers a few types of memberships for users to pick from, but in general, it goes along the lines of giving the member a number of credits they can use to buy audio books in exchange of the member subscribing to a monthly or a yearly plan.

A credit can usually be spent towards buying any audio book, no matter how much it costs, some memberships give you 1 credit monthly, some give you 2 credits monthly, and some of them you have to subscribe to a yearly plan where you get either 12 or 24 credits a year.

At the time of this writing, a credit worth is in the range of to $9.56 to $14.95 depending what type of membership you have.

How much a credit is worth is calculated by how much you're paying divided by the amount of credits you'd get.

# Problem Statement

Along with getting credits, audible memberships offer a 30% discount on the books you buy if you decide not to spend the credit, and here is something I'm personally stuck at and thus decided to make this project

The question is: If I want to buy a book, when should I spend a credit to buy that book? and when it's better to pay for it with real cash, saving the credit for a book that's more worth spending the credit on.

As I mentioned before, with an audible credit, you can buy a book no matter how much it costs thus you can save yourself a lot of money if you play your cards right, for example:

if you buy a book that costs $30 with a credit, you've saved yourself money in the range of $16.05 to $20.44.

For me, the deciding factor if I should spend a credit or buy the book and use the 30% discount is the following:

* Book price.
* Book length.

Generally speaking, the higher the price, the more I would consider spending the credit. The length plays a part too if the price isn't that far off from the credit price.

Even though, more often than not, I find myself torn between both options, so I decided to do something about it.

# Metrix

I used the accuracy_score to measure the model score because It will give us the accuracy of how much it works against the testing data. As in, it calculate the amount it predicted right vs the times it predicted wrong and give us the score that way.
It's the number of correct predictions divided by the total predictions multiplied by 100. Since our our labels are in just one column, we didn't need morre than that for that model.

# Solving the problem

I first started by collecting a dataset that includes books I've bought from audible, and I labeled each one with a credit_spent label to record if I spent a credit on that book or not.

I then trained a machine learning model on that dataset to recognize my credit spending vs cash purchasing habits for books.

Lastly, I made a web app with flask, including the model, so you can basically just go in, and enter a book price, and the length of that book, and see if it's worth paying for in real money or spending the credit is a better idea.

# Data Preprocessing

Our dataset contains 4 features:

* price
* hours
* minutes
* credit_spent

I merged the hours and minutes into one column and dropped the columns I no longer need.

Please look at the provided notebook for more details on how I did it.

# Data Exploration

Our dataset contains the following features:

* price
* hours
* minutes
* credit_spent

Like I explained in the last section, I merged  the hours and minutes columns into 1 called duration, so for example:

If hours is 11 and minutes is 30, in the new duration column that would be 11.5.

When we explored the prices, we foundout that the cheapest book costed $2.76, while the most expensive book costed $46.99. Meanwhile, the average book costed just about $2.66.

We also explored the book duration, we foundout that the shortest book was around 1 hour and a half in length, while the longest book was around 55 hours. Meanwhile, the average book was around 18 hours and 15 minutes in length.

# Data Visualization

One of the things I explored is the credit spending habits, lets take a look

![image](https://github.com/mohammad-aloufi/audible-credit-spending/blob/master/image.png?raw=true)

As you can see, both the books I spent credits on and the books I didn't are equal. In the dataset, it's actually 50 books each.

# Implementation

When I built the model pipeline, I used RandomForestClassifier algorithm and GridSearch. I used GridSearch because the way it works, you give it a few parameters like a grid, and then it combines them together in every possible way, giving us the best values hopefully.

# Refinement: Model Evaluation and Validation

It didn't take much for me to get to 100% accuracy to be honest, I think that's mainly because there was a pattern that was very easy for the model to figure out.
However, I managed to get to the same result but with less time by changing the parameters. At first, I was getting 100% accuracy with a training time of 0.14 minutes. I then decided to change the max_depth from 10 to 1, 5, and 10, I got a better result, 100% accuracy with  a training time of 0.08 minutes.
I also changed the estimators and max_leaf_nodes so they wouldn't take as much time.

parameters for the 0.14 minutes model:

* max_depth: 10, 10, 10.
* n_estimators: 10, 10, 10.
* min_samples_split: 2, 3, 4].
* random_state: 42.
* max_leaf_nodes: 10, 10, 10.

parameters for the 0.08 minutes model:

* max_depth: 1, 5, 10.
* n_estimators: 1, 5, 10.
* min_samples_split: 2, 3, 4.
* random_state: 42.
* max_leaf_nodes: 2, 5, 10.

I think the good thing here is that we saved time when building the pipeline rather than getting a better accuracy because the model is as accurate as it can get, and that's a good thing.

# Justification

the end result of this project is a model and a web app to help with the decision if buying with a credit is worth it or not 
With the help of the web app as well, one can just launch the app and input the book data and just check and test the model.

# Reflection

This project was interesting to say the least. Since it's actually a personal project, it was something I looked forward to. I had a problem before starting this project, and now that I finished it, I can say that I don't have this big problem when deciding what to do when I want to buy books. I learned a lot when I was doing this project, doing everything from the scratch was part of it. Collecting the data, labeling them, and then building the model, and actually create a web app that makes things easier for everyone wo wants to use it.
I think that collecting the data was the hardest part. It took me some time to gather everything and label every book. But I made a script to help with that, and it actually helped. After that comes the building of the pipeline, it wasn't hard, but was really interesting to say the least, I thought I'd be messing with the parameters for a while, but it was an easy ride actually.

# Improvement

As for the improvements, I'm honestly happy that I managed to get to an excellent accuracy with my model, and for me that means I really did good with all the steps I did before, from data collection to building the machine learning pipeline and what not, however, I think that it could be deceiving just as much. I think I need more data to really test the model. For now I have just 100 books and it's enough for now, but I'd love me some data that go to other ranges of numbers too. I also would love to improve the app even more and add a feature where you just put in the link of the book, and it gets all the required info for you and then predict on them instead of you manually typing and selecting everything.

# Installation

First thing first, you need jupyter and python.

You also need the following libraries:

* pandas
* flask
* joblib
* pickle
* sklearn
* matplotlib
* seaborn

Or you can just do "pip install -r requirements.txt"

# The web app

After you install the libraries, just run the app.py file, and then go to http://localhost:5000 to open the app.
If there is no model.pkl file in the project folder, you'd have to run the jupyter notebook first. Run all cells in there, when they finish running, you can run the app.py file again.

# Folder structure

Here is a list of the files in the repo folder and their description:

1. templates: This is the folder for the html pages for the flask server to serve.
2. app.py: The flask app.
3. data.csv: the dataset for the project.
4. data_collection.py: I coded this script to make it easier for me to add books to the dataset at the time of collecting the data.
5. model.pkl: the machine learning model.
6. project.ipynb: the jupyter notebook that contains everything from data exploration to building the machine learning pipeline and creating the actual model.
7. README.md: the README for the repo.
8. requirements.txt: Library requirements.

# Conclusion

Throughout this project, I collected a dataset that contains some information about some books on audible, like their member price, and duration. I then labeled every book with if it's good to spend an audible credit on that book or not. I then started exploring the dataset on this notebook and made a machine learning model to hopefully help me and others to decide if it's a good idea to buy a book with a credit, or just use the 30% discount that comes with all audible memberships. I also made a web app where you can input the book price and the book length to see for that book if spending the credit is worth it or not.