"""Reproduce the main quantitative tables of the paper from the released data.

Usage:  python scripts/reproduce_tables.py
Requires: pandas
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1] / "data"
SCEN = ["hospital", "tavern", "quest", "negotiation", "demolition"]
BACKBONES = ["GPT-5-mini", "Claude-Sonnet-4.6", "DeepSeek-V4-Flash",
             "Gemini-3.1-Flash-Lite", "Grok-4.20", "GPT-4o"]


def table1():
    c = pd.read_csv(ROOT / "fidelity" / "fidelity_cells.csv")
    cols = {"Fav_T_mean": "Fav^T", "S_T_mean": "S^T", "reciprocity_mean": "Recip.",
            "EI_index_mean": "E-I", "balance_mean": "Balance(%)", "repair_pct_mean": "Repair(%)"}
    c = c.rename(columns=cols)
    c["Balance(%)"] *= 100
    a = c.groupby("scenario")[list(cols.values())].mean().loc[SCEN]
    print("\n== Table 1(a): scenario means over six backbones ==")
    print(a.round(2).to_string())
    b = c[c.scenario == "tavern"].set_index("backbone").loc[BACKBONES, list(cols.values())]
    print("\n== Table 1(b): Tavern scenario by backbone ==")
    print(b.round(2).to_string())


def trajectories_check():
    t = pd.read_csv(ROOT / "fidelity" / "trajectories.csv")
    last = t[t["round"] == t["round"].max()]
    fav = last.groupby(["scenario", "backbone", "episode"]).favorability.mean() \
              .groupby(["scenario", "backbone"]).mean()
    c = pd.read_csv(ROOT / "fidelity" / "fidelity_cells.csv").set_index(["scenario", "backbone"])
    diff = (fav - c["Fav_T_mean"]).abs().max()
    print(f"\nFinal favorability recomputed from trajectories: max |diff| vs cells = {diff:.4f}")


def table2_and_3():
    r = pd.read_csv(ROOT / "recasting" / "recasting_iterations.csv")
    init = r[r.iteration == 0].set_index(["task", "method", "initialization", "backbone"]).score
    final = r[r.is_final == 1].set_index(["task", "method", "initialization", "backbone"]).score
    both = pd.DataFrame({"Init": init, "Final": final})
    avg = both.groupby(["task", "method", "initialization"]).mean().unstack("initialization")
    print("\n== Tables 3-4: means over six backbones (12 episodes per casting) ==")
    print(avg.round(2).to_string())


if __name__ == "__main__":
    table1()
    trajectories_check()
    table2_and_3()
