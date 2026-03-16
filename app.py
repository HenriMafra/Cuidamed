import sys
import os
import streamlit as st

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), "src"))

from medicamentos import (
    carregar_medicamentos,
    salvar_medicamentos,
    adicionar_medicamento,
    listar_medicamentos,
    remover_medicamento,
    buscar_medicamento,
)
from api import buscar_info_medicamento, formatar_info

st.set_page_config(
    page_title="CuidaMed",
    page_icon="💊",
    layout="centered",
)

st.title("💊 CuidaMed")
st.caption("Gerenciador de horários de medicamentos")

medicamentos = carregar_medicamentos()

aba = st.tabs(["Medicamentos", "Adicionar", "Buscar", "Consultar API"])

# --- ABA 1: LISTAR ---
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
                medicamentos, _ = remover_medicamento(medicamentos, m["nome"])
                salvar_medicamentos(medicamentos)
                st.rerun()

# --- ABA 2: ADICIONAR ---
with aba[1]:
    st.subheader("Adicionar medicamento")
    with st.form("form_adicionar"):
        nome = st.text_input("Nome do medicamento")
        horario = st.text_input("Horário (ex: 08:00)")
        doses = st.number_input("Doses por dia", min_value=1, max_value=10, value=1)
        enviado = st.form_submit_button("Adicionar")

    if enviado:
        if nome and horario:
            medicamentos = adicionar_medicamento(medicamentos, nome, horario, int(doses))
            salvar_medicamentos(medicamentos)
            st.success(f"'{nome}' adicionado com sucesso!")
        else:
            st.error("Preencha o nome e o horário.")

# --- ABA 3: BUSCAR ---
with aba[2]:
    st.subheader("Buscar medicamento")
    termo = st.text_input("Digite o nome ou parte do nome")
    if termo:
        encontrados = buscar_medicamento(medicamentos, termo)
        if encontrados:
            for m in encontrados:
                st.write(f"**{m['nome']}** — {m['horario']} — {m['doses_por_dia']}x/dia")
        else:
            st.warning("Nenhum medicamento encontrado.")

# --- ABA 4: CONSULTAR API ---
with aba[3]:
    st.subheader("Consultar informações (OpenFDA)")
    st.caption("Busca informações sobre medicamentos na base de dados pública da FDA (em inglês).")
    nome_api = st.text_input("Nome do medicamento (em inglês, ex: Aspirin, Ibuprofen)")
    if st.button("Consultar"):
        if nome_api:
            with st.spinner("Consultando OpenFDA..."):
                info = buscar_info_medicamento(nome_api)
            if info and "erro" not in info:
                st.success("Informações encontradas!")
                col_a, col_b = st.columns(2)
                col_a.metric("Nome genérico", ", ".join(info.get("nomes_genericos", ["-"])))
                col_b.metric("Via", ", ".join(info.get("via_administracao", ["-"])))
                st.write(f"**Fabricante:** {', '.join(info.get('fabricante', ['-']))}")

                with st.expander("Indicações"):
                    indicacoes = info.get("indicacoes", ["Não disponível"])
                    st.write(indicacoes[0] if indicacoes else "Não disponível")

                with st.expander("Advertências"):
                    advertencias = info.get("advertencias", ["Não disponível"])
                    st.write(advertencias[0] if advertencias else "Não disponível")
            elif info and "erro" in info:
                st.error(info["erro"])
            else:
                st.warning(f"Nenhuma informação encontrada para '{nome_api}' na base OpenFDA.")
        else:
            st.error("Digite o nome de um medicamento.")
