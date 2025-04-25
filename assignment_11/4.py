import pandas as pd

# Schedule of visits
data = {
    "John": [True, False, True, False, True, False, False, True, False, False],
    "Judy": [True, False, True, True, False, False, True, False, True, False],
}
schedule = pd.DataFrame(data)

# Calculate days until the next party
days_til_party = []
for i in range(len(schedule)):
    if schedule.loc[i, "John"] and schedule.loc[i, "Judy"]:
        days_til_party.append(0)
    elif i < len(schedule) - 1 and schedule.loc[i + 1, "John"] and schedule.loc[i + 1, "Judy"]:
        days_til_party.append(1)
    else:
        days_til_party.append(2)

schedule["days_til_party"] = days_til_party
print(schedule)
