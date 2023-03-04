from flask import Flask
import pandas as pd

app = Flask(__name__)
df = pd.read_excel('./planilhas/caixa-mensal-2023.xlsx', sheet_name=0)

@app.route("/")
def index():
    return df

@app.route("/entradas")
def entradas():
    colunas_entrada = ["CAIXA", "PIX", "CARTAO", "IFOOD"]

    def entrada_mes(colunas):
        total = 0
        contador = 0
        total_entrada_mes = []

        for col in colunas:
            for contador in range(26):
                total += df.at[contador, col]
                contador += 1

            total_entrada_mes.append(round(total, 2))
            total = 0

        return {
            "total_entrada_mes": total_entrada_mes
        }

    def entrada_dia(colunas):
        linhas = 1
        dias = 1
        total = 1
        contador = 1
        total_mensal = 0.00
        total_diario = []

        for contador in range(26):
            for col in colunas:
                if linhas > 25:
                    break

                total += df.at[linhas, col]

                if col == colunas[-1]:
                    dia = {
                        dias: round(total, 2)
                    }

                    total_diario.append(dia)
                    total_mensal += total

                    total = 0
                    linhas += 1
                    dias += 1

        return {
            "total_diario": total_diario,
            "total_mensal": total_mensal
        }

    response = [entrada_mes(colunas_entrada), entrada_dia(colunas_entrada)]

    return response

@app.route("/saidas")
def saidas():
    colunas_saida = ["DIZ", "SALGADO", "EMBALAGENS", "AÇAI/MILK", "FEIRA/PAD.", "COMBUSTIVEL", "MERCADO", "PARTICULAR", "OUTROS"]

    def saida_mes(colunas):
        total = 0
        contador = 0
        total_saida_mes = []

        for col in colunas:
            for contador in range(26):
                total += df.at[contador, col]
                contador += 1

            total_saida_mes.append(float(round(total, 2)))
            total = 0

        return {
            "total_saida_mes": total_saida_mes
        }

    def saida_dia(colunas):
        linhas = 1
        dias = 1
        total = 1
        contador = 1
        total_mensal = 0.00
        total_diario = []

        for contador in range(26):
            for col in colunas:
                if linhas > 25:
                    break

                total += df.at[linhas, col]

                if col == colunas[-1]:
                    dia = {
                        dias: round(total, 2)
                    }

                    total_diario.append(dia)
                    total_mensal += total

                    total = 0
                    linhas += 1
                    dias += 1

        return {
            "total_diario": total_diario,
            "total_mensal": total_mensal
        }

    response = [saida_mes(colunas_saida), saida_dia(colunas_saida)]

    return response

if __name__ == '__main__':
    app.run(debug=True)
