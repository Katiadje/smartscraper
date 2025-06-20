from flask import Flask, jsonify, request
from scraper import scrape_data_gouv

app = Flask(__name__)

datasets = []

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur l’API de scrapping data.gouv.fr !"})

@app.route('/scrap', methods=['POST'])
def scrap():
    global datasets
    body = request.json or {}
    page = body.get('page', 1)
    page_size = body.get('page_size', 20)

    scraped = scrape_data_gouv(page, page_size)
    # Convertit en dict pour JSON
    datasets = [ds.to_dict() for ds in scraped]

    return jsonify({"message": f"{len(datasets)} datasets récupérés."})

@app.route('/datasets', methods=['GET'])
def get_datasets():
    return jsonify(datasets)

@app.route('/datasets/<string:dataset_id>', methods=['GET'])
def get_dataset(dataset_id):
    dataset = next((d for d in datasets if d['id'] == dataset_id), None)
    if dataset:
        return jsonify(dataset)
    return jsonify({"message": "Dataset non trouvé"}), 404


if __name__ == '__main__':
    app.run(debug=True)
