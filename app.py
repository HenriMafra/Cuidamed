import json
import os
import requests
import streamlit as st

ARQUIVO = "medicamentos.json"

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def buscar_openfda(nome):
    try:
        url = "https://api.fda.gov/drug/label.json"
        r = requests.get(url, params={"search": f'openfda.brand_name:"{nome}"', "limit": 1}, timeout=5)
        if r.status_code == 200:
            resultados = r.json().get("results", [])
            if resultados:
                res = resultados[0]
                openfda = res.get("openfda", {})
                return {
                    "nomes_genericos": openfda.get("generic_name", ["Não informado"]),
                    "fabricante": openfda.get("manufacturer_name", ["Não informado"]),
                    "via": openfda.get("route", ["Não informado"]),
                    "indicacoes": res.get("indications_and_usage", ["Não disponível"]),
                    "advertencias": res.get("warnings", ["Não disponível"]),
                }
        return None
    except Exception as e:
        return {"erro": str(e)}

st.set_page_config(page_title="CuidaMed", page_icon="💊", layout="centered")
st.title("💊 CuidaMed")
st.caption("Gerenciador de horários de medicamentos")

medicamentos = carregar()
aba = st.tabs(["Medicamentos", "Adicionar", "Buscar", "Consultar API"])

with aba[0]:
    st.subheader("Medicamentos cadastrados")
    if not medicamentos:
        st.info("Nenhum medicamento cadastrado ainda.")
    else:
        for m in medicamentos:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            col1.write(f"**{m['nome']}**")
            col2.write(m["horario"])
            col3.write(f"{m['doses_por_dia']}x por dia")
            if col4.button("🗑️", key=f"rem_{m['nome']}"):
                medicamentos = [x for x in medicamentos if x["nome"] != m["nome"]]
                salvar(medicamentos)
                st.rerun()

with aba[1]:
    st.subheader("Adicionar medicamento")
    with st.form("form_adicionar"):
        nome = st.text_input("Nome do medicamento")
        horario = st.text_input("Horário (ex: 08:00)")
        doses = st.number_input("Doses por dia", min_value=1, max_value=10, value=1)
        enviado = st.form_submit_button("Adicionar")
    if enviado:
        if nome and horario:
            medicamentos.append({"nome": nome, "horario": horario, "doses_por_dia": int(doses)})
            salvar(medicamentos)
            st.success(f"'{nome}' adicionado com sucesso!")
        else:
            st.error("Preencha o nome e o horário.")

with aba[2]:
    st.subheader("Buscar medicamento")
    termo = st.text_input("Digite o nome ou parte do nome")
    if termo:
        encontrados = [m for m in medicamentos if termo.lower() in m["nome"].lower()]
        if encontrados:
            for m in encontrados:
                st.write(f"**{m['nome']}** — {m['horario']} — {m['doses_por_dia']}x/dia")
        else:
            st.warning("Nenhum medicamento encontrado.")

with aba[3]:
    st.subheader("Consultar informações (OpenFDA)")
    st.caption("Busca informações na base pública da FDA (nomes em inglês).")
    nome_api = st.text_input("Nome do medicamento (ex: Aspirin, Ibuprofen)")
    if st.button("Consultar"):
        if nome_api:
            with st.spinner("Consultando OpenFDA..."):
                info = buscar_openfda(nome_api)
            if info and "erro" not in info:
                st.success("Informações encontradas!")
                col_a, col_b = st.columns(2)
                col_a.metric("Nome genérico", ", ".join(info["nomes_genericos"]))
                col_b.metric("Via", ", ".join(info["via"]))
                st.write(f"**Fabricante:** {', '.join(info['fabricante'])}")
                with st.expander("Indicações"):
                    st.write(info["indicacoes"][0])
                with st.expander("Advertências"):
                    st.write(info["advertencias"][0])
            elif info and "erro" in info:
                st.error(info["erro"])
            else:
                st.warning("Nenhuma informação encontrada.")
        else:
            st.error("Digite o nome de um medicamento.")
