import solara
import matplotlib.pyplot as plt
from model import MoneyModel

model = MoneyModel(n_agents=50)

@solara.component
def Page():
    step, set_step = solara.use_state(0)

    def run_step():
        model.step()
        set_step(step + 1)

    with solara.Column():
        solara.Text(f"Step: {step} | Total Wealth: {sum(a.wealth for a in model.agents)}")
        solara.Button("Run Step", on_click=run_step)

        wealths = [a.wealth for a in model.agents]
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.bar(range(len(wealths)), sorted(wealths, reverse=True), color="steelblue")
        ax.set_xlabel("Agent (ranked)")
        ax.set_ylabel("Wealth")
        ax.set_title("Wealth Distribution")
        plt.tight_layout()
        solara.FigureMatplotlib(fig)
        plt.close(fig)