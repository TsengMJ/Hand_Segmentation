import json
import os

Jason_file = "labels.jason"

with open(Jason_file, "a") as f:
    jason_file = json.load(open("via_region_data.json"))
    infos = list(jason_file.values())

    f.write("{\n")
    for info in infos:
        filename = info["filename"]
        regions_info = info["regions"]

        regions = []
        for region in regions_info:
            xs = region["shape_attributes"]["all_points_x"]
            ys = region["shape_attributes"]["all_points_y"]
            regions.append([xs, ys])

        info = '{{"filename": "{}", "regions": {} }},\n'.format(filename, regions)
        f.write(info)

    f.write("{\n")