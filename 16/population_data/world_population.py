import json

from country_code import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data= json.load(f)

#打印每个国家2010年人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code =get_country_code(country_name)
        if code:
            print(code +": "+str(population))
        else:
            print("ERROR - " +country_name)