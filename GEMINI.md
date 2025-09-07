# Gemini - Guia do Projeto Django "carrosF1"

Este documento serve como um guia centralizado e fonte de contexto para o projeto, garantindo que o desenvolvimento assistido pela IA seja eficiente, seguro e alinhado com a estrutura atual.

## 1. Visão Geral do Projeto

O projeto é uma aplicação web construída com Django para gerenciar uma coleção de carros, possivelmente de Fórmula 1. Ele permite listar, visualizar detalhes, adicionar, editar e remover carros. O sistema também inclui autenticação de usuários e mantém um inventário agregado do valor e da quantidade de carros.

## 2. Dependências (`requirements.txt`)

-   **`Django==5.2.5`**: O framework principal do projeto.
-   **`Pillow==11.3.0`**: Utilizado para manipulação de imagens (upload de fotos dos carros).
-   **`asgiref` e `sqlparse`**: Dependências do Django.

## 3. Configurações Principais (`app/settings.py`)

-   **Apps Instalados**: O projeto é composto pelos apps `carsF1` (lógica principal) e `accounts` (autenticação), além dos apps padrão do Django.
-   **Banco de Dados**: Utiliza `SQLite` como banco de dados padrão.
-   **Mídia**: Arquivos de mídia (fotos dos carros) são salvos no diretório `/media/cars/`.
-   **Autenticação**:
    -   `LOGIN_URL`: `/accounts/login/`
    -   `LOGIN_REDIRECT_URL`: `/cars/` (após o login, o usuário é levado para a lista de carros).
    -   `LOGOUT_REDIRECT_URL`: `/accounts/login/`

## 4. Estrutura de Aplicações (Apps)

### 4.1. App `carsF1`

Responsável por toda a lógica de negócio relacionada aos carros.

-   **Modelos (`models.py`):**
    -   `Brand`: Representa a marca de um carro (ex: Ferrari, McLaren).
        -   `name`: `CharField`
    -   `Car`: O modelo principal, representando um carro.
        -   `model`: `CharField`
        -   `brand`: `ForeignKey` para o modelo `Brand`.
        -   `factory_year`, `model_year`: `IntegerField`
        -   `plate`: `CharField` (placa do carro).
        -   `value`: `FloatField` (valor do carro).
        -   `photo`: `ImageField` (foto do carro).
    -   `CarInventory`: Armazena dados agregados sobre o inventário.
        -   `cars_count`: `IntegerField` (quantidade total de carros).
        -   `cars_value`: `FloatField` (soma do valor de todos os carros).
        -   **Lógica de Negócio Importante**: Este modelo é atualizado automaticamente através de *signals* (`post_save`, `post_delete`) sempre que um `Car` é criado ou excluído, garantindo que o inventário esteja sempre sincronizado.

-   **Views (`views.py`):**
    -   Utiliza Class-Based Views (CBVs) e exige que o usuário esteja logado (`LoginRequiredMixin`).
    -   `CarsListView`: Lista todos os carros.
    -   `CarDetailView`: Mostra os detalhes de um carro específico.
    -   `NewCarCreateView`: Formulário para adicionar um novo carro.
    -   `CarUpdateView`: Formulário para editar um carro existente.
    -   `CarDeleteView`: Página de confirmação para deletar um carro.

-   **URLs (`urls.py`):**
    -   O app é acessado pela rota principal `/cars/`.
    -   Define as rotas para todas as views listadas acima (ex: `cars/<int:pk>/`, `cars/new/`, etc.).

### 4.2. App `accounts`

Responsável pela autenticação e gerenciamento de usuários.

-   **Modelos (`models.py`):**
    -   Não define modelos customizados, utilizando o sistema de usuários padrão do Django (`django.contrib.auth`).
-   **Views e Templates:**
    -   Fornece as páginas de `login.html` e `register.html`.

## 5. Ambiente e Comandos

-   **Ambiente Virtual**: Ative com `source .venv/bin/activate`.
-   **Instalar Dependências**: `pip install -r requirements.txt`.
-   **Executar Servidor**: `python manage.py runserver`.
-   **Migrações de BD**: `python manage.py makemigrations` e `python manage.py migrate`.
-   **Executar Testes**: `python manage.py test`.
-   **Qualidade de Código**: `black .` (formatação) e `ruff check .` (linting).

## 6. Interação e Geração de Código

Para garantir a qualidade e a segurança, todo novo código será gerado seguindo um processo de revisão e aprovação:
1.  **Análise Crítica:** O código será analisado quanto ao impacto e boas práticas.
2.  **Plano de Implementação:** Um plano detalhado será apresentado.
3.  **Aprovação do Usuário:** Nenhuma alteração será feita sem aprovação explícita de cada passo.

## 7. Padrões de Desenvolvimento

-   **Documentação Oficial do Django**: Todo o código e arquitetura desenvolvidos devem seguir estritamente as convenções e melhores práticas descritas na [documentação oficial do Django](https://docs.djangoproject.com/en/5.2/), utilizando a versão 5.2 ou superior como referência.
-   **Filosofias de Design**: É fundamental que o desenvolvimento também siga as **[Filosofias de Design do Django](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/)**, que guiam as decisões de arquitetura e o "jeito Django" de resolver problemas.

## 8. Diretrizes de Engenharia e Qualidade

Para garantir a longevidade, manutenibilidade e segurança do projeto, seguimos as seguintes diretrizes de engenharia.

### 8.1. Qualidade de Código e Estilo
- **Ferramentas Obrigatórias**: O código deve ser formatado com `black` e passar na verificação do `ruff check .` sem erros.
- **Automação (Sugestão)**: Recomenda-se o uso de `pre-commit hooks` para automatizar a verificação de estilo e qualidade antes de cada commit, garantindo que todo o código na base se mantenha consistente.

### 8.2. Estratégia de Testes
- **Testes Unitários**: Toda nova função, método de modelo ou lógica de negócio complexa (ex: signals) deve ter testes unitários correspondentes, focando em testar a lógica em isolamento.
- **Testes de Integração**: As views devem ter testes que verifiquem a integração completa (requisição-resposta), incluindo status HTTP, template renderizado e contexto.
- **Cobertura de Testes**: O objetivo é manter ou aumentar a cobertura de testes (`test coverage`) a cada nova adição de código.

### 8.3. Diretrizes de Frontend
- **Framework CSS**: O projeto utiliza **Bootstrap 5**. Aderir aos seus componentes e sistema de utilitários é mandatório para manter a consistência visual.
- **Componentização**: Elementos de UI reutilizáveis (como cards, botões, formulários) devem seguir o padrão estabelecido nos templates existentes. O `app/templates/base.html` é a fonte da verdade para a estrutura principal.
- **JavaScript**: O uso de JavaScript deve ser mínimo. Se for necessário, o código deve ser contido em arquivos estáticos separados e não inline nos templates.

### 8.4. Gestão de Configurações e Segredos
- **Padrão de Doze Fatores**: O projeto deve seguir os princípios do [The Twelve-Factor App](https://12factor.net/), especialmente na gestão de configurações.
- **Ferramenta Recomendada**: É mandatório o uso de uma biblioteca como a `django-environ` para carregar configurações e segredos (como `SECRET_KEY`, `DEBUG`) a partir de variáveis de ambiente ou de um arquivo `.env`. **Nenhum segredo deve estar hard-coded no código.**

### 8.5. Migrações de Banco de Dados
- **Fluxo Padrão**: Sempre utilize `python manage.py makemigrations` para gerar novos arquivos de migração.
- **Imutabilidade**: Uma vez que um arquivo de migração é comitado, ele não deve ser editado manualmente. Se uma alteração for necessária, crie uma nova migração.
- **Campos Não-Nulos**: Ao adicionar um novo campo `NOT NULL` a um modelo existente, forneça sempre um valor `default` para evitar que a migração falhe em produção.

### 8.6. Clareza na Execução de Comandos
- **Especificação do Ambiente**: Para cada comando a ser executado, será explicitamente indicado o ambiente correto:
    - **Terminal do Sistema**: Para comandos de sistema (ex: `sudo apt-get`, `git`, `docker`). A ativação do ambiente virtual é indiferente.
    - **Ambiente Virtual (`.venv`)**: Para comandos que dependem de pacotes Python do projeto (ex: `python manage.py ...`, `pip install ...`, `black .`). O ambiente deve estar ativado.

### 8.7. Princípio de Depuração: Simplicidade e Verificação Direta
Ao investigar um comportamento inesperado, deve-se priorizar os mecanismos de feedback mais simples e diretos disponíveis. Para depuração no console do Django (`runserver`), o uso de `print()` é mais confiável para saídas imediatas do que o módulo `logging`, que pode não estar configurado para exibir mensagens no console por padrão. Antes de concluir que uma função não é executada, é mandatório confirmar usando a forma mais básica de saída (`print()`) para evitar diagnósticos falsos baseados em suposições sobre a configuração do ambiente.
