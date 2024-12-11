from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


# Modelo de resposta padrão
class ResponseModel(BaseModel):
    status: str
    message: str
    data: list


# Modelo para a Aula
class Aula(BaseModel):
    id: int
    titulo: str
    descricao: str


# Modelo para a Categoria
class Categoria(BaseModel):
    nome: str
    aulas: List[Aula]


# Modelo para o Curso
class Curso(BaseModel):
    id: int
    titulo: str
    descricao: str
    professor: str
    plataforma: str
    categorias: List[Categoria]


# Lista de cursos (Banco de Dados em Memória)
cursos = [
    Curso(
        id=1,
        titulo="Curso de Python",
        descricao="Aprenda Python do zero!",
        professor="Renato William",
        plataforma="Udemy",
        categorias=[
            Categoria(
                nome="Introdução",
                aulas=[
                    Aula(
                        id=1,
                        titulo="Boas-vindas",
                        descricao="Introdução ao curso",
                    ),
                    Aula(
                        id=2,
                        titulo="Configurando o ambiente",
                        descricao="Como configurar o ambiente para Python no Visual Studio Code",
                    ),
                ],
            ),
            Categoria(
                nome="Avançado",
                aulas=[
                    Aula(
                        id=3,
                        titulo="Otimização de código",
                        descricao="Melhores práticas para otimização",
                    ),
                    Aula(
                        id=4,
                        titulo="Multithreading",
                        descricao="Como utilizar multithreading em Python",
                    ),
                ],
            ),
        ],
    ),
    Curso(
        id=2,
        titulo="Curso de FastAPI",
        descricao="Desenvolva APIs com FastAPI",
        professor="Gabriel Tavares",
        plataforma="Youtube",
        categorias=[
            Categoria(
                nome="Fundamentos",
                aulas=[
                    Aula(
                        id=5,
                        titulo="Instalação do FastAPI",
                        descricao="Como instalar o FastAPI e suas dependências",
                    ),
                    Aula(
                        id=6,
                        titulo="Criando a primeira API",
                        descricao="Desenvolvendo sua primeira API com FastAPI",
                    ),
                ],
            ),
            Categoria(
                nome="Avançado",
                aulas=[
                    Aula(
                        id=7,
                        titulo="Criando rotas CRUD",
                        descricao="Criação de rotas CRUD em sua API",
                    ),
                    Aula(
                        id=8,
                        titulo="Integração Banco de Dados",
                        descricao="Sua API com banco SQLAlchemy",
                    ),
                ],
            ),
        ],
    ),
]


# 1. Listar todos os cursos
@app.get("/cursos", response_model=ResponseModel)
async def listar_cursos():
    return ResponseModel(
        status="success",
        message="Cursos listados com sucesso.",
        data=cursos,
    )


# 2. Buscar curso por ID
@app.get("/cursos/{curso_id}", response_model=ResponseModel)
async def obter_curso(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            return ResponseModel(
                status="success",
                message="Curso encontrado.",
                data=[curso],
            )
    raise HTTPException(status_code=404, detail="Curso não encontrado")


# 3. Adicionar novo curso
@app.post("/cursos", response_model=ResponseModel)
async def criar_curso(curso: Curso):
    cursos.append(curso)
    return ResponseModel(
        status="success",
        message="Curso cadastrado com sucesso.",
        data=[curso],
    )


# 4. Atualizar curso por ID
@app.put("/cursos/{curso_id}", response_model=ResponseModel)
async def atualizar_curso(curso_id: int, curso: Curso):
    for i, c in enumerate(cursos):
        if c.id == curso_id:
            cursos[i] = curso
            return ResponseModel(
                status="success",
                message="Curso atualizado com sucesso.",
                data=[curso],
            )
    raise HTTPException(status_code=404, detail="Curso não encontrado")


# 5. Deletar curso por ID
@app.delete("/cursos/{curso_id}", response_model=ResponseModel)
async def deletar_curso(curso_id: int):
    for i, c in enumerate(cursos):
        if c.id == curso_id:
            del cursos[i]
            return ResponseModel(
                status="success",
                message="Curso deletado com sucesso.",
                data=[c],
            )
    raise HTTPException(status_code=404, detail="Curso não encontrado")


# 6. Listar categorias de um curso específico
@app.get("/cursos/{curso_id}/categorias", response_model=ResponseModel)
async def listar_categorias(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            return ResponseModel(
                status="success",
                message="Categorias encontradas.",
                data=curso.categorias,
            )
    raise HTTPException(status_code=404, detail="Curso não encontrado")


# 7. Adicionar uma nova aula a uma categoria de um curso específico
@app.post(
    "/cursos/{curso_id}/categorias/{categoria_nome}/aulas",
    response_model=ResponseModel,
)
async def adicionar_aula(curso_id: int, categoria_nome: str, aula: Aula):
    for curso in cursos:
        if curso.id == curso_id:
            for categoria in curso.categorias:
                if categoria.nome == categoria_nome:
                    categoria.aulas.append(aula)
                    return ResponseModel(
                        status="success",
                        message="Aula adicionada com sucesso.",
                        data=[aula],
                    )
    raise HTTPException(
        status_code=404, detail="Curso ou categoria não encontrados"
    )


# 8. Listar todas as aulas de um curso
@app.get("/cursos/{curso_id}/aulas", response_model=ResponseModel)
async def listar_aulas_do_curso(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            aulas = [
                aula
                for categoria in curso.categorias
                for aula in categoria.aulas
            ]
            return ResponseModel(
                status="success",
                message="Aulas encontradas.",
                data=aulas,
            )
    raise HTTPException(status_code=404, detail="Curso não encontrado")


# 9. Atualizar aula de um curso
@app.put(
    "/cursos/{curso_id}/categorias/{categoria_nome}/aulas/{aula_id}",
    response_model=ResponseModel,
)
async def atualizar_aula(
    curso_id: int, categoria_nome: str, aula_id: int, aula: Aula
):
    for curso in cursos:
        if curso.id == curso_id:
            for categoria in curso.categorias:
                if categoria.nome == categoria_nome:
                    for i, a in enumerate(categoria.aulas):
                        if a.id == aula_id:
                            categoria.aulas[i] = aula
                            return ResponseModel(
                                status="success",
                                message="Aula atualizada com sucesso.",
                                data=[aula],
                            )
    raise HTTPException(
        status_code=404, detail="Curso, categoria ou aula não encontrados"
    )


# 10. Deletar aula de um curso
@app.delete(
    "/cursos/{curso_id}/categorias/{categoria_nome}/aulas/{aula_id}",
    response_model=ResponseModel,
)
async def deletar_aula(curso_id: int, categoria_nome: str, aula_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            for categoria in curso.categorias:
                if categoria.nome == categoria_nome:
                    for i, a in enumerate(categoria.aulas):
                        if a.id == aula_id:
                            del categoria.aulas[i]
                            return ResponseModel(
                                status="success",
                                message="Aula deletada com sucesso.",
                                data=[a],
                            )
    raise HTTPException(
        status_code=404, detail="Curso, categoria ou aula não encontrados"
    )
