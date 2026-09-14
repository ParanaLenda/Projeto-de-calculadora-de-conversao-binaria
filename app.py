from flask import Flask, render_template, request

app = Flask(__name__)

def converter_base(valor, base_origem, base_destino):
    numero_decimal = int(valor, base_origem)

    if base_destino == 2:
        return bin(numero_decimal)[2:]
    elif base_destino == 8:
        return oct(numero_decimal)[2:]
    elif base_destino == 10:
        return str(numero_decimal)
    elif base_destino == 16:
        return hex(numero_decimal)[2:].upper()


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    erro = ""

    if request.method == "POST":
        valor = request.form.get("valor")
        base_origem = int(request.form.get("base_origem"))
        base_destino = int(request.form.get("base_destino"))

        try:
            resultado = converter_base(
                valor,
                base_origem,
                base_destino
            )

        except ValueError:
            erro = "Valor inválido para a base selecionada."

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro
    )


if __name__ == "__main__":
    app.run(debug=True)