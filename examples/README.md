# Examples

Both examples are unedited logs from the experiments reported in the paper. Model-access configuration has been removed.

**fidelity_tavern/** One episode of the Tavern inheritance dispute (Section 5.2). Each round lists the scenario event, every agent's pre-decision (urgency, visibility, intent), the speaking order, public and private utterances with private reasoning, and the judge's emotional (S) and relational (R) updates with their stated reasons. `episode01_final_state.json` holds the final S of every agent and the final directed relationship matrix.

**tpr_lost_at_sea/** The run shown in Figure 7 (Section 5.3). `recasting_trajectory.json` lists, for each iteration, the casting, mean L1 over 12 episodes, the per-episode diagnoses with proposed recasts, and the majority-voted changes. The two transcripts show one episode under the initial casting (iteration 0) and one under the final casting (iteration 3).
