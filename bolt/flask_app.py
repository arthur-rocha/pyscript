from flask import Flask, request
from recommendation_engine import Recommender
import os

app = Flask(__name__)

job_model = Recommender()

@app.route('/')
def home():
    return 'Bolt Job recommender'

@app.route('/recommend_job', methods=['POST'])
def recommend_job():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        description = request.json['description']
        recomend_dict = job_model.recommend(description).to_dict(orient='index')
        return recomend_dict
    else:
        return 'Content-Type not supported!'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host='0.0.0.0', port=port)