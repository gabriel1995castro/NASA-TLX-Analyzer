import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sb
import numpy as np
import os


plt.rcParams.update({'axes.titlesize': 14, 'axes.titleweight': 'bold'})

def get_palette(condicoes):
    cores_padrao = ['#1f77b4', '#d62728', '#2ca02c', '#9467bd', '#ff7f0e', '#8c564b']
    return dict(zip(condicoes, cores_padrao))


print("### NASA TLX ANALYZER ####")
caminho = input("Enter the path of the CSV file: ").strip()

if not os.path.exists(caminho):
    print("The specified path does not exist.")
    exit(1)

usar_pesos = input("Do you want to use weights? (y/N): ").strip().lower() == 'y'
print("Which graphs do you want to display?")
print("1 - Average Bars by Dimension")
print("2 - Boxplot by Dimension")
print("3 - Radar Chart")
print("4 - Final TLX by Participant")
print("Press Enter for All")

entrada = input("Enter the numbers separated by commas (e.g. 1,3):").strip()
if entrada:
    opcoes = set(entrada.split(','))
else:
    opcoes = {'1', '2', '3', '4'}

# === LOAD CSV FILE ===
try:
    data = pd.read_csv(caminho)
except Exception as e:
    print(f"Error loading CSV: {e}")
    exit(1)

dimensoes = ['Mental', 'Physical', 'Temporal', 'Performance', 'Effort', 'Frustration']
condicoes = data['Condicao'].unique()
palette = get_palette(condicoes)

# === TLX FINAL CALCULATION ===
def calcular_tlx(row):
    if usar_pesos:
        total_peso = 0
        total = 0
        for d in dimensoes:
            nota = row[d]
            peso = row.get(f'Peso_{d}', 1)
            total += nota * peso
            total_peso += peso
        return total / total_peso if total_peso > 0 else 0
    else:
        return row[dimensoes].mean()

data['TLX_Final'] = data.apply(calcular_tlx, axis=1)

# === GRAPH 1: AVERAGE BARS BY DIMENSION ===
if '1' in opcoes:
    if usar_pesos:
        for d in dimensoes:
            data[f'{d}_pond'] = data[d] * data[f'Peso_{d}']
        medias = {}
        for d in dimensoes:
            soma_nota = data.groupby('Condicao')[f'{d}_pond'].sum()
            soma_peso = data.groupby('Condicao')[f'Peso_{d}'].sum()
            medias[d] = soma_nota / soma_peso
        data_media = pd.DataFrame(medias).T.reset_index().melt(id_vars='index', var_name='Condicao', value_name='Score')
        data_media.rename(columns={'index': 'Dimension'}, inplace=True)
    else:
        data_media = data.groupby('Condicao')[dimensoes].mean().T.reset_index().melt(id_vars='index', var_name='Condicao', value_name='Score')
        data_media.rename(columns={'index': 'Dimension'}, inplace=True)

    plt.figure(figsize=(8, 5))
    sb.barplot(x='Dimension', y='Score', hue='Condicao', data=data_media, palette=palette)
    plt.title("Average Workload by Dimension" + (" (Weighted)" if usar_pesos else ""))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=False)

# === GRAPH 2: BOXPLOT BY DIMENSION ===
if '2' in opcoes:
    data_box = data.melt(id_vars=['Participante', 'Condicao'], value_vars=dimensoes,
                         var_name='Dimension', value_name='Score')
    plt.figure(figsize=(8, 6))
    sb.boxplot(x='Dimension', y='Score', hue='Condicao', data=data_box, palette=palette)
    plt.title("Score Distribution by Dimension")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show(block=False)

# === GRAPH 3: RADAR CHART ===
if '3' in opcoes:
    angles = np.linspace(0, 2 * np.pi, len(dimensoes), endpoint=False).tolist()
    angles += [angles[0]]
    
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_aspect('equal')
    
    def polar_to_cart(angle, radius):
        return radius * np.cos(angle), radius * np.sin(angle)
    
 
    for level in range(20, 101, 20):
        hex_points = []
        for angle in angles[:-1]: 
            x, y = polar_to_cart(angle, level)
            hex_points.append([x, y])
        
        hexagon = Polygon(hex_points, fill=False, edgecolor='gray', 
                         linewidth=0.5, linestyle='--')
        ax.add_patch(hexagon)
    
   
    for angle in angles[:-1]:
        x, y = polar_to_cart(angle, 100)
        ax.plot([0, x], [0, y], '--', lw=0.5, color='gray')
    
    for cond in condicoes:
        if usar_pesos:
            valores = []
            for d in dimensoes:
                subset = data[data['Condicao'] == cond]
                notas = subset[d]
                pesos = subset[f'Peso_{d}']
                media_pond = (notas * pesos).sum() / pesos.sum()
                valores.append(media_pond)
        else:
            valores = data[data['Condicao'] == cond][dimensoes].mean().tolist()
        
        valores += [valores[0]]
        
      
        x_coords = []
        y_coords = []
        for angle, valor in zip(angles, valores):
            x, y = polar_to_cart(angle, valor)
            x_coords.append(x)
            y_coords.append(y)
        
        ax.plot(x_coords, y_coords, label=cond, color=palette[cond])
        ax.fill(x_coords, y_coords, color=palette[cond], alpha=0.25)
    
  
    for angle, dim in zip(angles[:-1], dimensoes):
        x, y = polar_to_cart(angle, 110)
        ax.text(x, y, dim, ha='center', va='center', fontweight='bold')
    
    for level in range(20, 101, 20):
        x, y = polar_to_cart(angles[0], level)
        ax.text(x + 5, y, str(level), ha='left', va='center', fontsize=8, color='gray')
    
    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    plt.title("NASA-TLX Mean Profile" + (" (Weighted)" if usar_pesos else ""))
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.show(block=False)

# === GRAPH 4: FINAL TLX BY PARTICIPANT ===
if '4' in opcoes:
    plt.figure(figsize=(8, 5))
    sb.barplot(x='Participante', y='TLX_Final', hue='Condicao', data=data, palette=palette)
    plt.title("Final TLX Score by Participant")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.show()

input("Press Enter to exit...")
