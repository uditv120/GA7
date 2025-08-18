# Author contact: 22f3002257@ds.study.iitm.ac.in
# Marimo reactive notebook: interactive analysis demonstrating variable relationships

import marimo as mo

# Create the Marimo app instance
app = mo.App()


@app.cell
def __():
    """
    Setup cell
    - Imports libraries used across downstream cells.
    - Exposes them as variables so other cells can depend on them.
    Data flow: Provides np, pd, px to all dependent cells.
    """
    import numpy as np
    import pandas as pd
    import plotly.express as px

    # Return shared libraries for dependency injection into other cells
    return np, pd, px


@app.cell
def __(mo=mo):
    """
    Controls cell
    - Creates an interactive slider to control noise level in the synthetic dataset.
    Data flow: Exposes `noise` (widget) for use in dataset and visualization cells.
    """
    noise = mo.ui.slider(0, 50, value=10, label="Noise level (%)")

    # Display the widget in this cell
    noise

    # Make `noise` available to downstream cells
    return noise,


@app.cell
def __(noise, np, pd, mo=mo):
    """
    Data cell
    - Generates a synthetic linear dataset y = 2x + 3 with adjustable Gaussian noise.
    Dependencies: depends on `noise` and libraries (np, pd).
    Exposes: `df` for plotting and metrics.
    """
    rng = np.random.default_rng(0)
    n = 300
    x = np.linspace(0.0, 10.0, n)
    y = 2.0 * x + 3.0

    # Add noise proportional to the slider value (as a percentage of y's std dev)
    sigma = (noise.value / 100.0) * y.std()
    y_noisy = y + rng.normal(0.0, sigma, size=n)

    df = pd.DataFrame({"x": x, "y": y_noisy})

    # Optional preview for transparency
    mo.md(f"Generated {len(df)} rows with noise σ = {sigma:.3f} (from {noise.value}%)")
    df.head(5)

    return df,


@app.cell
def __(df, px, np, noise, mo=mo):
    """
    Visualization and metrics cell
    - Computes Pearson correlation and renders an interactive scatter plot with trendline.
    Dependencies: uses `df` from the data cell and `noise` for contextual messaging.
    Exposes: `r` (correlation) and `fig` (plotly figure) if needed elsewhere.
    """
    r = np.corrcoef(df["x"], df["y"])[0, 1]

    # Dynamic markdown based on widget state and computed metric
    strength = ("🟢 strong" if abs(r) > 0.8 else "🟡 moderate" if abs(r) > 0.5 else "🟥 weak")
    mo.md(
        f"""
        ### Correlation and Interpretation
        - Current noise: **{noise.value}%**
        - Pearson r: **{r:.3f}** → {strength}
        """
    )

    fig = px.scatter(
        df,
        x="x",
        y="y",
        opacity=0.7,
        title="y vs. x with adjustable noise (trendline=OLS)",
        labels={"x": "x", "y": "y"},
        trendline="ols",
    )

    fig

    return r, fig


@app.cell
def __(mo=mo):
    """
    Documentation cell (self-documenting notebook header)
    - Describes purpose and how to interact with the notebook.
    """
    mo.md(
        """
        # Interactive Data Analysis (Marimo)
        This notebook demonstrates reactive, reproducible analysis:
        - Adjust the slider to control noise in a synthetic linear relationship.
        - All dependent cells recompute automatically (like a spreadsheet).
        - Comments above each cell document data flow and dependencies.
        """
    )
    return


if __name__ == "__main__":
    # Run with: uvx marimo edit marimo_analysis.py
    app.run()
