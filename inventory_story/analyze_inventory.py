import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "inventory_turnover_2024.csv"
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

INDUSTRY_TARGET = 8.0
#Error: No data analysis file (.py, .R, .ipynb) found in the PR files

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    # ensure correct types and ordering
    order = ["Q1", "Q2", "Q3", "Q4"]
    df["Quarter"] = pd.Categorical(df["Quarter"], categories=order, ordered=True)
    df = df.sort_values("Quarter").reset_index(drop=True)
    return df


def compute_metrics(df: pd.DataFrame) -> dict:
    avg_turnover = df["InventoryTurnover"].mean()
    gap_to_target = INDUSTRY_TARGET - avg_turnover
    below_target_quarters = df[df["InventoryTurnover"] < INDUSTRY_TARGET]["Quarter"].tolist()

    metrics = {
        "average": round(float(avg_turnover), 2),
        "gap_to_target": round(float(gap_to_target), 2),
        "below_target_quarters": below_target_quarters,
        "min_quarter": df.loc[df["InventoryTurnover"].idxmin(), "Quarter"],
        "min_value": round(float(df["InventoryTurnover"].min()), 2),
        "max_quarter": df.loc[df["InventoryTurnover"].idxmax(), "Quarter"],
        "max_value": round(float(df["InventoryTurnover"].max()), 2),
    }
    return metrics


def plot_trend(df: pd.DataFrame) -> Path:
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x="Quarter", y="InventoryTurnover", marker="o", linewidth=2)
    plt.axhline(INDUSTRY_TARGET, color="red", linestyle="--", label=f"Industry target = {INDUSTRY_TARGET}")
    plt.title("Inventory Turnover Ratio - 2024")
    plt.ylabel("Turnover Ratio")
    plt.xlabel("Quarter")
    plt.legend()
    plt.tight_layout()
    out_path = OUTPUT_DIR / "turnover_trend.png"
    plt.savefig(out_path, dpi=200)
    plt.close()
    return out_path


def plot_bars(df: pd.DataFrame) -> Path:
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df, x="Quarter", y="InventoryTurnover", color="#4C78A8")
    plt.axhline(INDUSTRY_TARGET, color="red", linestyle="--", label=f"Industry target = {INDUSTRY_TARGET}")
    for i, row in df.iterrows():
        plt.text(i, row["InventoryTurnover"] + 0.2, f"{row['InventoryTurnover']:.2f}", ha="center", va="bottom", fontsize=9)
    plt.title("Inventory Turnover by Quarter vs Target")
    plt.ylabel("Turnover Ratio")
    plt.xlabel("Quarter")
    plt.legend()
    plt.tight_layout()
    out_path = OUTPUT_DIR / "turnover_bars.png"
    plt.savefig(out_path, dpi=200)
    plt.close()
    return out_path


def main():
    df = load_data(DATA_PATH)
    metrics = compute_metrics(df)
    trend_path = plot_trend(df)
    bars_path = plot_bars(df)

    summary = {
        "average": metrics["average"],
        "gap_to_target": metrics["gap_to_target"],
        "below_target_quarters": metrics["below_target_quarters"],
        "min": {"quarter": str(metrics["min_quarter"]), "value": metrics["min_value"]},
        "max": {"quarter": str(metrics["max_quarter"]), "value": metrics["max_value"]},
        "trend_chart": str(trend_path),
        "bars_chart": str(bars_path),
    }

    out_json = OUTPUT_DIR / "summary.json"
    pd.Series(summary).to_json(out_json, indent=2)

    print("Average Turnover:", metrics["average"])  # Expect 5.68
    print("Gap to Target (8):", metrics["gap_to_target"])  # Expect 2.32
    print("Below-target quarters:", ", ".join(metrics["below_target_quarters"]))
    print("Trend chart:", trend_path)
    print("Bars chart:", bars_path)


if __name__ == "__main__":
    main()

