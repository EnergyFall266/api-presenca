# API Face Recognition

## Instalação

A versão de Python utilizada foi 3.12.

```bash
pip install dlib
```

Após isso para instalar as bibliotecas utilizadas, rode o comando:
```bash
pip install -r requirements.txt

```

## Utilização

Esta Api possui 1 porta ***POST***.
 - /verifica-presenca

### /verifica-presenca
Recebe uma lista de imagens e uma imagem avulsa, ambas em base64, para a comparação.

#### Entrada
```json
{
"data_single": "<string base64 da imagem>",
"data_list": ["<string base64 da imagem1>","<string base64 da imagem2>"]
}
```

#### Saída
Se a imagem enviada der *match* com alguma da lista ele retornará:
```json
{
"message": "presente"
}
```
Se não der *match*:
```json
{
"message": "nao esta presente"
}
```

### Execução
Para subir a API na rede local é só rodar no terminal, na pasta do projeto, o comando:
```bash
uvicorn main:app --reload
```
