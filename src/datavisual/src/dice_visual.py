import plotly.express as px 

from die import Die

# 6면체 주사위 두 개를 만듭니다.
die_1 = Die()
die_2 = Die()

# 주사위를 100번 굴립니다. 각 결과를 리스트에 저장합니다.
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 결과를 분석합니다.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides 
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과를 시작 합니다.
title = 'Results of rolling two D6 Dice 1000 times'
labels = {'x': 'Result', 'y': 'Frequency'}
fig = px.bar(x=poss_results, 
             y=frequencies, 
             title=title,
             labels=labels)
fig.update_layout(xaxis_dtick=1)

fig.show()