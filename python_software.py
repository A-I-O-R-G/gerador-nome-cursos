from flask import Flask, render_template, request
import random
import nltk

# Baixar os recursos necessários do NLTK (se ainda não baixados)
# nltk.download('punkt') # Descomente esta linha se executar pela primeira vez

app = Flask(__name__)

# Função para gerar sugestões de nomes para cursos
def generate_course_names(theme_or_description):
    # Aqui você pode implementar uma lógica mais complexa com NLP se desejar
    base_names = [
        'Introdução a', 
        'Avançado em', 
        'Fundamentos de', 
        'Explorando', 
        'Criando', 
        'Dominando', 
        'O Melhor de', 
        'Técnicas de', 
        'Estratégias para'
    ]
    
    # Dividindo a descrição em palavras para basear as sugestões
    words = nltk.word_tokenize(theme_or_description)
    suggestions = [f'{random.choice(base_names)} {' '.join(words)}' for _ in range(5)]
    return suggestions

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = []
    if request.method == 'POST':
        theme_or_description = request.form['theme_or_description']
        suggestions = generate_course_names(theme_or_description)
    return render_template('index.html', suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)
