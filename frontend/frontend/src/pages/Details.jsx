import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

const Details = () => {
  const { id } = useParams();
  const [dataset, setDataset] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDataset = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/datasets`);
        setDataset(response.data);
      } catch (err) {
        console.error(err);
        setError("Erreur lors du chargement des données ou dataset non trouvé.");
      }
    };

    fetchDataset();
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!dataset) return <p>Chargement...</p>;

  return (
    <div>
      <h2>Détails du dataset</h2>
      <ul>
        <li><strong>ID :</strong> {dataset.id}</li>
        <li><strong>Titre :</strong> {dataset.title}</li>
        <li><strong>Description :</strong> {dataset.description || "Pas de description"}</li>
        <li><strong>Lien :</strong> <a href={dataset.url} target="_blank" rel="noopener noreferrer">Accéder au dataset</a></li>
      </ul>
    </div>
  );
};

export default Details;
