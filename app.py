from flask import Flask, jsonify, request
from scraper import scrape_data_gouv
# Import DatasetDB and SessionLocal from your database module
from db import DatasetDB, SessionLocal

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
    datasets = [ds.to_dict() for ds in scraped]

    # 🔽 Persistance
    session = SessionLocal()
    try:
        for ds in scraped:
            # Vérifie si le dataset existe déjà (évite les doublons)
            existing = session.query(DatasetDB).get(ds.id)
            if not existing:
                new_ds = DatasetDB(
                    id=ds.id,
                    title=ds.title,
                    description=ds.description,
                    url=ds.url
                )
                session.add(new_ds)
        session.commit()
    except Exception as e:
        session.rollback()
        print("Erreur DB :", e)
        return jsonify({"message": "Erreur lors de la sauvegarde en base"}), 500
    finally:
        session.close()

    return jsonify({"message": f"{len(datasets)} datasets récupérés et stockés."})


@app.route('/datasets', methods=['GET'])
def get_datasets():
    session = SessionLocal()
    try:
        db_data = session.query(DatasetDB).all()
        result = [d.to_dict() for d in db_data]
        return jsonify(result)
    except Exception as e:
        print("Erreur DB :", e)
        return jsonify([]), 500
    finally:
        session.close()

@app.route('/datasets/<string:dataset_id>', methods=['GET'])
def get_dataset(dataset_id):
    dataset = next((d for d in datasets if d['id'] == dataset_id), None)
    if dataset:
        return jsonify(dataset)
    return jsonify({"message": "Dataset non trouvé"}), 404


if __name__ == '__main__':
    app.run(debug=True)
