# Yelp Recommender

The goal of this project is to create a recommender system for restaurants using [Yelp's Open Dataset](https://www.yelp.com/dataset). I would like to key in on a single city, and depending on the layout of the data, make the type of recommender that would be the most appropriate (whether it be explicit, implicit, or content-based). Ultimately, I would like to make a recommender that does not tilt toward suggesting the most popular places, but instead places that would appeal to individual's specific tastes.

This is not a novel idea. Yelp itself uses a recommendation system for its users, and given that the dataset is publicly available other data scientists have also worked to make their own (some examples include these works by [Sawant & Pai](http://cs229.stanford.edu/proj2013/SawantPai-YelpFoodRecommendationSystem.pdf), [Carillo et al](https://www.math.uci.edu/icamp/summer/research/student_research/recommender_systems_slides.pdf), and [De Paolis Kaluza](http://www.ccs.neu.edu/home/clara/resources/depaoliskaluza_CS6220.pdf)). Techniques used include SVD, clustering, and graph projection.

I would like to build upon these models and improve them. One aim is to create recommender in OOP, such that users would be able to interact with it like an object. Additionally, I would love to create a Flask app as well. Lastly, my aim is to be able to tweak and fine tune existing algorithms. More than just using solutions out-of-the-box, I'm hoping to be able to adjust specific parameters to create the best model possible (exploring techniques for handling cold starts, toying with bias parameters, exploring neighborhoods, and looking into other recommendation techniques not covered in class).

If successful, I'm hoping my project would be able to expand and push forward the existing work in the field of recommendation system. I would like to roll out an effective system that picks up the nuances of user's interests, and doesn't lean too far into simply recommending spots that are highly popular.

In its totality, the Yelp dataset contains over 8M reviews for 200,000+ businesses in 10 metropolitan areas. The information is stored in JSONs.

I expect to run into challenges associated with cold starts and with matrix density, which is why I'm flexible as it comes to approaches. If I find that data is too skewed toward high scores, I'll likely pivot toward a recommender that focuses on the contents of reviews. If the reviews aren't informative (I believe they would be en masse but I could also see there being poor reviews since businesses often incentivize users to leave them), I would focus instead on the scores.

My first steps will be to explore the data and become comfortable with it so that I can start to make informed decisions. I would also like to do additional research on systems that have been created with Yelp data, as well as other recommender systems, so that I can baselines in mind and so that I can explore new techniques.
