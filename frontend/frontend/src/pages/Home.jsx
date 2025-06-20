import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [datasets, setDatasets] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchDatasets = async () => {
      try {
        const response = await axios.get('http://localhost:5000/datasets');
        setDatasets(response.data);
      } catch (err) {
        console.error(err);
        setError("Erreur lors du chargement des datasets.");
      }
    };

    fetchDatasets();
  }, []);

  if (error) return <p>{error}</p>;
  if (!datasets.length) return <p>Chargement...</p>;

  return (
    <div>
      <h1>Liste des Datasets</h1>
      <ul>
        {datasets.map(ds => (
          <li key={ds.id}>
            <Link to={`/datasets/${ds.id}`}>
              <strong>{ds.title || "Sans titre"}</strong>
            </Link>
            <p>{ds.description?.slice(0, 100) || "Pas de description"}...</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
