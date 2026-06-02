import streamlit as st

# Configura a página para o modo escuro/centralizado
st.set_page_config(page_title="Simulador de Negociação", page_icon="🏢", layout="centered")

# CSS para forçar o fundo escuro e tirar margens desnecessárias
st.markdown("""
    <style>
    .main { background-color: #111111; color: white; }
    h1, h2, h3, p, label { color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- 1. LOGO E TÍTULO ---
try:
    st.image("sua_logo.png", width=220)
except:
    st.markdown("<h1 style='text-align: center; color: #00BFFF;'>Fabiano Baú Creci 16.356</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>Simulador de Negociação</h2>", unsafe_allow_html=True)

# --- 2. PAINEL: DADOS DA UNIDADE E CLIENTE ---
st.markdown("### 🏢 Dados do Atendimento")
col_cli1, col_cli2 = st.columns(2)

with col_cli1:
    nome_cliente = st.text_input("Nome do Cliente", value="Ricardo")
    nome_empreendimento = st.text_input("Empreendimento", value="Visione")

with col_cli2:
    unidade = st.text_input("Unidade / Sala", value="11 Bloco C")
    preco_total = st.number_input("Preço Total (R$)", min_value=0.0, value=600000.0, step=10000.0)

# --- 3. PAINEL: CONFIGURAÇÃO DE PRAZOS ---
st.markdown("### 📅 Configuração de Prazos")
col_prz1, col_prz2 = st.columns(2)

with col_prz1:
    qtd_entrada = st.number_input("Nº Parc. Entrada", min_value=1, value=1)
    qtd_mensais = st.number_input("Nº Parc. Mensais", min_value=1, value=48)

with col_prz2:
    tipo_intercalada = st.selectbox("Tipo", ["Semestrais", "Anuais"])
    qtd_intercaladas = st.number_input("Nº Parc. Intercaladas", min_value=0, value=8)

# --- 4. PAINEL: DISTRIBUIÇÃO DO FLUXO (%) ---
st.markdown("### 📊 Distribuição do Fluxo (%)")
col_flx1, col_flx2, col_flx3, col_flx4 = st.columns(4)

with col_flx1:
    pct_entrada = st.number_input("Entrada (%)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
with col_flx2:
    pct_mensais = st.number_input("Mensais (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
with col_flx3:
    pct_intercaladas = st.number_input("Intercaladas (%)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)
with col_flx4:
    pct_entrega = st.number_input("Entrega (%)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

# Validação matemática do fechamento do fluxo
total_porcentagem = pct_entrada + pct_mensais + pct_intercaladas + pct_entrega

# Se a porcentagem estiver errada, exibe o aviso em VERMELHO
if total_porcentagem == 100.0:
    st.markdown(f"<p style='color: #00BFFF; font-weight: bold;'>✅ Fechamento do fluxo perfeito: {total_porcentagem}%</p>", unsafe_allow_html=True)
else:
    st.markdown(f"<p style='color: #FF0000; font-weight: bold;'>❌ Erro no fechamento: {total_porcentagem}% (Precisa somar exatamente 100%)</p>", unsafe_allow_html=True)

# --- 5. CÁLCULOS MATEMÁTICOS DOS VALORES ---
valor_entrada_total = preco_total * (pct_entrada / 100)
valor_mensais_total = preco_total * (pct_mensais / 100)
valor_intercaladas_total = preco_total * (pct_intercaladas / 100)
valor_entrega_total = preco_total * (pct_entrega / 100)

valor_un_entrada = valor_entrada_total / qtd_entrada if qtd_entrada > 0 else 0
valor_un_mensal = valor_mensais_total / qtd_mensais if qtd_mensais > 0 else 0
valor_un_intercalada = valor_intercaladas_total / qtd_intercaladas if qtd_intercaladas > 0 else 0

# --- 6. PAINEL: RESULTADO FINANCEIRO (CÓDIGO REESCRITO DO ZERO) ---
st.markdown("### 💰 Resultado Financeiro")
col_res1, col_res2 = st.columns(2)

def formata_real(val):
    return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

with col_res1:
    # Bloco Entrada
    st.markdown(f"**ENTRADA ({pct_entrada}%)**")
    st.markdown(f"<h3 style='color: #00BFFF; margin-top:0px; margin-bottom:0px;'>{formata_real(valor_entrada_total)}</h3>", unsafe_allow_html=True)
    st.markdown(f"Fluxo: {qtd_entrada}x de {formata_real(valor_un_entrada)}")
    st.markdown("---")
    
    # Bloco Intercaladas
    st.markdown(f"**{tipo_intercalada.upper()} ({pct_intercaladas}%)**")
    st.markdown(f"<h3 style='color: #00BFFF; margin-top:0px; margin-bottom:0px;'>{formata_real(valor_intercaladas_total)}</h3>", unsafe_allow_html=True)
    st.markdown(f"Fluxo: {qtd_intercaladas}x de {formata_real(valor_un_intercalada)}")

with col_res2:
    # Bloco Mensais
    st.markdown(f"**MENSAIS ({pct_mensais}%)**")
    st.markdown(f"<h3 style='color: #00BFFF; margin-top:0px; margin-bottom:0px;'>{formata_real(valor_mensais_total)}</h3>", unsafe_allow_html=True)
    st.markdown(f"Fluxo: {qtd_mensais}x de {formata_real(valor_un_mensal)}")
    st.markdown("---")
    
    # Bloco Chaves
    st.markdown(f"**ENTREGA / CHAVES ({pct_entrega}%)**")
    st.markdown(f"<h3 style='color: #00BFFF; margin-top:0px; margin-bottom:0px;'>{formata_real(valor_entrega_total)}</h3>", unsafe_allow_html=True)
    st.markdown("Parcela única na entrega das chaves")

# --- 7. GERADOR DE RELATÓRIO PARA WHATSAPP ---
st.markdown("<br>", unsafe_allow_html=True)
texto_relatorio = f"""*PROPOSTA COMERCIAL DE NEGOCIAÇÃO IMOBILIÁRIA*

🏢 *Empreendimento:* {nome_empreendimento}
🔑 *Unidade:* {unidade}
👤 *Cliente:* {nome_cliente}
💵 *Preço Total:* {formata_real(preco_total)}

*Fluxo de Pagamento Sugerido:*
• Entrada ({pct_entrada}%): {qtd_entrada}x de {formata_real(valor_un_entrada)} (Total: {formata_real(valor_entrada_total)})
• Mensais ({pct_mensais}%): {qtd_mensais}x de {formata_real(valor_un_mensal)} (Total: {formata_real(valor_mensais_total)})
• {tipo_intercalada} ({pct_intercaladas}%): {qtd_intercaladas}x de {formata_real(valor_un_intercalada)} (Total: {formata_real(valor_intercaladas_total)})
• Chaves ({pct_entrega}%): Parcela única de {formata_real(valor_entrega_total)}

_Proposta gerada para análise técnica e aprovação._"""

st.text_area("📋 Relatório pronto para copiar e enviar no WhatsApp:", texto_relatorio, height=240)
