import streamlit as st

# Configuração da aba do navegador
st.set_page_config(page_title="Calculadora Univesp", page_icon="🎓")

st.title("🎓 Calculadora de Média Ponderada")
st.markdown("---")

# Entradas organizadas
n1 = st.number_input("Nota N1 (Peso 0.4)", min_value=0.0, max_value=10.0, step=0.1)
n2 = st.number_input("Nota N2 (Peso 0.6)", min_value=0.0, max_value=10.0, step=0.1)

media = (0.4 * n1) + (0.6 * n2)

st.markdown("---")

if st.button("Calcular Resultado"):
    st.subheader(f"Média Final: {media:.1f}")
    
    if media >= 5.0:
        st.success("✅ **APROVADO!** Parabéns pelo seu esforço!")
    else:
        st.error("❌ **REPROVADO.** Não desanime, continue estudando!")



