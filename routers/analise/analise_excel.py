from . import analise_blueprint
import pandas as pd
import json

data = []
df = pd.read_excel('./planilhas/caixa-mensal-2023.xlsx', sheet_name=0)
for contador in range(25):
    d = f"{df['DATA'][contador]}"
    data.append(d)

@analise_blueprint.route("/")
def index():
    return df.to_json()

@analise_blueprint.route("/entradas")
def entradas():
    colunas_entrada = ["CAIXA", "PIX", "CARTAO", "IFOOD"]

    def entrada_mes(colunas):
        total = 0
        soma_entradas = []
        lista_entradas = []

        for col in colunas:
            for contador in range(26):
                total += df.at[contador, col]
                contador += 1

            soma_entradas.append(total)
            total = 0

        for contador in range(soma_entradas.__len__()):
            lista_entradas.append({
                colunas[contador]: soma_entradas[contador]
            })

        return {
            "total_entrada_mes": lista_entradas
        }

    def entrada_dia(colunas, datas):
        linhas = 1
        dias = 1
        total = 0
        total_mensal = 0.00
        entradas_dia = []
        total_diario = []

        for contador in range(26):
            for col in colunas:
                if linhas > 25:
                    break

                total += df.at[linhas, col]

                if col == colunas[-1]:
                    entradas_dia.append(total)
                    total_mensal += total

                    total = 0
                    linhas += 1
                    dias += 1

        for contador in range(len(datas)):
            total_diario.append({
                datas[contador]: entradas_dia[contador]
            })

        return {
            "total_diario": total_diario,
            "total_mensal": total_mensal
        }

    response = [entrada_mes(colunas_entrada), entrada_dia(colunas_entrada, data)]

    return response

@analise_blueprint.route("/saidas")
def saidas():
    colunas_saida = ['DIZ', 'SALGADO', 'EMBALAGENS', 'AÇAI/MILK', 'FEIRA/PAD.', 'COMBUSTIVEL', 'MERCADO', 'PARTICULAR', 'OUTROS']

    def saida_mes(colunas):
        total = 0
        soma_saidas = []
        lista_saidas = []

        for col in colunas:
            for contador in range(25):
                total += float(df.at[contador, col])
                contador += 1
                json.dumps(total)

            soma_saidas.append(total)
            total = 0

        for contador in range(len(soma_saidas)):
            lista_saidas.append({
                colunas[contador]: soma_saidas[contador]
            })

        return {
            "total_saidas": lista_saidas
        }

    def saida_dia(colunas, datas):
        linhas = 0
        dias = 1
        total = 0
        total_mensal = 0.00
        saidas_dia = []
        saidas_total_diaria = []

        for contador in range(26):
            for col in colunas:
                if linhas > 25:
                    break

                total += df.at[linhas, col]

                if col == colunas[-1]:
                    saidas_dia.append(total)
                    total_mensal += total

                    total = 0
                    linhas += 1
                    dias += 1

        for contador in range(len(datas)):
            saidas_total_diaria.append({
                datas[contador]: saidas_dia[contador]
            })

        return {
            "total_diario": saidas_total_diaria,
            "total_mensal": total_mensal
        }

    response = [saida_mes(colunas_saida), saida_dia(colunas_saida, data)]

    return response
