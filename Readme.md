
## Introduction
A Movie recommender system has became an interesting research topic due to the growth of users in a mobile environment. To recommend movies, a complete aggregation of user’s preferences and reviews are required to assist users to find the best movies in a more convenient way.

---
## Features 📋
* Existing users can login and new users can register.
* Users can search through various movies.
* Users can submit ratings for the movies.
* Users can add movies to their watch list(My List).
* Users can get movie recommendations (Recommendation algorithm named Collaborative Filtering is used which suggests new movies based on the ratings given by the user.)
---

## Technologies used 
* Python (Jupyter Notebook) 
* Web Technologies- html,css,javascript, bootstrap, Django
* Machine learning libraries in python3- pandas,numpy,scipy
* Database used- SQLite

---

## Algorithm Used- Collabortive Filtering 
* Collaborative filtering filters information by using the interactions and data collected by the system from other users. It's based on the idea that people who agreed in their evaluation of certain items are likely to agree again in the future.
* When we want to find a new movie to watch we'll often refer our friends for recommendations. Naturally, we have greater trust in the recommendations from friends who share tastes similar to our own.
* Collaborative-filtering systems focus on the relationship between users and items. The similarity of items is determined by the similarity of the ratings of those items by the users who have rated both items.
* There are two types of collaborative filtering
    * **User-based**- which measures the similarity between target users and other users.
    * **Item-based**- which measures the similarity between the items that target users rate or interact with and other items.
   
> I have used user based collaborative filtering in this project.

> In this project, Slope One algorithm is used in order to predict individual recommendations, which are further  combined into a group recommendation using the multiplicative utilitarian strategy. Slope one algorithm is a special form of collaborative filtering algorithm, which has the characteristics of easy to use, accurate recommendation and high computational efficiency. We have chosen a Group Model Based approach in order to implement a group recommendation strategy, by building the group profile using the individual profile of each member of the group. With this approach, a group recommender system considers the preferences of each individual in the group with some criterion that maximizes the happiness of the group (also called group’s satisfaction). The concept of group happiness can vary, it sometimes corresponds to the average of preferences of the members, and other times to the happiest (and least happy) member, etc.
---

## Problems faced and solutions adopted to resolve them
* Ramp-Up and Cold Start problems
* slope one algorithm can lead to ramp-up and cold start problems.
* To solve these problems an initial load is made using the MovieLens 10M dataset with data from anonymous users, items and scores. Once this dataset is loaded, we       use this data to initialize the matrix of average of rating differences used by the Slope One algorithm. 
* Thus, taking advantage of the benefits of the Slope One algorithm, new users must just rate a few movies when they enter the system for the first time so that the     algorithm can find entries in the matrix of average of rating differences and start generating good recommendations for the user.
   
## Web Application Development
* Register page(for new users)

![image](https://user-images.githubusercontent.com/79890808/170688685-d8c28cd0-a82a-4507-bfd9-92ed93fe5c88.png)


* Login Page(for existing users)

![image](https://user-images.githubusercontent.com/79890808/170688807-89f24838-8317-4710-acd3-5da74c108f06.png)


* Browse through movies

![image](https://user-images.githubusercontent.com/79890808/170689078-017bac59-c665-4061-9a46-d67d296dcc0d.png)

![image](https://user-images.githubusercontent.com/79890808/170689104-af9989c6-4545-43b7-a53e-963f3270de7f.png)


* Submit Rating and add to My List

![image](https://user-images.githubusercontent.com/79890808/170689264-9f975fc8-b4b9-4f7b-9f8f-f4a614998e4a.png)


* My List

![image](https://user-images.githubusercontent.com/79890808/170689330-767c3038-e1b3-41ab-a698-d5f31cc7af8d.png)


* Get Recommendations

![image](https://user-images.githubusercontent.com/79890808/170689508-31b7f988-4f15-4846-8697-17805f82e81e.png)


## Installation 📦

* Clone the project and download the source code.
* Once inside the folder run following commands:

> $ pip install -r requirements.txt                                                                                           

> $ python manage.py runserver

NOTE: Run server locally
    : Install Python 3.7 to run the source code 

Go to > localhost:8000

     
 
