import React from 'react';

const Header = () => {
  return (
    <header style={styles.header}>
      <h1 style={styles.title}>SmartScraper</h1>
      <nav style={styles.nav}>
        <a href="/" style={styles.link}>Accueil</a>
      </nav>
    </header>
  );
};

const styles = {
  header: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    width: '100%',
    height: '70px', // hauteur fixe du header
    backgroundColor: '#282c34',
    padding: '0 40px',
    color: 'white',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    zIndex: 1000,
    boxSizing: 'border-box',
  },
  title: {
    margin: 0,
    fontSize: '24px',
  },
  nav: {
    display: 'flex',
    gap: '30px',
  },
  link: {
    color: 'white',
    textDecoration: 'none',
    fontSize: '16px',
    padding: '8px 12px',
    transition: 'background-color 0.2s ease',
  }
};


export default Header;
