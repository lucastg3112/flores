import codecs

with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'r', 'utf-8') as f:
    content = f.read()

# Let's write the new japon_indicators with updated descriptions and chart configs
japon_indicators_updated = """japon_indicators = [
    {
        "title": "1. Índice de Percepción de la Corrupción",
        "icon": "policy",
        "description": "Japón es un país de gran transparencia institucional que mantiene un bajo nivel de corrupción, registrando un puntaje sobresaliente de 73 sobre 100 en el Índice de Percepción de la Corrupción (IPC) durante el periodo 2021-2023. Aunque el puntaje disminuyó ligeramente a 71 en 2024 y 2025, el país continúa ofreciendo un entorno extremadamente seguro y confiable para los negocios. Para Dreams Flowers S.A.S., esta estabilidad reduce drásticamente los riesgos de sobrecostos informales o retrasos discrecionales en los trámites aduaneros y permisos sanitarios, facilitando una planificación financiera robusta.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_1",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Puntaje IPC (0-100)", "data": [73, 73, 73, 71, 71], "backgroundColor": "#735664"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Puntaje IPC (0-100) - Japón"}}, "scales": {"y": {"min": 70, "max": 75}}}
        }
    },
    {
        "title": "2. Estado de Derecho (Rule of Law)",
        "icon": "balance",
        "description": "El sistema legal de Japón es sumamente sólido, protegiendo con rigurosidad la propiedad intelectual, los contratos y el cumplimiento de las normas comerciales. En términos de percentil global, el país se mantuvo en un sobresaliente percentil del 89% en el Índice de Estado de Derecho (Rule of Law) durante 2021 y 2022, subiendo al 90% entre 2023 y 2025. Para Dreams Flowers S.A.S., este entorno con seguridad jurídica inmejorable garantiza que cualquier acuerdo comercial con importadores o distribuidores locales esté plenamente respaldado, minimizando disputas legales o riesgos de impago.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_2",
        "chart_config": {
            "type": "pie",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Percentil (%)", "data": [89, 89, 90, 90, 90], "backgroundColor": ["#ba1a1a", "#3d6751", "#735664", "#a8d5ba", "#6c5777"]}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Percentil (%) Estado de Derecho"}}}
        }
    },
    {
        "title": "3. Requisitos Fitosanitarios para Importación de Flores",
        "icon": "eco",
        "description": "Japón exige controles estrictos para la importación de flores frescas con el fin de evitar plagas. Los requisitos son altamente rigurosos: el Certificado Fitosanitario en origen es de carácter Obligatorio (100%), la Inspección Sanitaria física en puerto de entrada se aplica con un rotundo 'Sí' (100%), el Control de Plagas es catalogado como de nivel 'Alto' (90%) y la exigencia de una Normativa Estable y predecible se cumple en un 100% ('Sí'). Para Dreams Flowers S.A.S., cumplir rigurosamente con estos exigentes parámetros sanitarios asegura el acceso permanente al mercado de mayor valor de Asia y consolida el prestigio de la floricultura colombiana.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_3",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Certificado fitosanitario", "Inspección sanitaria", "Control de plagas", "Normativa estable"],
                "datasets": [{"label": "Nivel de Exigencia", "data": [100, 100, 90, 100], "backgroundColor": ["#735664", "#735664", "#a8d5ba", "#735664"]}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Requisitos Fitosanitarios de Importación"}}}
        }
    },
    {
        "title": "4. Arancel aplicado a flores importadas",
        "icon": "money_off",
        "description": "Como parte de sus políticas de apertura comercial para insumos perecederos de alto valor, Japón aplica un arancel promedio del 0% para las flores importadas, una condición que se ha mantenido completamente estable durante el periodo 2021-2025. Este beneficio arancelario nulo permite a Dreams Flowers S.A.S. ingresar sus productos sin cargas tributarias aduaneras adicionales, mejorando los márgenes de ganancia en comparación con otros mercados y permitiendo competir eficientemente frente a productores locales u otros exportadores de la región.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_4",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Arancel promedio (%)", "data": [0, 0, 0, 0, 0], "borderColor": "#735664", "backgroundColor": "#73566420", "fill": false}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Arancel Promedio Aplicado a Flores (%)"}}, "scales": {"y": {"min": 0, "max": 10}}}
        }
    },
    {
        "title": "5. Índice de Desempeño Logístico (LPI)",
        "icon": "local_shipping",
        "description": "Japón cuenta con una de las infraestructuras de transporte más avanzadas del mundo. Su desempeño en el Índice de Desempeño Logístico (LPI) del Banco Mundial registra un puntaje de 3.99 sobre 5 en 2018, ascendiendo a un sobresaliente 4.1 en 2023, consolidando al país como líder en eficiencia aduanera, calidad de infraestructura y puntualidad de envíos. Para Dreams Flowers S.A.S., este excelente desempeño logístico es crucial, garantizando que el transporte de flores (un producto altamente perecedero) se realice de forma ágil y eficiente tras el aterrizaje de los aviones.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_5",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2018", "2023"],
                "datasets": [{"label": "Puntaje LPI", "data": [3.99, 4.1], "backgroundColor": "#735664"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Índice de Desempeño Logístico (LPI)"}}, "scales": {"y": {"min": 0, "max": 5}}}
        }
    },
    {
        "title": "6. Tiempo promedio para el despacho aduanero",
        "icon": "schedule",
        "description": "Gracias a procesos aduaneros altamente digitalizados y eficientes, el tiempo promedio para el despacho de mercancías en Japón se ha mantenido constante en un rango de 1 a 2 días (con un promedio real registrado de 1.5 días) durante el periodo de 2021 a 2025. Este despacho extremadamente rápido resulta indispensable para Dreams Flowers S.A.S., pues asegura que la cadena de frío no se rompa y que las flores frescas sean liberadas a los distribuidores en óptimas condiciones, extendiendo su vida útil en el florero del consumidor final.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_6",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Tiempo promedio (días)", "data": [1.5, 1.5, 1.5, 1.5, 1.5], "backgroundColor": "#6c5777"}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Tiempo Promedio de Despacho Aduanero (Días)"}}, "scales": {"x": {"min": 0, "max": 3}}}
        }
    },
    {
        "title": "7. Regulación fitosanitaria y barreras no arancelarias",
        "icon": "gavel",
        "description": "El Ministerio de Agricultura, Silvicultura y Pesca de Japón (MAFF) exige un cumplimiento fitosanitario estricto. El Control de Plagas en origen, la Documentación rigurosa (exigida de forma estricta desde agosto de 2023) y la Inspección Física en terminales aéreas tienen una exigencia absoluta del 100%. La Tolerancia a plagas o insectos vivos es del 0% (Tolerancia Cero). Si se detecta un insecto vivo, el lote debe ser incinerado o fumigado con bromuro de metilo, lo que causa una pérdida estimada del 10% en el valor comercial de la flor premium. Para Dreams Flowers S.A.S., esto obliga a garantizar la máxima limpieza en postcosecha.",
        "impact": "Riesgo alto",
        "rating": 2,
        "chart_id": "chart_japon_7",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Control de Plagas", "Documentación", "Inspección Física", "Tolerancia a Plagas (insectos)", "Riesgo Pérdida (Fumigación)"],
                "datasets": [{"label": "Exigencia / Margen de Tolerancia (%)", "data": [100, 100, 100, 0, 10], "backgroundColor": ["#ba1a1a", "#ba1a1a", "#ba1a1a", "#a8d5ba", "#735664"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Control Fitosanitario en Aduana de Japón (%)"}}}
        }
    },
    {
        "title": "8. Estructura de Distribución y Logística",
        "icon": "grid_view",
        "description": "La distribución de flores en Japón se rige por un esquema tradicional. Aproximadamente el 85% del volumen de flores importadas pasa obligatoriamente por subastas públicas autorizadas por el gobierno, denominadas Kaki (como la subasta Ota en Tokio). Por otro lado, las ventas directas y canales de e-commerce directos a minoristas o supermercados representan tan solo el 15% restante de la participación de mercado. Para Dreams Flowers S.A.S., si bien las subastas aseguran pago rápido y distribución impecable en menos de 24 horas, la cantidad de intermediarios eleva el precio final y limita el margen comercial directo del productor colombiano.",
        "impact": "Riesgo medio",
        "rating": 3,
        "chart_id": "chart_japon_8",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Subastas Públicas (Kaki / Ota)", "Ventas Directas a Minoristas"],
                "datasets": [{"label": "Participación de Mercado (%)", "data": [85, 15], "backgroundColor": "#6c5777"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura de Distribución Floral en Japón (%)"}}}
        }
    },
    {
        "title": "9. Canales de Comercialización Digital y Suscripciones Florales",
        "icon": "shopping_cart",
        "description": "El comercio electrónico de flores en Japón experimentó un notable impulso. En el periodo 2023-2024, el crecimiento interanual del canal digital pasó del 10% al 12%, mientras que la participación del e-commerce y suscripciones digitales (modelos como Bloomee) en la venta de flores totales aumentó del 18% al 22%, alcanzando una valoración estimada de más de ¥50,000 millones (USD 350 millones). Para Dreams Flowers S.A.S., este auge representa una oportunidad inigualable para negociar de manera directa con distribuidores digitales, diversificando la demanda sin depender enteramente de las rígidas subastas mayoristas.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_9",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Crecimiento interanual", "Participación de mercado e-commerce"],
                "datasets": [
                    {"label": "2023", "data": [10, 18], "backgroundColor": "#3d6751"},
                    {"label": "2024", "data": [12, 22], "backgroundColor": "#735664"}
                ]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Canales Digitales e-commerce y Suscripciones (%)"}}}
        }
    },
    {
        "title": "10. Sostenibilidad, Certificaciones Ambientales y Sociales",
        "icon": "workspace_premium",
        "description": "El interés por la floricultura responsable ha crecido significativamente. La demanda corporativa de flores importadas que cuenten con certificación de sostenibilidad (como MPS o Fairtrade) subió del 40% en 2023 al 60% en 2024. Del mismo modo, la preferencia de los distribuidores y hoteles premium por empaques optimizados y libres de plástico escaló del 45% al 80% en ese mismo periodo. Para Dreams Flowers S.A.S., contar con estas certificaciones ecológicas y de comercio justo representa una ventaja competitiva de primer orden para posicionarse como un proveedor preferente y con precios premium.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_10",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Flores Certificadas (MPS/Fairtrade)", "Empaques Ecológicos / Libres de Plástico"],
                "datasets": [
                    {"label": "2023", "data": [40, 45], "backgroundColor": "#3d6751"},
                    {"label": "2024", "data": [60, 80], "backgroundColor": "#735664"}
                ]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Exigencia de Sostenibilidad y Empaques Ecológicos (%)"}}}
        }
    },
    {
        "title": "11. Usuarios de Internet y Conectividad Digital",
        "icon": "language",
        "description": "Japón destaca por su hiperconectividad de red. Para inicios de 2025, la tasa de penetración de internet alcanzó el 88.2% de la población (equivalente a 109 millones de usuarios conectados). Asimismo, la adopción de redes sociales representa el 78.6% de la población total y el 87% de los adultos mayores de 18 años. Esto se complementa con una velocidad promedio de descarga de internet fijo de 196.42 Mbps y un crecimiento interanual de tráfico de banda ancha del 12.7% en 2024. Para Dreams Flowers S.A.S., esta infraestructura digital robusta es perfecta para implementar estrategias de marketing y captar clientes premium.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_11",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Penetración Internet (Total)", "Adopción Redes Sociales (Adultos 18+)", "Adopción Redes Sociales (Total)"],
                "datasets": [{"label": "Porcentaje (%)", "data": [88.2, 87.0, 78.6], "backgroundColor": ["#6c5777", "#735664", "#3d6751"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Infraestructura Digital y Conectividad (%)"}}}
        }
    },
    {
        "title": "12. Hábitos de consumo y significación floral",
        "icon": "favorite",
        "description": "La cultura de consumo floral japonesa es una de las más ricas y exigentes del planeta. Tradiciones espirituales milenarias (como Ikebana e Hanakotoba), rituales y festividades (como el Obon y funerales) y la exigencia de máxima calidad física registran una importancia absoluta de 5 sobre 5 (Esencial/Máxima prioridad). Por su parte, el surgimiento de nuevas tendencias de consumo cotidiano en línea e-commerce se posiciona con un alto impacto de 4 sobre 5 (80%). Para Dreams Flowers S.A.S., este mercado asegura una demanda masiva, recurrente e inelástica de flores de la más alta calidad.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_12",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Tradición Espiritual (Ikebana)", "Rituales Obligatorios (Obon)", "Exigencia Calidad Física", "Tendencias Digitales Urbanas"],
                "datasets": [{"label": "Nivel de Importancia / Adopción (%)", "data": [100, 100, 100, 80], "backgroundColor": ["#735664", "#a8d5ba", "#3d6751", "#3d6751"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura del Consumo Floral en Japón (%)"}}}
        }
    },
    {
        "title": "13. Acceso a Tecnología e Innovación en la Cadena de Suministro",
        "icon": "devices",
        "description": "La distribución hortícola japonesa destaca por su digitalización y automatización. La inversión total en el mercado de logística de cadena de frío asciende a USD 18,000 millones (18.0 billion USD). El control de temperatura mediante sensores IoT logra una efectividad del 100%, asegurando que las mermas o pérdidas físicas de producto tras el ingreso logístico se reduzcan por debajo del 5.0% (Límite Máximo). Para Dreams Flowers S.A.S., esta sofisticación tecnológica garantiza la perfecta preservación de los tallos importados, eliminando el riesgo de deterioro térmico.",
        "impact": "Extremadamente favorable",
        "rating": 5,
        "chart_id": "chart_japon_13",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Inversión Cadena de Frío (B USD)", "Efectividad Monitoreo IoT (%)", "Pérdida/Mermas de Producto (%)"],
                "datasets": [{"label": "Valor Absoluto / Eficiencia (%)", "data": [18, 100, 5], "backgroundColor": ["#6c5777", "#6c5777", "#a8d5ba"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Distribución Logística y Cadena de Frío"}}}
        }
    },
    {
        "title": "14. Geográficos relevantes y Conectividad de Infraestructura",
        "icon": "map",
        "description": "Japón posee un índice de urbanización del 92.9%, lo que concentra la demanda de consumo en el megacorredor Kanto-Kansai. Los aeropuertos de Narita y Kansai absorben el 90.0% de la carga total de flor cortada que ingresa al país. Asimismo, la concentración urbana y del consumo de flores en este eje representa el 100% de la zona objetivo inicial. Para Dreams Flowers S.A.S., esta alta concentración geográfica facilita la distribución del producto, aunque expone la cadena al riesgo de tifones puntuales que puedan demorar los desembarques.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_14",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Índice de Urbanización Nacional (%)", "Carga en Aeropuertos Narita/Kansai (%)", "Concentración de Consumo Kanto-Kansai (%)"],
                "datasets": [{"label": "Porcentaje (%)", "data": [92.9, 90.0, 100.0], "backgroundColor": ["#6c5777", "#735664", "#3d6751"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Indicadores Geográficos y Concentración Urbana (%)"}}}
        }
    }
]"""

# Replace in generate_content.py
# find where japon_indicators starts and where it ends (which is at the end of the file before next stuff? no, japon_indicators is at lines 248-482)
start_idx = content.find("japon_indicators = [")
# find where japon_indicators block ends. It ends at the closing square bracket of japon_indicators, which is followed by \n\n# Let's write the functions...
# Let's search for "def generate_stars"
end_idx = content.find("def generate_stars")
if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + japon_indicators_updated + "\n\n" + content[end_idx:]
    with codecs.open('e:\\pagina web aldea global 2\\generate_content.py', 'w', 'utf-8') as f:
        f.write(new_content)
    print("generate_content.py successfully updated with new Japan indicators.")
else:
    print("Could not find start or end of japon_indicators in generate_content.py")
