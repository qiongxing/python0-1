from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

#掷几次骰子
results = []
for roll in range(5000):
    result =  die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

#对结果可视化
hist = pygal.Bar()

hist.title = "Resilts of rolling one a D6 and D10 5000 times"
hist.x_labels = [str(x) for x in range(2,max_results+1)]
hist.x_title = "Result"
hist.y_titles = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
