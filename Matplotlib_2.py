#Name :- Mayuri Pawar
#Branch :- Computer
#Task :- Matplotlib Styles

import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023]

kohli_runs = [1200, 1377, 842, 560, 765, 1100]
rohit_runs = [1030, 1490, 912, 700, 899, 980]
dhoni_runs = [800, 950, 700, 500, 600, 650]  

plt.style.use('dark_background')

plt.plot(
    years, kohli_runs,
    label="Virat Kohli",
    color='orange',
    linestyle='--',
    marker='o'
)

plt.plot(
    years, rohit_runs,
    label="Rohit Sharma",
    color='lime',
    linestyle='-.',
    marker='s'
)

plt.plot(
    years, dhoni_runs,
    label="MS Dhoni",
    color='cyan',
    linestyle=':',
    marker='^'
)

plt.title("Runs Scored per Year - Kohli vs Rohit vs Dhoni")
plt.xlabel("Year")
plt.ylabel("Runs Scored")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
