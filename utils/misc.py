from json import load

region_list = []

with open('/home/user/projects/aiogram_projects/taksi_bot/reg_dis.json') as f:
    d: dict = load(f)
    for region in d.keys():
        region_list += [region]


def get_districts_by_region(region_name):
    with open('/home/user/projects/aiogram_projects/taksi_bot/reg_dis.json') as f:
        data: dict = load(f)
        districts = data.get(region_name)
        return districts
