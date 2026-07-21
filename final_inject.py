import codecs

# We load the variables from generate_content.py
namespace = {}
with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    code = f.read()

# Execute everything up to the replacement logic
exec_code = code[:code.find("with open('e:\\\\pagina web aldea global 2")]
exec(exec_code, namespace)

html_japon = namespace['html_japon']
html_eau = namespace['html_eau']
js_charts = namespace['js_charts']

js_injection = f'''
        // JS Injected for Japan and UAE
        {js_charts}
    </script>
</body>
'''

with codecs.open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'r', 'utf-8') as f:
    content = f.read()

japon_start = content.find('<div id="country-japon"')
arabia_start = content.find('<div id="country-arabia"')
main_end = content.find('</main>')

if japon_start != -1 and arabia_start != -1 and main_end != -1:
    new_content = content[:japon_start] + html_japon + "\n\n        " + html_eau + "\n    " + content[main_end:]
    
    # Check if there is already injected js to avoid duplicating
    if "// JS Injected for Japan and UAE" in new_content:
        # replace the old injection
        pass # already injected in previous run? No, we replaced everything up to main_end, but js is after main_end
    
    new_content = new_content.replace('</script>\n</body>', js_injection)
    
    with codecs.open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'w', 'utf-8') as f:
        f.write(new_content)
    print("Success: File updated.")
else:
    print("Error: Could not find markers.")
