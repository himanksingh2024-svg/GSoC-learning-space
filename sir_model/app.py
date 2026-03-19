import solara
import matplotlib.pyplot as plt
from model import SIRModel, State

model = SIRModel()

@solara.component
def Page():
    step, set_step = solara.use_state(0)

    def run_step():
        model.step()
        set_step(step + 1)

    df = model.datacollector.get_model_vars_dataframe()

    with solara.Column():
        solara.Text(f"Step: {step}")
        solara.Button("Run Step", on_click=run_step)

        if len(df) > 0:
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.plot(df["Susceptible"], label="Susceptible", color="blue")
            ax.plot(df["Infected"], label="Infected", color="red")
            ax.plot(df["Recovered"], label="Recovered", color="green")
            ax.legend()
            ax.set_xlabel("Step")
            ax.set_ylabel("Agents")
            ax.set_title("SIR Epidemic Model")
            plt.tight_layout()
            solara.FigureMatplotlib(fig)
            plt.close(fig)