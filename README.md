# Calculadora de Conversão de Bases Numéricas

Projeto de uma calculadora web desenvolvida em **Python com Flask**, capaz de realizar conversões entre diferentes bases numéricas.

A aplicação possui uma interface web simples e permite que o usuário informe um número, escolha sua base de origem e selecione a base para a qual deseja realizar a conversão.

## Funcionalidades

A calculadora permite realizar conversões entre:

- Binário (Base 2)
- Octal (Base 8)
- Decimal (Base 10)
- Hexadecimal (Base 16)

Também possui tratamento para entradas inválidas, exibindo uma mensagem de erro quando o número informado não pertence à base selecionada.

## Tecnologias utilizadas

O projeto foi desenvolvido utilizando:

- Python
- Flask
- HTML5
- CSS3
- Jinja

## Estrutura do projeto

```text
Projeto-de-calculadora-de-conversao-binaria/
│
├── app.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── Documentacao_Calculadora_Conversao_Bases.pdf
│
└── README.md
```

### app.py

Arquivo principal da aplicação.

É responsável por:

- Inicializar o servidor Flask;
- Receber os dados enviados pelo formulário;
- Identificar a base de origem e a base de destino;
- Realizar as conversões;
- Tratar valores inválidos;
- Enviar o resultado novamente para a interface.

### templates/index.html

Responsável pela estrutura da interface web.

Contém o formulário utilizado para informar o número e selecionar as bases de origem e destino.

### static/style.css

Responsável pela aparência da aplicação, incluindo cores, espaçamentos, campos, botão e área de exibição do resultado.

### Documentação

O arquivo `Documentacao_Calculadora_Conversao_Bases.pdf` contém a documentação detalhada do projeto e a explicação dos principais trechos dos códigos utilizados.

## Como executar

Primeiramente, é necessário possuir o Python instalado.

Instale o Flask utilizando:

```bash
py -m pip install flask
```

Depois, na pasta do projeto, execute:

```bash
py app.py
```

O servidor Flask será iniciado localmente.

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Exemplo

Uma conversão de:

```text
Binário: 11111111
```

para hexadecimal produzirá:

```text
Hexadecimal: FF
```

## Funcionamento

O usuário informa um número pelo frontend e seleciona as bases de origem e destino.

O formulário envia os dados ao backend Flask através do método HTTP `POST`.

O Python transforma inicialmente o número para decimal e posteriormente realiza a conversão para a base selecionada.

O resultado é enviado novamente ao arquivo HTML e apresentado ao usuário.

## Autor

Projeto acadêmico desenvolvido por **Alexandre Henrique Freitas Ferreira Mendes**.

