# Diário de Evolução do Projeto carrosF1

Este arquivo registra, de forma detalhada, todas as etapas, decisões, aprendizados e alterações realizadas no projeto carrosF1.

---

## 27/07/2025
- Início do projeto Django.
- Criação do app `carsF1`.
- Configuração inicial do banco de dados SQLite.
- Adição do campo `ImageField` no modelo `Car` (instalação do Pillow).
- Configuração de `MEDIA_ROOT` e `MEDIA_URL` para upload de imagens.
- Criação da primeira view simples (`cars_view`) retornando HTML estático.
- Mapeamento da view no arquivo `urls.py`.
- Criação do arquivo `README.md` com instruções e histórico.

## 29/07/2025
- Criação do template `cars.html` para exibir informações dos carros.
- Início da integração entre views e templates.
- Ajuste do template para exibir o campo `model` do objeto `cars`.

---

> Este diário será atualizado sempre que houver mudanças, correções ou novas funcionalidades no projeto. Use este espaço para registrar decisões técnicas, problemas encontrados e soluções adotadas.
