# Instruções para rodar o Monopoly Simulator com Docker Compose

Este documento descreve como iniciar a aplicação Django (`monopoly_simulator`) usando Docker e Docker Compose.

---

## Pré-requisitos

- Docker instalado:
- Código fonte do projeto disponível localmente.

---

## Passos para rodar

1. **Navegue até a raiz do projeto** (onde está o arquivo `docker-compose.yml`)

2. **Execute o comando:** `docker-compose up --build`

3. **Faça um get para:** `http://localhost:8080/jogo/simular`

## Documentação

**Acesse `http://localhost:8080/api/swagger/` para ver o swagger da aplicação**
