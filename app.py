import streamlit as st

# Configurações da página (ícone e título na aba do navegador)
st.set_page_config(page_title="Calculadora de Notas", page_icon="🎓")

# Título principal e uma linha divisória
st.title("🎓 Calculadora de Média - Univesp")
st.markdown("---")

# Usando colunas para as notas ficarem lado a lado
col1, col2 = st.columns(2)

with col1:
    n1 = st.number_input("Nota N1 (Peso 40%)", min_value=0.0, max_value=10.0, step=0.1)

with col2:
    n2 = st.number_input("Nota N2 (Peso 60%)", min_value=0.0, max_value=10.0, step=0.1)

# Cálculo da média ponderada
media = (0.4 * n1) + (0.6 * n2)

st.markdown("---")

# Botão centralizado para calcular
if st.button("Verificar Resultado Final"):
    st.subheader(f"Sua média é: {media:.1f}")
    
    if media >= 5.0:
        st.success(f"🎉 **APROVADO!** Parabéns pelo desempenho.")
    else:
        st.error(f"📚 **REPROVADO.** Você precisa de pelo menos 5.0 para passar.")




