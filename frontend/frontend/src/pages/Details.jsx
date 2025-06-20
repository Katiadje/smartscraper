// import React from 'react';

// const Details = () => {
//   return (
//     <>
//     <h1>Page details </h1>
//     </>
//   )
// };
// export default Details;


import { useParams } from 'react-router-dom';
import data from '../data.json';

const Details = () => {
  const { id } = useParams();
  const person = data.find(p => p.id === parseInt(id));

  if (!person) return <p>Personne non trouvée.</p>;

  return (
    <div>
      <h2>Détails de {person.nom} {person.prenom}</h2>
      <ul>
        <li><strong>Nom :</strong> {person.nom}</li>
        <li><strong>Prénom :</strong> {person.prenom}</li>
        <li><strong>Âge :</strong> {person.age}</li>
        <li><strong>Fonction :</strong> {person.fonction}</li>
      </ul>
    </div>
  );
};

export default Details;

