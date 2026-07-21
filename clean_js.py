import re
import codecs

with codecs.open('e:\\pagina web aldea global 2\\assets\\js\\charts-entrega3.js', 'r', 'utf-8') as f:
    js_content = f.read()

# Let's find where the dynamic configs start. It's either before "japon" or "arabia".
idx = js_content.find('\n    "japon":')
if idx == -1:
    idx = js_content.find('\n    "arabia":')
if idx == -1:
    idx = js_content.find('\n    "japon":') # fallback search
if idx == -1:
    # If not found, look for the clean end of india's block
    idx = js_content.find('};\nwindow.renderChartsForCountry')

if idx != -1:
    # Truncate and clean the base content
    base_js = js_content[:idx].strip()
    # Make sure it ends with the closing brace of india's object
    if not base_js.endswith('}'):
        # If it doesn't end with }, let's find the last }
        last_brace = base_js.rfind('}')
        if last_brace != -1:
            base_js = base_js[:last_brace+1]
            
    print("Found base JS length:", len(base_js))
    with codecs.open('e:\\pagina web aldea global 2\\assets\\js\\charts-entrega3.js', 'w', 'utf-8') as f:
        f.write(base_js + "\n};\n\nwindow.renderChartsForCountry = function(countryId) {\n    const configs = chartDataConfig[countryId];\n    if(!configs) return;\n    for(let i = 1; i <= 15; i++) {\n        const canvasId = \"chart_\" + countryId + \"_\" + i;\n        const canvas = document.getElementById(canvasId);\n        if(!canvas) continue;\n        if(chartInstances[canvasId]) { chartInstances[canvasId].destroy(); }\n        const ctx = canvas.getContext(\"2d\");\n        chartInstances[canvasId] = new Chart(ctx, configs[i]);\n    }\n};\nfunction initCharts() {\n    setTimeout(() => {\n        window.renderChartsForCountry(\"india\");\n    }, 500);\n}\nif (document.readyState === 'loading') {\n    document.addEventListener(\"DOMContentLoaded\", initCharts);\n} else {\n    initCharts();\n}\n")
    print("charts-entrega3.js cleaned successfully.")
else:
    print("Could not find insertion or cleaning point in JS.")
