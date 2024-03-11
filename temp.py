import matplotlib.pyplot as plt
import numpy as np
import copy
import datetime
import pandas as pd
from enum import Enum

class Status(Enum):
    DONE = "DONE"
    NOT_DONE = "NOT_DONE"


# 25/10/23 - 23/11/23
req_spec = [
    ["Belbin (or equivalent) strength assessment", 0.5, Status.NOT_DONE, "26/10/2023"],
    ["Introduction", 1, Status.DONE, "16/11/2023"],
    ["Risk assessment", 1, Status.DONE, "16/11/2023"],
    ["Cover page", 1, Status.DONE, "22/11/2023"],
    ["Introduction - overview and justification", 1, Status.DONE, "16/11/2023"],
    ["Introduction - product scope", 1, Status.DONE, "16/11/2023"],
    ["Introduction - system description", 1, Status.DONE, '16/11/2023'],
    ["Solution Requirements - functional requirements", 2, Status.DONE, "18/11/2023"],
    ["Solution Requirements - non-functional requirements", 2, Status.DONE, "18/11/2023"],
    ["Solution Requirements - risks and issues", 2, Status.DONE, "18/11/2023"],
    ["Project Development - development approach", 1, Status.DONE, "18/11/2023"],
    ["Project Development - project schedule", 1, Status.DONE, "18/11/2023"],
    ["Group review document", 0.5, Status.DONE, "20/11/2023"],
    ["Format document", 0.5, Status.DONE, "20/11/2023"],
    ["NOT_DONE", 2, Status.NOT_DONE, "20/11/2023"]
]

# 22/11/23 - 07/12/23
design_video = [
    ["Introduction", 1, Status.DONE, "29/11/2023"],
    ["Format script", 0.5, Status.DONE, "06/12/2023"],
    ["Technical outline - describe the technical aspects of the system", 3, Status.DONE, "03/12/2023"],
    ["Future work", 1, Status.DONE, "06/12/2023"],
    ["[slides] Technical outline - walkthrough of potential features", 2, Status.DONE, "05/12/2023"],
    ["[slides] Technical outline - development approach", 1, Status.DONE, "05/12/2023"],
    ["[slides] Technical outline - mockups, user journey", 2, Status.DONE, "05/12/2023"],
    ["[script] Technical outline - walkthrough of potential features", 1, Status.DONE, "05/12/2023"],
    ["[script] Technical outline - development approach", 1, Status.DONE, "05/12/2023"],
    ["[script] Technical outline - development approach", 1, Status.DONE, "05/12/2023"],
    ["NOT DONE", 2, Status.NOT_DONE, "05/12/2023"]
]

# 10/01/2024 - 01/02/2024
test_plan_report = [
    ["Unit testing", 1, Status.DONE, "18/01/2024"],
    ["Integration testing", 1, Status.DONE, "18/01/2024"],
    ["Testing methodology", 1, Status.DONE, "18/01/2024"],
    ["Test cases", 3, Status.DONE, "24/01/2024"],
    ["Introduction", 1, Status.DONE, "17/01/2024"],
    ["User acceptance testing", 1, Status.DONE, "24/01/2024"],
    ["Equivalence classes", 1, Status.DONE, "24/01/2024"],
    ["System testing", 1, Status.DONE, "24/01/2024"],
    ["Testing scope", 1, Status.DONE, "23/01/2024"],
    ["Test coverage", 1, Status.DONE, "22/01/2024"],
    ["Performance testing", 1, Status.DONE, "24/01/2024"],
    ["Functional testing", 1, Status.DONE, "25/01/2024"],
    ["Non-functional testing", 1, Status.DONE, "25/01/2024"],
    ["Testing context", 1, Status.DONE, "26/01/2024"],
    ["Failure severity", 1, Status.DONE, "26/01/2024"],
    ["Module integration testing", 2, Status.DONE, "26/01/2024"],
    ["References", 0.5, Status.DONE, "27/01/2024"],
    ["NOT DONE", 2, Status.NOT_DONE, "27/01/2024"]
]

# 07/02/2024 - 07/03/2024
user_manual = [
    ["User requirements table and analysis", 1, Status.DONE, "14/02/2024"],
    ["User journey", 1, Status.DONE, "15/02/2024"],
    ["Technical user manual", 3, Status.DONE, "16/02/2024"],
    ["Technologies overview", 1, Status.DONE, "16/02/2024"],
    ["Environment setup instructions", 1, Status.DONE, "24/02/2024"],
    ["Setup git instructions", 0.5, Status.DONE, "24/02/2024"],
    ["User interface instructions", 2, Status.DONE, "25/02/2024"],
    ["Implementing AI TTS functionality", 0.5, Status.DONE, "26/02/2024"],
    ["Non-Functional requirements / constraints", 1, Status.DONE, "27/02/2024"],
    ["Hardware/software limitations", 1, Status.DONE, "01/03/2024"],
    ["Compatibility requirements", 0.5, Status.DONE, "02/03/2024"],
    ["Future maintenance", 1, Status.DONE, "03/03/2024"],
    ["Future development", 1, Status.DONE, "03/03/2024"],
    ["Future development priority", 0.5, Status.DONE, "04/03/2024"],
    ["Ethical / societal analysis", 0.5, Status.DONE, "05/03/2024"],
    ["NOT DONE", 5, Status.NOT_DONE, "05/03/2024"]
]

# 14/02/2024 - 13/03/2024
product_presentation = [
    ["Introduction - introduce client", 0.5, Status.DONE, "04/03/2024"],
    ["Introduction - introduce project / requirements", 1, Status.DONE, "04/03/2024"],
    ["Solution / demonstration - key system features", 1, Status.DONE, "06/03/2024"],
    ["Solution / demonstration - requirements spec", 1, Status.DONE, "08/03/2024"],
    ["Solution / demonstration - comparison to original", 1, Status.DONE, "08/03/2024"],
    ["Solution / demonstration - system testing", 1, Status.DONE, "08/03/2024"],
    ["Handover plan", 2, Status.DONE, "08/03/2024"],
    ["Handover plan - user manual", 1, Status.DONE, "11/03/2024"],
    ["Format presentation / rehearsal", 0.5, Status.DONE, "12/03/2024"],
    ["NOT DONE", 5, Status.NOT_DONE, "12/03/2024"]
]

# 13/03/2024
product_handover = [
    ["Product handover", 2, Status.DONE, "24/04/2024"],
    ["Implement project", 10, Status.NOT_DONE, "24/04/2024"],
    ["Package project", 2, Status.NOT_DONE, "24/04/2024"]
]

sprints = [
    ["25/10/2023", "08/11/2023"],
    ["08/11/2023", "22/11/2023"],
    ["22/11/2023", "06/12/2023"],
    ["06/12/2023", "27/12/2023"],
    ["27/12/2023", "10/01/2024"],
    ["10/01/2024", "24/01/2024"],
    ["24/01/2024", "07/02/2024"],
    ["07/02/2024", "21/02/2024"],
    ["21/02/2024", "06/03/2024"],
    ["06/03/2024", "20/03/2024"],
    ["20/03/2024", "03/04/2024"]
]

all_issues = req_spec + design_video + test_plan_report + user_manual + product_presentation + product_handover

sp_left = sum(x[1] for x in all_issues)
total_sp = copy.copy(sp_left)
sp_completed = 0
sp_not_completed = 0

start_date = datetime.datetime(2023, 10, 25)
end_date = datetime.datetime(2024, 4, 4)
"03/04/2024"
x_values = []
y_values = []

def sp_by_date_str_fn(date_str):
    global sp_completed, sp_not_completed
    output = 0
    for issue in all_issues:
        try:
            if issue[3] == date_str:
                output += issue[1]
                if issue[2] == Status.DONE:
                    sp_completed += float(issue[1])
                elif issue[2] == Status.NOT_DONE:
                    sp_not_completed += float(issue[1])
        except:
            continue
    return output


fig, ax = plt.subplots()
num_days = (end_date - start_date).days

ax.grid()
# add line for ideal burn-rate
ideal_burn_rate_x = [start_date + datetime.timedelta(days=x) for x in range(num_days + 1)]
# y = (-total_sp / total_days) * x + total_sp
ideal_burn_rate_y = [(-total_sp / num_days) * i + total_sp for i in range(num_days + 1)]
plt.plot(ideal_burn_rate_x, ideal_burn_rate_y, linestyle='--', color='black')

while start_date <= end_date:
    x_values.append(start_date)
    date_str = start_date.strftime("%d/%m/%Y")
    sp_by_date_str = sp_by_date_str_fn(date_str)
    sp_left -= sp_by_date_str
    y_values.append(sp_left)

    start_date += datetime.timedelta(days=1)


print("SP completed:", sp_completed)
print("SP not completed:", sp_not_completed)
print("Total:", total_sp, sp_completed + sp_not_completed)
plt.xlabel("Sprint")
plt.ylabel("Story points")
ax.plot(x_values, y_values, color='black')

# shade sprints
sprints = [(datetime.datetime.strptime(start, "%d/%m/%Y"), datetime.datetime.strptime(end, "%d/%m/%Y")) for start, end in sprints]

midpoints = []
colors = plt.cm.tab10(range(len(sprints)))  # Get a colormap to distinguish each sprint
for i, (start_date, end_date) in enumerate(sprints):
    midpoint = start_date + (end_date - start_date) / 2
    midpoints.append(midpoint)

for i in range(len(x_values) - 1):  # This ensures i+1 is always a valid index
    # Find the minimum and maximum y-values for the current segment to determine the color
    min_y = min(ideal_burn_rate_y[i], y_values[i])
    max_y = max(ideal_burn_rate_y[i], y_values[i])

    # Choose color based on the condition
    color = 'green' if y_values[i] <= ideal_burn_rate_y[i] else 'red'

    # It's crucial to ensure i+1 doesn't exceed the list's bounds, which is guaranteed by the loop's range
    plt.fill_between(x_values[i:i + 2], y1=[min_y, min(y_values[i + 1], ideal_burn_rate_y[i + 1])],
                     y2=[max_y, max(y_values[i + 1], ideal_burn_rate_y[i + 1])], color=color, alpha=0.2)


plt.xticks(midpoints, [f'{i+1}' for i in range(len(sprints))])
plt.legend(loc='upper right', labels=['Ideal story points remaining', 'Actual story points remaining'])
plt.show()

# TODO: figure out why no work was done throughout sprint 4/5
# TODO: and sprint 7


# TODO: velocity charts
# TODO: add "not complete" blocks to issues, to add noise

"""
Velocity chart
"""
velocity_y_values = [[0, 0] for _ in range(len(sprints))]

start_date = datetime.datetime(2023, 10, 25)

for i, sprint in enumerate(sprints):
    start, end = sprint
    while start <= end:
        date_str = start.strftime("%d/%m/%Y")
        for issue in all_issues:
            if date_str == issue[3]:
                if issue[2] == Status.DONE:
                    velocity_y_values[i][1] += issue[1]
                velocity_y_values[i][0] += issue[1]
        start += datetime.timedelta(days=1)

velocity_sp_predicted = [x[0] for x in velocity_y_values]
velocity_sp_actual = [x[1] for x in velocity_y_values]

fig, ax = plt.subplots()

# Number of pairs
n_pairs = len(velocity_y_values)
# Create an index for each pair
index = np.arange(n_pairs)

# Plotting two bars side by side for each pair in the data
bar_width = 0.35

bar1 = ax.bar(index - bar_width/2, velocity_sp_predicted, bar_width, label='Predicted story points')
bar2 = ax.bar(index + bar_width/2, velocity_sp_actual, bar_width, label='Completed story points')

# Labeling
ax.set_xlabel('Sprint')
ax.set_ylabel('Story points')
ax.set_xticks(index)
ax.set_xticklabels([f'{i+1}' for i in range(n_pairs)])
ax.legend(loc='upper right')
# Display the plot
plt.tight_layout()
plt.show()