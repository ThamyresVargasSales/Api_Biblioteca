from fastapi import FastAPI

app = FastAPI(title="API da Biblioteca")

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "categoria": "Romance"},
    {"id": 2, "titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "categoria": "Infantil"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "ano": 1949, "categoria": "Ficção"},
    {"id": 4, "titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "categoria": "Romance"}
]

@app.get("/")
def inicio():
    return {"mensagem": "API da Biblioteca funcionando!"}

@app.get("/livros")
def listar_livros():
    return {"livros": livros}

@app.get("/livros/{id}")
def buscar_livro(id: int):
    for livro in livros:
        if livro["id"] == id:
            return livro
    return {"erro": "Livro não encontrado"}

@app.get("/autores")
def listar_autores():
    return {"autores": sorted(set(livro["autor"] for livro in livros))}

@app.get("/categorias")
def listar_categorias():
    return {"categorias": sorted(set(livro["categoria"] for livro in livros))}

@app.get("/busca/autor/{nome}")
def buscar_por_autor(nome: str):
    resultado = [livro for livro in livros if nome.lower() in livro["autor"].lower()]
    return {"livros": resultado}

@app.get("/exercicio/ano/{ano}")
def buscar_por_ano(ano: int):
    resultado = [livro for livro in livros if livro["ano"] == ano]
    return {"ano": ano, "livros": resultado}

