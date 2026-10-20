# import copy
# list1 = [[1,2],[3,4]]
# shallow_copy = copy.copy(list1)
# shallow_copy[0][0]= 99
# # print('original copy', list1)
# # print('shallow copy ' ,shallow_copy)

# list2 = [[100,101],[102,103]]
# deep_copy = copy.deepcopy(list2)
# deep_copy[0][0] = 99
# print('original list', list2)
# print('deep copy list ', deep_copy)

# 2 zipped list

# list1 =[1,2,3]
# list2 = ['a','b','c']

# zipped_list = zip(list1,list2)
# list_zip = list(zipped_list)
# print(list_zip)

# 3 enumerate

# list1 = {'apple','banana','cherry'}
# for index , value in enumerate(list1):
#     print(f"Index : ", {index}, "Value : ", {value})


# list comperihenson
# n = [1,2,3,4]
# list1 = [i **2 for i in n]
# print(list1)

#5 dictionary compriheson
# n = [1,2,3,4]
# dic = {i for i in n}
# print(dic)

import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

soup = BeautifulSoup(requests.get(url).text, "html.parser")

grid = {}
max_x = max_y = 0

for row in soup.find_all("tr")[1:]:
    cells = row.find_all("td")

    if len(cells) < 3:
        continue

    x = int(cells[0].get_text(strip=True))
    char = cells[1].get_text(strip=True)
    y = int(cells[2].get_text(strip=True))

    grid[(x, y)] = char
    max_x = max(max_x, x)
    max_y = max(max_y, y)

for y in range(max_y, -1, -1):
    print("".join(grid.get((x, y), " ") for x in range(max_x + 1)))