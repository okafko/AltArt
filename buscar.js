const dados = [
    { id: 1, titulo: "Introdução ao HTML", conteudo: "HTML é a base de qualquer site." },
    { id: 2, titulo: "CSS Avançado", conteudo: "Estilize sua página com CSS." },
    { id: 3, titulo: "JavaScript Básico", conteudo: "Aprenda lógica de programação com JS." },
    { id: 4, titulo: "Node.js para Backend", conteudo: "Use JavaScript no lado do servidor." },
];

function buscar() {
    const query = document.getElementById('search').value.toLowerCase();
    const resultados = dados.filter(item =>
        item.titulo.toLowerCase().includes(query) || item.conteudo.toLowerCase().includes(query)
    );

    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    if (resultados.length > 0) {
        resultados.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.titulo} - ${item.conteudo}`;
            resultsContainer.appendChild(li);
        });
    } else {
        resultsContainer.innerHTML = '<li>Nenhum resultado encontrado</li>';
    }
}
