import os
from natsort import natsorted

root = "img"

result = ""
for folder in natsorted(os.listdir(root)):
    if '0' <= folder[1] <= '9':
        index = folder[0:2]
        app_name = folder[2:]
    else:
        index = folder[0]
        app_name = folder[1:]
    with open(os.path.join(root, folder, "url.txt"), 'r') as f:
        url = f.readline()

    result += "## {}. [{}]({})\n\n".format(index, app_name, url)
    result += "<img src=\"/img/{}/obsolete.png\" alt=\"obsolete\" width=\"300px\" />\n".format(folder)
    result += "<img src=\"/img/{}/latest.png\" alt=\"latest\" width=\"300px\" />\n\n".format(folder)

with open("md", 'w') as f:
    f.write(result)
