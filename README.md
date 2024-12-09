 CursosCheck 📚

**CursosCheck** é um app desenvolvido com **FastAPI** para gerenciar um checklist de cursos. Com ele, você pode criar, listar, atualizar e deletar cursos, categorias e aulas.

---

### Desenvolvedor:
**Weslem Rodrigues**

### Curso:
**Arquitetura de Sistemas**

### Professor:
**Gabriel Tavares**

---

## Endpoints 🌐

### 1. **Listar Cursos** 📋
**GET** `/cursos`

Listar cursos.
**Response:**
```json
  "curso" : {
    [...],
    [...]
  }
```

### 2. Criar Curso
**POST** `/cursos`
Cria um novo curso.
**Response:**
```json
  "curso" : {
    [...]
  }
```

### 3. Listar um Curso
**GET** `/cursos/{curso_id}`
Listar curso por id.
**Response:**
```json
  "curso" : {
    [...]
  }
```

### 4. Atualizar Curso
**PUT** `/cursos/{curso_id}`
Atualiza os dados de um curso existente.
**Response:**
```json
  "curso" : {
    [...]
  }
```

### 5. Deletar Curso
**DELETE** `/cursos/{curso_id}`
Remove um curso específico.
**Response:**
```json
  "curso" : {
    [...]
  }
```

### 6. Listar Categorias do Curso
**GET** `/cursos/{curso_id}/categorias`
Retorna as categorias de um curso específico.
**Response:**
```json
  "categorias" : {
    [...],
    [...]
  }
```

### 7. Adicionar Aula
**POST** `/cursos/{curso_id}/categorias/{categoria_nome}/aulas`
Adiciona uma nova aula a uma categoria específica.
**Response:**
```json
  "aula" : {
    [...]
  }
```

### 8. Listar Aulas de um Curso
**GET** `/cursos/{curso_id}/aulas`
Retorna todas as aulas de um curso específico.
**Response:**
```json
  "aulas" : {
    [...],
    [...]
  }
```

### 9. Atualizar Aula do Curso
**PUT** `/cursos/{curso_id}/categorias/{categoria_nome}/aulas/{aula_id}`
Atualiza os dados de uma aula específica.
**Response:**
```json
  "aula" : {
    [...]
  }
```

## 10. Deletar Aula
**DELETE** `/cursos/{curso_id}/categorias/{categoria_nome}/aulas/{aula_id}`
Remove uma aula específica de um curso.
**Response:**
```json
  "aula" : {
    [...]
  }
```

## Como Executar 🚀

### Pré-requisitos

Antes de rodar o projeto, é necessário ter os seguintes pré-requisitos:

- 🐍 **Python 3.9** ou superior instalado.
- 📦 Instalar as dependências do projeto.

### Passos

1. **Clone o repositório**:
   Se você ainda não tem o projeto, clone-o para sua máquina local com o seguinte comando:
   ```bash
   git clone https://github.com/wes-lem/CursosCheck.git
   cd nome-do-repositorio
   ```
