#Name :- Mayuri Pawar
#Branch :- Computer
#Task :- Matplotlib styles

import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023]

kohli_runs = [1200, 1377, 842, 560, 765, 1100]
rohit_runs = [1030, 1490, 912, 700, 899, 980]


plt.plot(years, kohli_runs, label="Virat Kohli", color='blue', linestyle='--', marker='o')

plt.plot(years, rohit_runs, label="Rohit Sharma", color='green', linestyle='-.', marker='s')


plt.title("Runs Scored per Year - Kohli vs Rohit")
plt.xlabel("Year")
plt.ylabel("Runs Scored")


plt.grid(True)
plt.legend()

plt.show()
