import codecs
import re

with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    content = f.read()

botanical_colors = ['"#3d6751"', '"#735664"', '"#6c5777"', '"#ba1a1a"', '"#a8d5ba"']

def replace_color(match):
    # keep #3d6751 if it already is
    if match.group(0).lower() in botanical_colors:
        return match.group(0)
    # pick a color based on hash to be consistent
    h = hash(match.group(0))
    return botanical_colors[h % len(botanical_colors)]

# replace color strings in JSON like "#abcdef"
new_content = re.sub(r'"#[0-9a-fA-F]{6}"', replace_color, content)

# also replace the background color with alpha (e.g. "#4CAF5020")
botanical_colors_alpha = ['"#3d675120"', '"#73566420"', '"#6c577720"', '"#ba1a1a20"', '"#a8d5ba20"']
def replace_color_alpha(match):
    if match.group(0).lower() in botanical_colors_alpha:
        return match.group(0)
    h = hash(match.group(0))
    return botanical_colors_alpha[h % len(botanical_colors_alpha)]

new_content = re.sub(r'"#[0-9a-fA-F]{8}"', replace_color_alpha, new_content)

with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'w', 'utf-8') as f:
    f.write(new_content)

# Now modify rebuild_all.py to use #735664 and #6c5777 instead of #d946ef and #0ea5e9
with codecs.open('e:\\pagina web aldea global 2\\rebuild_all.py', 'r', 'utf-8') as f:
    rebuild_content = f.read()

rebuild_content = rebuild_content.replace("#d946ef", "#735664")
rebuild_content = rebuild_content.replace("#0ea5e9", "#6c5777")

with codecs.open('e:\\pagina web aldea global 2\\rebuild_all.py', 'w', 'utf-8') as f:
    f.write(rebuild_content)

print("Colors updated in scripts.")
