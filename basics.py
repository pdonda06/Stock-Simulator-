from taipy import Gui
import pandas as pd

data = {
    "Date": pd.date_range("2023-12-12", periods=4, freq="D"),
    "Min": [822,197.7,27.7,75.5],
    "Max": [998.6,658.2,212,423.5]
}


title = "Stock Simulator By Donda"
path = "logo.png"
company_name="Tata"
company_minp=457
company_maxp=809

def button_pressed(state):
    print("Hy")
    print(state.path)
    print(state.company_minp)

    with open("data.txt","w") as f:
        f.write(f"{state.company_name},{state.company_minp},{state.company_maxp}")

page = """
<|text-center |
<|{path}|image|>

<|{title}|hover_text=Welcome to Stock Simulator|>

Name of Stock:<|{company_name}|input|>

Min price:<|{company_minp}|input|>


Max price:<|{company_maxp}|input|>

<|Run Simulation|button|on_action=button_pressed|>

<|{title}|hover_text=Your Simulation|>

<|{data}|chart|mode=lines|x=Date|y[1]=Min|y[2]=Max|color[1]=blue|color[2]=red|>

>
"""

if __name__ == "__main__":
    app=Gui(page)
    app.run(use_reloader=True)

