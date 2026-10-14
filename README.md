# Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams

**Yirui Qi**<sup>1,2</sup>, **Xiaoming Zhang**<sup>1&dagger;</sup>, **Jaehong Yoon**<sup>2&dagger;</sup>
<sup>1</sup>Beihang University &nbsp;&nbsp; <sup>2</sup>Nanyang Technological University, Singapore
<sup>&dagger;</sup>Corresponding authors

[[Paper (arXiv)]](https://arxiv.org/abs/2610.15788) &nbsp; [[Project Page]](https://lululu896.github.io/Agent-Sociodrama/)

LLM agent teams fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. **Agent Sociodrama** models how agents' emotional states and directed, asymmetric relationships evolve over interaction, validates these trajectories against classical social-theory patterns and human judgments, and uses them to diagnose team failures. **Trajectory-Guided Persona Recasting (TPR)** then recasts agent personas to repair the team.

## Release status

| Component | Status |
|---|---|
| Processed results for both experiments (social-dynamics fidelity and persona recasting) | Released |
| Script that recomputes the main tables from the released data | Released |
| Example transcripts from both experiments | Released |
| Simulation engine, TPR controller, and task implementations | Will be released upon acceptance |

## Repository contents

```
data/
  fidelity/
    fidelity_cells.csv          30 scenario x backbone conditions: mean and s.d. of
                                Fav^T, S^T, reciprocity, E-I index, balance, repair (5 episodes each)
    kruskal_wallis_fav.csv      Kruskal-Wallis test of final favorability across backbones, per scenario
    trajectories.csv            Per-round emotional state S and directed favorability for every agent
                                and directed edge (5 scenarios x 6 backbones x 5 episodes x 9 rounds)
  recasting/
    recasting_iterations.csv    Every evaluated casting of the recasting loop: task, method,
                                initialization, backbone, iteration, score (mean over 12 episodes),
                                and the persona of each agent
scripts/
  reproduce_tables.py           Recomputes Table 1 and the model averages of Tables 3 and 4
examples/
  fidelity_tavern/              One complete nine-round episode of the Tavern inheritance dispute
                                (all five agents driven by Claude Sonnet 4.6; GPT-4o judge):
                                actions, private reasoning, and every S and R update
  tpr_lost_at_sea/              The Lost at Sea run shown in Figure 7 (DeepSeek V4-Flash, Random):
                                per-iteration castings, diagnoses, and proposed recasts,
                                plus one episode before (iteration 0) and after (iteration 3) recasting
```

## Reproducing the tables

```
pip install pandas
python scripts/reproduce_tables.py
```

## Column conventions

**fidelity_cells.csv.** `Fav_T` is mean final favorability over all directed edges in [-1, 1]; `S_T` is mean final affective valence in [0, 1]; `balance` is the fraction of balanced triads; `repair_pct` is the percentage of deteriorated directed edges that recover by the final round. Metric definitions follow the appendix of the paper.

**trajectories.csv.** One row per (scenario, backbone, episode, round, agent, target). `S` is the agent's emotional state after the round; `favorability` is the agent's favorability toward `target`, in [-1, 1].

**recasting_iterations.csv.** `iteration = 0` is the initial casting; `is_final = 1` marks the last evaluated casting, reported as *Final* in the paper. `metric` is top-1 accuracy (%) for Student Council, Pareto rate (%) for Solar-farm Negotiation, and L1 error to the expert ranking for NASA Moon Survival and Lost at Sea (lower is better). `method` is one of `TPR`, `TPR_wo_social_dynamics`, `SOTOPIA+recasting`, and `AgentVerse+recasting`.

## Citation

If you use our data or findings, please cite:

```bibtex
@article{qi2026agentsociodrama,
  title   = {Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams},
  author  = {Qi, Yirui and Zhang, Xiaoming and Yoon, Jaehong},
  journal = {arXiv preprint arXiv:2610.15788},
  year    = {2026}
}
```

## License

The data and examples in this repository are released under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). You may use and adapt them for non-commercial purposes with attribution.
