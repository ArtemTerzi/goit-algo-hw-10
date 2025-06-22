from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem("Maximize_Production", LpMaximize)

x = LpVariable("Lemonade", lowBound=0, cat='Integer')
y = LpVariable("FruitJuice", lowBound=0, cat='Integer')

model += x + y, "Total_Production"

model += 2*x + 1*y <= 100, "Water"
model += 1*x <= 50, "Sugar"
model += 1*x <= 30, "LemonJuice"
model += 2*y <= 40, "FruitPuree"

model.solve()

print("Статус:", model.status)
print("Виробити лимонаду:", x.varValue)
print("Виробити фруктового соку:", y.varValue)
print("Загальна кількість напоїв:", value(model.objective))
