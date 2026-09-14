from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


NOMES_BASES = {
    2: "Binário",
    8: "Octal",
    10: "Decimal",
    16: "Hexadecimal"
}


SIMBOLOS = "0123456789ABCDEF"


def formatar_numero(numero, base):

    sinal = "-" if numero < 0 else ""

    numero = abs(numero)

    if base == 2:
        resultado = bin(numero)[2:]

    elif base == 8:
        resultado = oct(numero)[2:]

    elif base == 10:
        resultado = str(numero)

    elif base == 16:
        resultado = hex(numero)[2:].upper()

    else:
        raise ValueError("Base não suportada.")

    return sinal + resultado


def valor_digito(caractere):

    caractere = caractere.upper()

    if caractere.isdigit():
        return int(caractere)

    return ord(caractere) - ord("A") + 10


def explicar_para_decimal(valor, base_origem):

    valor_sem_sinal = valor.lstrip("-").upper()

    # Se já estiver em decimal, não é necessário fazer expansão
    if base_origem == 10:

        return [
            f"O número já está na base decimal.",
            f"Valor decimal: {valor}"
        ]

    linhas = []

    linhas.append(
        f"1) Convertendo {valor} da base {base_origem} para decimal:"
    )

    linhas.append("")

    parcelas = []

    tamanho = len(valor_sem_sinal)

    for indice, caractere in enumerate(valor_sem_sinal):

        digito = valor_digito(caractere)

        expoente = tamanho - indice - 1

        resultado = digito * (base_origem ** expoente)

        linhas.append(
            f"{caractere} × {base_origem}^{expoente} = {resultado}"
        )

        parcelas.append(resultado)

    linhas.append("")

    expressao = " + ".join(str(x) for x in parcelas)

    total = sum(parcelas)

    linhas.append(
        f"{expressao} = {total}"
    )

    if valor.startswith("-"):
        linhas.append("")
        linhas.append(
            f"Como o número original é negativo: -{total}"
        )

    return linhas


def explicar_decimal_para_base(numero_decimal, base_destino):

    if base_destino == 10:

        return [
            "2) Como a base de destino é decimal, "
            "não é necessária uma nova conversão."
        ]

    linhas = []

    linhas.append(
        f"2) Convertendo {abs(numero_decimal)} "
        f"de decimal para base {base_destino}:"
    )

    linhas.append("")

    numero = abs(numero_decimal)

    if numero == 0:

        linhas.append("0 representa 0 em qualquer base.")

        return linhas

    restos = []

    atual = numero

    while atual > 0:

        quociente = atual // base_destino

        resto = atual % base_destino

        simbolo = SIMBOLOS[resto]

        linhas.append(
            f"{atual} ÷ {base_destino} = "
            f"{quociente}, resto {resto}"
            + (
                f" ({simbolo})"
                if resto >= 10
                else ""
            )
        )

        restos.append(simbolo)

        atual = quociente

    linhas.append("")

    linhas.append(
        "Lendo os restos de baixo para cima:"
    )

    resultado = "".join(reversed(restos))

    if numero_decimal < 0:
        resultado = "-" + resultado

    linhas.append(resultado)

    return linhas


def criar_explicacao(
    valor,
    base_origem,
    base_destino,
    numero_decimal,
    resultado
):

    linhas = []

    linhas.extend(
        explicar_para_decimal(
            valor,
            base_origem
        )
    )

    linhas.append("")
    linhas.append("")

    linhas.extend(
        explicar_decimal_para_base(
            numero_decimal,
            base_destino
        )
    )

    linhas.append("")
    linhas.append("")

    linhas.append(
        f"Resultado final: {resultado} "
        f"(base {base_destino})"
    )

    return "\n".join(linhas)


def realizar_conversao(
    valor,
    base_origem,
    base_destino
):

    valor = valor.strip()

    if not valor:
        raise ValueError("Digite um número.")

    # Converte o valor informado para decimal
    numero_decimal = int(
        valor,
        base_origem
    )

    # Resultado principal
    resultado = formatar_numero(
        numero_decimal,
        base_destino
    )

    # Todas as representações
    representacoes = {

        "binario":
            formatar_numero(
                numero_decimal,
                2
            ),

        "octal":
            formatar_numero(
                numero_decimal,
                8
            ),

        "decimal":
            formatar_numero(
                numero_decimal,
                10
            ),

        "hexadecimal":
            formatar_numero(
                numero_decimal,
                16
            )
    }

    # Quantidade mínima de bits
    bits = abs(
        numero_decimal
    ).bit_length()

    if bits == 0:
        bits = 1

    # Explicação matemática
    explicacao = criar_explicacao(
        valor,
        base_origem,
        base_destino,
        numero_decimal,
        resultado
    )

    return {

        "resultado": resultado,

        "representacoes":
            representacoes,

        "bits": bits,

        "explicacao":
            explicacao,

        "base_origem_nome":
            NOMES_BASES[
                base_origem
            ],

        "base_destino_nome":
            NOMES_BASES[
                base_destino
            ]
    }


@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route(
    "/converter",
    methods=["POST"]
)
def converter():

    dados = request.get_json()

    try:

        valor = dados.get(
            "valor",
            ""
        )

        base_origem = int(
            dados.get(
                "base_origem"
            )
        )

        base_destino = int(
            dados.get(
                "base_destino"
            )
        )

        dados_resultado = realizar_conversao(
            valor,
            base_origem,
            base_destino
        )

        return jsonify({

            "sucesso": True,

            **dados_resultado
        })

    except ValueError:

        return jsonify({

            "sucesso": False,

            "erro":
                "O número informado não é válido "
                "para a base selecionada."
        })


if __name__ == "__main__":

    app.run(debug=True)