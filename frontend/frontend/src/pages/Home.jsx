import { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Home = () => {
  const [datasets, setDatasets] = useState([]);
  const [error, setError] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

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

  const filteredDatasets = datasets.filter(dataset =>
    dataset.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
  dataset.description?.toLowerCase().includes(searchTerm.toLowerCase())

  );

  if (error) return <p>{error}</p>;
  if (!datasets.length) return <p>Chargement...</p>;

  return (
    <div style={{ padding: '20px' }}>
      <h1>Liste des Datasets</h1>

      <input
        type="text"
        placeholder="Rechercher par titre"
        value={searchTerm}
        onChange={e => setSearchTerm(e.target.value)}
        style={{
          marginBottom: '20px',
          padding: '10px',
          fontSize: '16px',
          width: '300px'
        }}
      />

      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f0f0f0' }}>
            <th style={{ border: '1px solid #ddd', padding: '10px' }}>Titre</th>
            <th style={{ border: '1px solid #ddd', padding: '10px' }}>Description</th>
            <th style={{ border: '1px solid #ddd', padding: '10px' }}>Lien</th>
          </tr>
        </thead>
        <tbody>
          {filteredDatasets.map(ds => (
            <tr key={ds.id}>
              <td style={{ border: '1px solid #ddd', padding: '10px' }}>
                <Link to={`/datasets/${ds.id}`}>{ds.title || "Sans titre"}</Link>
              </td>
              <td style={{ border: '1px solid #ddd', padding: '10px' }}>
                {ds.description?.slice(0, 100) || "Pas de description"}...
              </td>
              <td style={{ border: '1px solid #ddd', padding: '10px' }}>
                <a href={ds.url} target="_blank" rel="noopener noreferrer">Lien vers la source</a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Home;
