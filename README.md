# Projeto CarrosF1

Uma aplicação web construída com Django para gerenciar uma coleção de carros. O sistema permite listar, visualizar, adicionar, editar e remover carros, além de contar com um sistema de inventário e geração de descrições automáticas com IA.

## ✨ Funcionalidades Principais

*   CRUD completo de Carros (Criar, Ler, Atualizar, Deletar).
*   Sistema de inventário que calcula o valor e a quantidade total de carros em tempo real.
*   **Geração de Bio com IA**: Descrições de marketing para os carros são geradas automaticamente usando a API do Google Gemini se não forem fornecidas pelo usuário.
*   Upload de fotos para cada carro.
*   Autenticação de usuários.

## 🚀 Tecnologias Utilizadas

*   Python 3
*   Django 5.2.5
*   **Google Generative AI**: Para geração de conteúdo com o modelo Gemini.
*   **Django Environ**: Para gerenciamento seguro de variáveis de ambiente.
*   Pillow: Para manipulação de imagens.
*   SQLite3: Banco de dados padrão para desenvolvimento.

## ⚙️ Como Rodar o Projeto Localmente

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd carrosF1
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente:**
    *   Crie um arquivo chamado `.env` na raiz do projeto.
    *   Adicione sua chave da API do Google Gemini a este arquivo, como no exemplo abaixo:
        ```
        GEMINI_API_KEY="SUA_CHAVE_API_VEM_AQUI"
        ```
    *   **Nota**: O arquivo `.env` já está no `.gitignore` para garantir que suas chaves não sejam enviadas para o repositório.

5.  **Rode as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

## 🧪 Testes

Para garantir a qualidade e a estabilidade do código, o projeto conta com testes automatizados. Para executá-los, utilize o comando:

```bash
python manage.py test
```

## 📂 Estrutura do Projeto

-   `app/`: Configurações do projeto Django.
-   `carsF1/`: Aplicação principal.
    -   `gemini_service.py`: Módulo de serviço para interação com a API Gemini.
    -   `signals.py`: Gatilhos para automação (geração de bio, atualização de inventário).
    -   `models.py`, `views.py`, `urls.py`, etc.
-   `.env`: Arquivo local para variáveis de ambiente (não versionado).
-   `db.sqlite3`: Banco de dados SQLite.

---

> Este README será atualizado conforme o desenvolvimento do projeto.
