
import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';

const App = () => {
    return (
        <div>
            <Header />
            <main>
                <h1>React + Flask SSR</h1>
                <p>This is a server-side rendered React app served by Flask.</p>
            </main>
            <Footer />
        </div>
    );
};

export default App;
