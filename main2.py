import score

p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}
players = [p1, p2, p3, p4, p5]
scores = {}

for i in players:
    if i['role'] == 'bat':
        sc = score.bat(i)
        scores.update({i["name"]: sc})
    else:
        sc = score.bowl(i)
        scores.update({i["name"]:sc})

maximum = (max(scores))
print("The maximum scorer is %d with score %s" % (scores[maximum], maximum))










    


      


