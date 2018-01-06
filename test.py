import os

from ase_parse import parse


theme_path = os.path.join(os.path.dirname(__file__), "themes/")

for theme_file in os.listdir(theme_path):
    fp = os.path.join(theme_path, theme_file)
    print("Parsing %s" % theme_file)
    f = parse(fp)
    if not f:
        raise ValueError
    print("    %s" % f.data.palette.title)
    for color in f.data.palette.colors:
        print("      (%s)" % ", ".join(["%.04f" % f for f in color.color_values]))
