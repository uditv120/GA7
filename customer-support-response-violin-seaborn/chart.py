import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Styling for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Random seed for reproducibility
rng = np.random.default_rng(42)

# Synthetic, realistic response time data (in minutes) by support channel
channels = [
    "Email",       # typically slower, wider variance
    "Phone",       # faster, moderate variance
    "Chat",        # fastest, tight variance
    "Social",      # mixed, heavier tail
    "In-App"       # near-chat speeds, some tail
]

n_per_channel = 600

# Define channel-specific distributions (mixtures + clipping for realism)
# Using lognormal/gamma-like shapes to reflect positive, skewed response times
params = {
    "Email":  {"dist": "lognorm", "mean": 35, "sigma": 0.6},  # slower
    "Phone":  {"dist": "lognorm", "mean": 18, "sigma": 0.45},
    "Chat":   {"dist": "lognorm", "mean": 8,  "sigma": 0.35},  # fastest
    "Social": {"dist": "lognorm", "mean": 22, "sigma": 0.7},   # heavy tail
    "In-App": {"dist": "lognorm", "mean": 12, "sigma": 0.45},
}

def sample_response_times(mean, sigma, size):
    # Create lognormal around a rough mean by solving for mu given mean and sigma
    # mean_lognormal = exp(mu + sigma^2 / 2) -> mu = ln(mean) - sigma^2/2
    mu = np.log(mean) - (sigma ** 2) / 2.0
    samples = rng.lognormal(mean=mu, sigma=sigma, size=size)
    # Introduce occasional SLA breaches/heavy tails
    tail = rng.choice([0, 1], size=size, p=[0.95, 0.05])
    tail_boost = rng.lognormal(mean=np.log(2), sigma=0.6, size=size)  # 2x-ish bumps
    samples = np.where(tail == 1, samples * tail_boost, samples)
    # Clip to a reasonable max (e.g., 180 minutes)
    return np.clip(samples, 1, 180)

records = []
for ch in channels:
    p = params[ch]
    times = sample_response_times(p["mean"], p["sigma"], n_per_channel)
    pri = rng.uniform(0.5, 1.5, size=n_per_channel)  # priority multiplier
    # Priority: High/Normal/Low derived from pri
    priority = pd.cut(pri, bins=[0, 0.85, 1.15, np.inf], labels=["High", "Normal", "Low"], include_lowest=True)
    # Final observed response time with a small noise by priority multiplier
    observed = times * pri
    for t, pr in zip(observed, priority):
        records.append({"Channel": ch, "Response Time (min)": float(t), "Priority": str(pr)})

# Create DataFrame
_df = pd.DataFrame.from_records(records)

# Order categories for consistent presentation
cat_order = ["Chat", "In-App", "Phone", "Social", "Email"]
_df["Channel"] = pd.Categorical(_df["Channel"], categories=cat_order, ordered=True)
_df["Priority"] = pd.Categorical(_df["Priority"], categories=["High", "Normal", "Low"], ordered=True)

# Palette aligned with business context
palette = sns.color_palette("Set2", n_colors=3)

# Create 512x512 figure: figsize(8,8) at dpi=64 -> 512 px
plt.figure(figsize=(8, 8), dpi=64)

# Violin plot grouped by Channel and colored by Priority
# inner="quartile" to highlight quartiles; cut=0 to avoid extending beyond data range
ax = sns.violinplot(
    data=_df,
    x="Channel",
    y="Response Time (min)",
    hue="Priority",
    order=cat_order,
    hue_order=["High", "Normal", "Low"],
    palette=palette,
    inner="quartile",
    cut=0,
    linewidth=1,
    dodge=True,
)

# Improve readability
ax.set_title("Customer Support Response Time Distribution by Channel", pad=14, weight="bold")
ax.set_xlabel("")
ax.set_ylabel("Response Time (minutes)")
ax.set_ylim(0, _df["Response Time (min)"].quantile(0.98) * 1.05)

# Legend inside to preserve exact canvas size with tight layout
ax.legend(title="Priority", loc="upper right", frameon=True)

# Despine for a cleaner, publication-ready look
sns.despine(trim=True)

# Save next to this script, with required dpi and bbox_inches
out_path = Path(__file__).resolve().with_name("chart.png")
plt.tight_layout()
plt.savefig(out_path, dpi=64, bbox_inches="tight")
plt.close()
