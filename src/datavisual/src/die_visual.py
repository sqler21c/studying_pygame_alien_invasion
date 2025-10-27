import plotly.express as px 

from die import Die

# 6면체 주사위 하나를 만듭니다.
die = Die()

# 주사위를 100번 굴립니다. 각 결과를 리스트에 저장합니다.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 결과를 분석합니다.
frequencies = []

poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과를 시작 합니다.
title = 'Results of rolling one D6 1000 times'
labels = {'x': 'Result', 'y': 'Frequency'}
fig = px.bar(x=poss_results, 
             y=frequencies, 
             title=title,
             labels=labels)
fig.show()]