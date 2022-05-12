## Bolt's job recommender

- This is a project of a recommendation system using nlp that takes a user description about his professional experiences and skills and then try to match with the Bolt's jobs descriptions to give a list of recommendations.

### Data

- The data was scraped from Bolt's careers website (https://bolt.eu/en/careers/positions) and the notebook with the webscraper can be found at `notebooks/bolt_jobs_scraping.ipynb`.

### ML approach

- The approach used to make this recommendation system was the bag of words method and cosine similarity. You can find the notebook at `notebooks/bolt_bag_of_words_training.ipynb`.

### Pyscript application

- I've used the `Pyscript` framework to 'deploy' this model into a web application, so it can run it all on client-side!

- You can see the app in action here: https://arthur-rocha.github.io/pyscript/bolt

### Docker

- I've made a docker container to deploy a flask app which can receive http requests with the description as a parameter and return the recommended job list.

- To run the container on port 7979 use this command on bash:

`docker build -t docker_bolt_jobs . && docker run -d -p 7979:80 --name=docker_bolt_jobs -v $PWD:/app docker_bolt_jobs`

------ Resquest example ------


