import numpy as np
import random
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)

model = LightFM(loss = 'warp')

model.fit(data['train'], epochs = 30, num_threads = 3)

def sample_recommendation(model, data, user_ids, n_users, n_items, known_positives):


	for user_id in user_ids:

		scores = model.predict(user_id, np.arange(n_items))

		top_item = data['item_labels'][np.argsort(-scores)]

		movies_to_recommend = []

		for movie_to_recommend in top_item[:3]:
			if movie_to_recommend not in movies_to_recommend:
				movies_to_recommend.append(movie_to_recommend)
			else:`
				continue

		for j in movies_to_recommend:
			print('			%s' % j)


def find_user_id(model, data):
	answered_user_ids=[]

	favourite_movie = input('Please name your favourite movie: ')
	n_users, n_items = data['train'].shape

	for user_id_I_want in range(n_users):
		known_positive_movies = data['item_labels'][data['train'].tocsr()[user_id_I_want].indices]
		for known_positive_movie in known_positive_movies[:900]:
			if favourite_movie.lower() in known_positive_movie.lower():
				answered_user_ids.append(user_id_I_want)
				if len(answered_user_ids)>5:
					return answered_user_ids, n_users, n_items, known_positive_movies
					break
				else:
					continue
			else:
				continue
	if answered_user_ids == []:

		for N_iteration in range(3):
			answered_user_ids.append(random.randrange(3))

		return answered_user_ids, n_users, n_items, known_positive_movies

	else:

		return answered_user_ids, n_users, n_items, known_positive_movies


final_user_ids, n_users, n_items, known_positives = find_user_id(model, data)

print('Recommendation:')

sample_recommendation(model, data, final_user_ids, n_users, n_items, known_positives)


