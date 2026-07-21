import codecs
import re

with codecs.open('e:\\pagina web aldea global 2\\rebuild_all.py', 'r', 'utf-8') as f:
    content = f.read()

# We need to replace the HTML template part inside generate_india_style_html
# Specifically, we replace:
"""
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
"""
# with:
"""
                        <div class="p-8 rounded-2xl border relative overflow-hidden group"
                            style="background-color: {color}0d; border-color: {color}33;">
                            <div class="absolute right-0 top-0 w-32 h-32 rounded-full blur-2xl -mr-10 -mt-10 transition-transform group-hover:scale-150"
                                style="background-color: {color}1a;"></div>
                            <h4 class="font-bold mb-3 flex items-center gap-2 text-lg relative z-10"
                                style="color: {color};">
                                <span class="material-symbols-outlined">public</span> Relevancia para Dreams Flower S.A.S.
                            </h4>
                            <p class="text-base leading-relaxed mb-6 relative z-10 text-gray-700">{relevancia}</p>
                            
                            <div class="inline-flex items-center gap-2 text-white px-5 py-2 rounded-full text-sm font-bold shadow-lg relative z-10"
                                style="background-color: {color};">
                                <span class="material-symbols-outlined text-[20px]"
                                    style="font-variation-settings: 'FILL' 1;">lightbulb</span>
                                Oportunidad. Nivel de impacto: {ind['impact']}
                            </div>
                        </div>
"""

# And we also need to split the description inside generate_india_style_html
# we will inject code before html += f'''...
injection = """
        desc = ind['description']
        sentences = desc.split('. ')
        relevance_sentences = []
        analytic_sentences = []
        for s in sentences:
            sl = s.lower()
            if 'dreams' in sl or 'exportador' in sl or 'colombian' in sl or 'oportunidad' in sl or 'beneficia' in sl or 'ventaja' in sl or 'ingreso' in sl:
                relevance_sentences.append(s)
            else:
                analytic_sentences.append(s)
        
        if not relevance_sentences:
            relevance_sentences = [sentences[-1]]
            analytic_sentences = sentences[:-1]
            
        relevancia = '. '.join(relevance_sentences)
        if not relevancia.endswith('.'): relevancia += '.'
        
        analytic_text = '. '.join(analytic_sentences)
        if analytic_text and not analytic_text.endswith('.'): analytic_text += '.'
        if not analytic_text: analytic_text = desc
"""

# Now we replace the {ind['description']} with {analytic_text}

# Do the replacements
content = content.replace("html += f'''", injection + "\n        html += f'''")
content = content.replace("{ind['description']}</p>", "{analytic_text}</p>")

old_html = """<h4 class="font-bold mb-3 flex items-center gap-2 text-lg relative z-10"
                                style="color: {color};">
                                <span class="material-symbols-outlined">public</span> Impacto Comercial
                            </h4>
                            <p class="text-base leading-relaxed mb-6 relative z-10 text-gray-700">El impacto proyectado es: <strong>{ind['impact']}</strong></p>
                            
                            <div class="inline-flex items-center gap-2 text-white px-5 py-2 rounded-full text-sm font-bold shadow-lg relative z-10"
                                style="background-color: {color};">
                                <span class="material-symbols-outlined text-[20px]"
                                    style="font-variation-settings: 'FILL' 1;">star</span>
                                Calificación: {ind['rating']} / 5
                            </div>"""

new_html = """<h4 class="font-bold mb-3 flex items-center gap-2 text-lg relative z-10"
                                style="color: {color};">
                                <span class="material-symbols-outlined">public</span> Relevancia para Dreams Flower S.A.S.
                            </h4>
                            <p class="text-base leading-relaxed mb-6 relative z-10 text-gray-700">{relevancia}</p>
                            
                            <div class="inline-flex items-center gap-2 text-white px-5 py-2 rounded-full text-sm font-bold shadow-lg relative z-10"
                                style="background-color: {color};">
                                <span class="material-symbols-outlined text-[20px]"
                                    style="font-variation-settings: 'FILL' 1;">lightbulb</span>
                                Oportunidad. Impacto: {ind['impact']}
                            </div>"""

content = content.replace(old_html, new_html)

with codecs.open('e:\\pagina web aldea global 2\\rebuild_all_relevance.py', 'w', 'utf-8') as f:
    f.write(content)

print("Updated script created.")
