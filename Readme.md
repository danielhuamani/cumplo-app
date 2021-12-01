# Cumplo Challenge

My first idea is to move data of baxinco to the database for then do the queries and when  I have to call api of baxinco, first I verify in my database if exist data for that date range so I don't call api

## Installation

first create .env in directory compose/local/ and after copy variables of env.template and replace values

Compile docker image

```bash
make docker-local-build
```

Run the project

```bash
make docker-local-run
```

In other terminal run migrate

```bash
make docker-local-migrate
```
