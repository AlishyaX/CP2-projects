import matplotlib.pyplot as plt
import numpy as np

def radar_chart(character):
    stats = ['strength', 'defense', 'speed', 'health']
    values = [character[stat] for stat in stats]
    values += values[:1]  # Repeat the first value to close the radar chart
    
    angles = np.linspace(0, 2 * np.pi, len(stats), endpoint=False).tolist()
    angles += angles[:1]

    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], stats)

    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.4)
    
    plt.title(f"Stats for {character['name']}")
    plt.show()
