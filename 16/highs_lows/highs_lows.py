import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename ='death_valley_2014.csv'
with open(filename) as f:
    render = csv.reader(f)
    header_row = next(render)
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    dates,highs,lows = [],[],[]
    for row in render:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor ='blue',alpha=0.1)
#设置图形格式
plt.title("Daily high and low temperature,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.show()
