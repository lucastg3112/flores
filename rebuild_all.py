import codecs
import json
import re

# Load data from the old script
namespace = {}
with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    code = f.read()
exec_code = code[:code.find("with open('e:\\\\pagina web aldea global 2")]
exec(exec_code, namespace)

japon_indicators = namespace['japon_indicators']
eau_indicators = namespace['eau_indicators']

def generate_india_style_html(indicators, country_name, country_id, color):
    html = f'<div id="country-{country_id}" class="country-content hidden">\n'
    for idx, ind in enumerate(indicators):
        i = idx + 1
        title = ind['title']
        title_clean = title.split('. ', 1)[1] if '. ' in title else title
        
        # fix icon mapping
        icon = ind['icon']
        if not icon or icon == "":
            icon = "analytics"
            
        html += f'''
            <section class="indicator-card botanical-shadow reveal active" style="border-top-color: {color};">
                <div class="flex flex-col lg:flex-row gap-16">
                    <div class="lg:w-1/2 flex flex-col">
                        <h2 class="font-headline-md text-3xl mb-3 flex items-center gap-4" style="color: {color};">
                            <div class="icon-circle w-14 h-14 rounded-full flex items-center justify-center shrink-0"
                                style="background-color: {color}20; color: {color};">
                                <span class="material-symbols-outlined text-3xl"
                                    style="font-variation-settings: 'FILL' 1;">{icon}</span>
                            </div>
                            Indicador {i}
                        </h2>
                        <h3 class="text-xl font-bold mb-2 ml-18 pl-18">{title_clean}</h3>
                        <p class="text-sm text-gray-500 font-medium tracking-wide mb-8 ml-18 pl-18">Análisis de este indicador clave para el mercado de {country_name}.</p>
                        
                        <div class="glass-panel p-8 rounded-2xl mb-8 flex-grow">
                            <h4 class="font-bold mb-4 flex items-center gap-2 text-lg">
                                <span class="material-symbols-outlined" style="color: {color};">analytics</span> Texto Analítico / Hallazgo
                            </h4>
                            <p class="text-base leading-relaxed text-gray-700">{ind['description']}</p>
                        </div>
                        
                        <div class="p-8 rounded-2xl border relative overflow-hidden group"
                            style="background-color: {color}0d; border-color: {color}33;">
                            <div class="absolute right-0 top-0 w-32 h-32 rounded-full blur-2xl -mr-10 -mt-10 transition-transform group-hover:scale-150"
                                style="background-color: {color}1a;"></div>
                            <h4 class="font-bold mb-3 flex items-center gap-2 text-lg relative z-10"
                                style="color: {color};">
                                <span class="material-symbols-outlined">public</span> Impacto Comercial
                            </h4>
                            <p class="text-base leading-relaxed mb-6 relative z-10 text-gray-700">El impacto proyectado es: <strong>{ind['impact']}</strong></p>
                            
                            <div class="inline-flex items-center gap-2 text-white px-5 py-2 rounded-full text-sm font-bold shadow-lg relative z-10"
                                style="background-color: {color};">
                                <span class="material-symbols-outlined text-[20px]"
                                    style="font-variation-settings: 'FILL' 1;">star</span>
                                Calificación: {ind['rating']} / 5
                            </div>
                        </div>
                    </div>
                    
                    <div class="lg:w-1/2 flex flex-col justify-center bg-white/50 rounded-3xl p-6 border border-gray-200 shadow-inner">
                        <div class="relative w-full h-[400px]">
                            <canvas id="chart_{country_id}_{i}"></canvas>
                        </div>
                    </div>
                </div>
            </section>
        '''
    html += "</div>"
    return html

html_japon = generate_india_style_html(japon_indicators, 'Japón', 'japon', '#735664')
html_eau = generate_india_style_html(eau_indicators, 'Emiratos Árabes', 'arabia', '#6c5777')

# 1. UPDATE INDEX.HTML
with codecs.open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'r', 'utf-8') as f:
    content = f.read()

japon_start = content.find('<div id="country-japon"')
main_end = content.find('</main>')

new_content = content[:japon_start] + html_japon + "\n" + html_eau + "\n    " + content[main_end:]
with codecs.open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'w', 'utf-8') as f:
    f.write(new_content)


# 2. UPDATE CHARTS JS
def get_chart_configs(indicators):
    configs = {}
    for idx, ind in enumerate(indicators):
        config = ind['chart_config']
        # remove options.responsive etc if present to match the js style, or keep them.
        # we will keep the data part and inject it
        configs[idx + 1] = {
            "type": config['type'],
            "data": config['data'],
            "options": {"responsive": True, "maintainAspectRatio": False}
        }
    return json.dumps(configs, ensure_ascii=False)

japon_json = get_chart_configs(japon_indicators)
eau_json = get_chart_configs(eau_indicators)

with codecs.open('e:\\pagina web aldea global 2\\assets\\js\\charts-entrega3.js', 'r', 'utf-8') as f:
    js_content = f.read()

# Insert the JSON into chartDataConfig
# The end of chartDataConfig is "}\n};\nwindow.renderChartsForCountry"
insertion_point = js_content.find('};\nwindow.renderChartsForCountry')
if insertion_point != -1:
    new_js = js_content[:insertion_point] + ',\n    "japon": ' + japon_json + ',\n    "arabia": ' + eau_json + '\n' + js_content[insertion_point:]
    with codecs.open('e:\\pagina web aldea global 2\\assets\\js\\charts-entrega3.js', 'w', 'utf-8') as f:
        f.write(new_js)
    print("JS updated.")
else:
    print("Could not find insertion point in JS.")

print("HTML updated.")
