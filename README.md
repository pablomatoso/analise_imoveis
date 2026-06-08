# 📊 Análise do Mercado Imobiliário com Python!

> Simple real estate market analysis using Python, Pandas and Matplotlib.

## Sobre o Projeto

Este projeto realiza uma análise exploratória de dados do mercado imobiliário, com foco em:

- Comparação de preços médios por bairro
- Diferença de preços entre casas e apartamentos
- Preço médio por metro quadrado por região
- Relação entre área e valor do imóvel

A ideia surgiu da minha experiência como corretor e consultor imobiliário, onde lidar com precificação e análise de mercado faz parte da rotina. Quis trazer esse contexto para a prática com dados.

---

## Tecnologias Utilizadas

- Python 3
- Pandas
- Matplotlib

---

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/pablomatoso/analise-imoveis.git
cd analise-imoveis
```

2. Instale as dependências:
```bash
pip install pandas matplotlib
```

3. Execute o script:
```bash
python analise_imoveis.py
```

---

## Resultados

O script exibe no terminal as principais métricas e gera um arquivo `graficos_imoveis.png` com três visualizações:

- **Preço médio por bairro** — identifica as regiões mais valorizadas
- **Quantidade de imóveis por tipo** — distribuição entre casas e apartamentos
- **Relação área x preço** — mostra como o tamanho influencia o valor

### Exemplo de saída:

```
Total de imóveis analisados: 40
Bairros analisados: 8

Preço médio:   R$    322.825,00
Preço mínimo:  R$    110.000,00
Preço máximo:  R$    650.000,00

Preço Médio por Bairro:
Jardim América: R$ 445.833,33
Centro:         R$ 426.666,67
Bela Vista:     R$ 396.666,67
...
```

---

## Dataset

O arquivo `dados_imoveis.csv` contém 40 registros simulados com as seguintes colunas:

| Coluna | Descrição |
|---|---|
| tipo | Casa ou Apartamento |
| bairro | Localização do imóvel |
| area_m2 | Área em metros quadrados |
| quartos | Número de quartos |
| banheiros | Número de banheiros |
| vagas_garagem | Vagas de garagem |
| preco | Preço de venda em R$ |

---

## Autor

**Pablo Matoso Nunes**  
Graduado em Análise e Desenvolvimento de Sistemas | Analista de dados  
Em transição para a área de dados e tecnologia.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/pablo-nunes20)
