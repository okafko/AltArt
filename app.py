from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def produto():
    # Informações do produto (pode vir de um banco de dados ou API no futuro)
    produto_info = {
        'nome': 'Produto Exemplo',
        'descricao': 'Este é um produto de exemplo para demonstrar a estrutura de uma página de produto.',
        'preco': 'R$ 199,99',
        'imagem': 'static/imagem_produto.jpg'  
    }
    return render_template('produto.html', produto=produto_info)

if __name__ == '__main__':
    app.run(debug=True)
