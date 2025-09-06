# Projeto carrosF1

E de Fórmula 1.

## Tecnologias Utilizadas
- Python 3
- Django 5.2.5
- SQLite3 (banco de dados padrão)
- Pillow (para manipulação de imagens)

## Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd carrosF1
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Rode as migrações:
   ```bash
   .venv/bin/python manage.py migrate
   ```
5. Inicie o servidor:
   ```bash
   .venv/bin/python manage.py runserver
   ```

## Testes

Para garantir a qualidade e a estabilidade do código, o projeto conta com testes automatizados. Para executá-los, utilize o comando:

```bash
.venv/bin/python manage.py test
```

Os testes atuais (`carsF1/tests.py`) garantem o funcionamento correto da lógica de atualização do inventário de carros (`CarInventory`) através dos *signals*.

## Estrutura do Projeto
- `app/` - Configurações do projeto Django
- `carsF1/` - Aplicação principal com modelos, views, admin, etc.
- `db.sqlite3` - Banco de dados SQLite

---

> Este README será atualizado conforme o desenvolvimento do projeto, detalhando cada alteração e explicando as atividades realizadas.