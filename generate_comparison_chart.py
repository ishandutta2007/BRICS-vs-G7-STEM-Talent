import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def generate_comparison_chart():
    # Data from all 5 STEM Olympiads (2007-2026)
    olympiads = [
        "1. IMO\n(Mathematics)",
        "2. IPhO\n(Physics)",
        "3. IChO\n(Chemistry)",
        "4. IBO\n(Biology)",
        "5. IOI\n(Informatics)"
    ]

    brics_adjusted_avg = [50.2, 51.6, 40.4, 36.8, 34.8]
    g7_avg = [32.6, 21.3, 18.1, 18.4, 21.7]
    brics_standard_avg = [45.4, 46.6, 36.2, 33.4, 30.8]

    # Setup aesthetic styling
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300, facecolor='#0d1117')
    ax.set_facecolor('#161b22')

    x = np.arange(len(olympiads))
    width = 0.36

    # Colors
    color_brics = '#f59e0b'      # Amber / Gold
    color_g7 = '#38bdf8'         # Cyan / Sky blue

    # Bars
    bars_brics = ax.bar(
        x - width/2, 
        brics_adjusted_avg, 
        width, 
        label='BRICS Average(Russia Ban Adjusted)', 
        color=color_brics,
        edgecolor='#fbbf24',
        linewidth=1.5,
        alpha=0.95,
        zorder=3
    )

    bars_g7 = ax.bar(
        x + width/2, 
        g7_avg, 
        width, 
        label='G7 Average', 
        color=color_g7,
        edgecolor='#7dd3fc',
        linewidth=1.5,
        alpha=0.95,
        zorder=3
    )

    # Reference indicator for unadjusted BRICS
    for i in range(len(olympiads)):
        ax.scatter(
            x[i] - width/2, 
            brics_standard_avg[i], 
            color='#ffffff', 
            s=40, 
            zorder=5, 
            marker='o',
            edgecolor='#92400e',
            linewidth=1.2,
            label='Unadjusted BRICS Avg' if i == 0 else ""
        )

    # Add Value Labels on Bars
    for bar in bars_brics:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color='#fbbf24')

    for bar in bars_g7:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 6),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12, fontweight='bold', color='#7dd3fc')

    # Percentage lead badges
    for i in range(len(olympiads)):
        lead = ((brics_adjusted_avg[i] - g7_avg[i]) / g7_avg[i]) * 100
        mid_x = x[i]
        top_y = max(brics_adjusted_avg[i], g7_avg[i]) + 6.5
        ax.text(
            mid_x, top_y, 
            f'+{lead:.0f}% lead', 
            ha='center', va='center',
            fontsize=10, fontweight='bold',
            color='#10b981',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#064e3b', edgecolor='#059669', alpha=0.9, lw=1)
        )

    # Overall grand comparison summary card box
    grand_text = (
        "Grand Summary (Across all 5 disciplines):\n"
        "• Adjusted BRICS Mean: 42.8 golds/country\n"
        "• G7 Mean: 22.4 golds/country\n"
        "• Overall BRICS Advantage: +91.1%"
    )
    fig.text(
        0.08, 0.79, grand_text,
        fontsize=10, color='#e6edf3',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#21262d', edgecolor='#30363d', alpha=0.95, lw=1.2)
    )

    # Titles & Labels
    ax.set_title('BRICS vs. G7 STEM Talent Comparison\nAverage Gold Medals per Country by Olympiad Discipline (2007–2026)', 
                 fontsize=15, fontweight='bold', color='#f0f6fc', pad=24)
    ax.set_xticks(x)
    ax.set_xticklabels(olympiads, fontsize=11, fontweight='semibold', color='#c9d1d9')
    ax.tick_params(axis='y', colors='#8b949e', labelsize=10)
    ax.tick_params(axis='x', colors='#c9d1d9')
    ax.set_ylabel('Average Gold Medals per Country', fontsize=12, fontweight='semibold', color='#c9d1d9', labelpad=10)
    ax.set_ylim(0, 65)

    # Grid & Spines
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='#8b949e', zorder=0)
    ax.grid(axis='x', visible=False)
    for spine in ax.spines.values():
        spine.set_edgecolor('#30363d')
        spine.set_linewidth(1.2)

    # Legend
    legend = ax.legend(
        loc='upper right', 
        frameon=True, 
        facecolor='#21262d', 
        edgecolor='#30363d', 
        fontsize=10.5,
        labelcolor='#e6edf3'
    )

    # Footnote
    fig.text(0.5, 0.015, 
             '* Adjusted BRICS Average simulates counterfactual performance if Russian participation was uninterrupted.',
             ha='center', fontsize=9, fontstyle='italic', color='#8b949e')

    plt.tight_layout(rect=[0, 0.04, 1, 0.96])

    # Save output
    output_dir = Path(__file__).resolve().parent / "assets"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "brics_vs_g7_comparison.png"
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    # plt.show()
    plt.close()
    print(f"Chart saved successfully at {output_path}")

if __name__ == "__main__":
    generate_comparison_chart()
