// //import { useState } from 'react'
// //import reactLogo from './assets/react.svg'
// //import viteLogo from '/vite.svg'
// import './App.css'
// import { BrowserRouter, Routes, Route } from 'react-router-dom';
// import Header from './components/Header'
// import Details from './pages/Details'

// function App() {
  

//   return (
//     <>
//     <BrowserRouter>
//       <Header />
//       <main style={{ marginTop: '80px', padding: '20px' }}>
//         <Routes>
//           <Route path="/details" element={<Details />} />
//         </Routes>
//       </main>
//     </BrowserRouter>
        
//     </>
//   )
// }

// export default App

import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import { useState } from 'react';
import data from './data.json';
import Header from './components/Header';
import Details from './pages/Details';

function App() {
  const [searchTerm, setSearchTerm] = useState('');

  // Fonction pour filtrer les données
  const filteredData = data.filter(person =>
    `${person.nom} ${person.prenom}`.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <BrowserRouter>
      <Header />
      <main style={{ marginTop: '80px', padding: '20px' }}>
        <Routes>
          <Route 
            path="/" 
            element={
              <div style={{ 
                display: 'flex', 
                flexDirection: 'column',
                alignItems: 'center', 
                height: 'calc(100vh - 80px)' 
              }}>
                <h2>Liste des personnes</h2>

                {/* Champ de recherche */}
                <input
                  type="text"
                  placeholder="Rechercher par nom ou prénom"
                  value={searchTerm}
                  onChange={e => setSearchTerm(e.target.value)}
                  style={{
                    marginBottom: '20px',
                    padding: '8px',
                    fontSize: '16px',
                    width: '300px'
                  }}
                />

                <table style={{ borderCollapse: 'collapse', width: '50%' }}>
                  <thead>
                    <tr>
                      <th style={{ border: '1px solid black', padding: '10px' }}>Nom</th>
                      <th style={{ border: '1px solid black', padding: '10px' }}>Prenom</th>
                      <th style={{ border: '1px solid black', padding: '10px' }}>Voir détails</th>
                    </tr>
                  </thead>
                  <tbody>
                    {filteredData.map(person => (
                      <tr key={person.id}>
                        <td style={{ border: '1px solid black', padding: '10px', textAlign: 'center' }}>
                          {person.nom}
                        </td>
                        <td style={{ border: '1px solid black', padding: '10px', textAlign: 'center' }}>
                          {person.prenom}
                        </td>
                        <td style={{ border: '1px solid black', padding: '10px', textAlign: 'center' }}>
                          <Link to={`/details/${person.id}`}>Voir détails</Link>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            } 
          />
          <Route path="/details/:id" element={<Details />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
