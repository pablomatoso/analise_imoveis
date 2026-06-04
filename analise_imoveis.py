import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# Análise do Mercado Imobiliário
# Autor: Pablo Matoso Nunes
# ============================================

# Carregando os dados
df = pd.read_csv('dados_imoveis.csv')

# Calculando o preço por m²
df['preco_m2'] = df['preco'] / df['area_m2']

print("=" * 45)
print("    ANÁLISE DO MERCADO IMOBILIÁRIO")
print("=" * 45)

print(f"\nTotal de imóveis analisados: {len(df)}")
print(f"Bairros analisados: {df['bairro'].nunique()}")
print(f"Tipos: {', '.join(df['tipo'].unique())}")

# --- Estatísticas gerais ---
print("\n--- Estatísticas de Preço ---")
print(f"Preço médio:   R$ {df['preco'].mean():>12,.2f}")
print(f"Preço mínimo:  R$ {df['preco'].min():>12,.2f}")
print(f"Preço máximo:  R$ {df['preco'].max():>12,.2f}")

# --- Preço médio por tipo ---
print("\n--- Preço Médio por Tipo ---")
preco_tipo = df.groupby('tipo')['preco'].mean()
for tipo, preco in preco_tipo.items():
    print(f"{tipo}: R$ {preco:,.2f}")

# --- Preço médio por bairro ---
print("\n--- Preço Médio por Bairro (ordenado) ---")
preco_bairro = df.groupby('bairro')['preco'].mean().sort_values(ascending=False)
for bairro, preco in preco_bairro.items():
    print(f"{bairro}: R$ {preco:,.2f}")

# --- Preço médio por m² por bairro ---
print("\n--- Preço Médio por m² por Bairro ---")
preco_m2_bairro = df.groupby('bairro')['preco_m2'].mean().sort_values(ascending=False)
for bairro, valor in preco_m2_bairro.items():
    print(f"{bairro}: R$ {valor:,.2f}/m²")


# ============================================
# GRÁFICOS
# ============================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('Análise do Mercado Imobiliário', fontsize=14, fontweight='bold')

# Gráfico 1 - Preço médio por bairro
preco_bairro.plot(kind='bar', ax=axes[0], color='steelblue')
axes[0].set_title('Preço Médio por Bairro')
axes[0].set_xlabel('Bairro')
axes[0].set_ylabel('Preço (R$)')
axes[0].tick_params(axis='x', rotation=45)

# Gráfico 2 - Quantidade de imóveis por tipo
contagem_tipo = df['tipo'].value_counts()
contagem_tipo.plot(kind='bar', ax=axes[1], color=['steelblue', 'coral'])
axes[1].set_title('Imóveis por Tipo')
axes[1].set_xlabel('Tipo')
axes[1].set_ylabel('Quantidade')
axes[1].tick_params(axis='x', rotation=0)

# Gráfico 3 - Relação área x preço
for tipo in df['tipo'].unique():
    subset = df[df['tipo'] == tipo]
    axes[2].scatter(subset['area_m2'], subset['preco'], label=tipo, alpha=0.7)
axes[2].set_title('Área x Preço')
axes[2].set_xlabel('Área (m²)')
axes[2].set_ylabel('Preço (R$)')
axes[2].legend()

plt.tight_layout()
plt.savefig('graficos_imoveis.png', dpi=150)
plt.show()

print("\nAnálise concluída! Gráfico salvo como 'graficos_imoveis.png'")
