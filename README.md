# Yelp Recommender: Restaurants in Charlotte
The goal of this project was to build an explicit recommender system using collaborative filtering for restaurants in Charlotte using [Yelp's Open Dataset](https://www.yelp.com/dataset). I wanted to explore the mechanics of recommendations systems, and explore a new library in [Surprise](http://surpriselib.com).

# Technologies
* Python (including NumPy, Pandas, Matplotlib, Seaborn, and Surprise)
* Amazon EC2

# Looking Forward
I consider this project foundational in my understanding and implementation of recommender systems. Looking forward, here are some things I'd like to explore:
* Creating user interactivity, either through a self-contained Python class and/or a Flask app
* Further researching ways to handle skewed, non-evenly distributed data
* Adjusting the recommendation system to ensure that there's serendipity and variety, and that smaller businesses with fewer reviews are represented
* Building a hybrid recommender that also takes into account the text content of reviews

# Acknowledgements
A big thanks to Dan Rupp, Juliana Duncan, Peter Galea, and Austin Penner, each of whom poured a lot of their time and energy in helping me complete this project. Thanks to [Yelp](https://www.yelp.com/dataset) for making their dataset available. Additionally, several publications helped me in understanding the theory behind recommenders and test metrics:
* [Mansoury et al's "Flatter is better: Percentile Transformations for Recommender Systems"](https://arxiv.org/pdf/1907.07766.pdf)
* [Wllmott & Matsuura's "Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance"](https://www.int-res.com/articles/cr2005/30/c030p079.pdf)
* [Chai & Draxler's "Root mean square error (RMSE) or mean absolute error (MAE)? – Arguments against avoiding RMSE in the literature"](https://www.researchgate.net/profile/Tianfeng_Chai/publication/272024186_Root_mean_square_error_RMSE_or_mean_absolute_error_MAE-_Arguments_against_avoiding_RMSE_in_the_literature/links/54e3776f0cf2b2314f5d2f3c/Root-mean-square-error-RMSE-or-mean-absolute-error-MAE-Arguments-against-avoiding-RMSE-in-the-literature.pdf).
