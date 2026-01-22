# 🚀 ETL com Python (Extract, Transform, Load) — Projeto de Portfólio

Este projeto demonstra um pipeline **ETL** usando **Python**, com foco em entender o fluxo de dados entre as etapas:
**Extração → Transformação → Carregamento**.

A fonte de dados aqui é um **CSV local**, servindo como alternativa quando uma API está indisponível.

---

## 🎯 Objetivo

- Construir um pipeline ETL simples e funcional
- Ler dados de entrada (CSV)
- Transformar os dados gerando mensagens personalizadas
- Salvar os resultados em um novo arquivo CSV
- Publicar no GitHub como projeto de portfólio

---

## 🧩 Fluxo ETL

### ✅ Extract (Extração)
Leitura do arquivo `data/input_users.csv`, contendo informações básicas dos usuários:

- `nome`
- `conta`
- `cartao`

### ✅ Transform (Transformação)
Criação de uma coluna `mensagem` com texto simples e personalizado:

> "Olá {nome}, temos uma oferta especial disponível para você!"

### ✅ Load (Carregamento)
Geração do arquivo `data/output_messages.csv` contendo:

- `nome`
- `mensagem`

---

## 📁 Estrutura do Projeto

```text
etl-python-portfolio/
├── data/
│   ├── input_users.csv
│   └── output_messages.csv
├── etl.py
├── requirements.txt
└── README.md
