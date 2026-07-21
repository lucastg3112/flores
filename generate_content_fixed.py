import re
import json

# Data for Emiratos Árabes Unidos (15 indicators)
eau_indicators = [
    {
        "title": "1. Población total",
        "icon": "group",
        "description": "La población de Emiratos Árabes Unidos ha mantenido una tendencia creciente durante los últimos años gracias al dinamismo económico, la llegada de trabajadores extranjeros y el continuo desarrollo de sectores como el turismo, el comercio y la construcción. Este crecimiento amplía el tamaño del mercado potencial para empresas internacionales, ya que incrementa la cantidad de consumidores y la demanda de bienes y servicios. Para Dreams Flowers S.A.S., una mayor población implica un mayor número de clientes potenciales en segmentos como hoteles, restaurantes, organizadores de eventos, floristerías y consumidores finales. Además, el país cuenta con una población multicultural que celebra festividades de diversas tradiciones, favoreciendo el consumo de flores durante todo el año.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_1",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "Población total", "data": [9445785, 9401038, 9575152, 10074977, 10483751, 10986400], "borderColor": "#3d6751", "backgroundColor": "#3d675120", "fill": "true"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Población total - Emiratos Árabes Unidos (2019-2024)"}}}
        }
    },
    {
        "title": "2. PIB per cápita",
        "icon": "attach_money",
        "description": "El PIB per cápita refleja el elevado poder adquisitivo de la población emiratí. Emiratos Árabes Unidos se ubica entre las economías con mayores ingresos por habitante, lo que favorece el consumo de productos premium y diferenciados. Para Dreams Flowers S.A.S. este aspecto resulta especialmente importante porque las flores de exportación compiten por calidad, frescura y exclusividad más que por precio. Un consumidor con mayor capacidad económica está dispuesto a pagar por arreglos florales de alto valor para eventos, hoteles de lujo, oficinas y celebraciones. Asimismo, este indicador evidencia estabilidad económica y capacidad de mantener una demanda constante de bienes importados.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_2",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "PIB per cápita (US$ corrientes)", "data": [45938.6, 37991.7, 44118.5, 50759.8, 49850.7, 50273.5], "borderColor": "#4CAF50", "backgroundColor": "#4CAF5020", "fill": "true"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "PIB per cápita de Emiratos Árabes Unidos (2019-2024)"}}}
        }
    },
    {
        "title": "3. Importaciones de flores cortadas",
        "icon": "local_shipping",
        "description": "Las importaciones de flores cortadas permiten medir directamente la demanda existente para el producto que comercializa Dreams Flowers S.A.S. Los datos muestran que Emiratos Árabes Unidos depende del abastecimiento internacional para satisfacer gran parte del consumo interno, debido a sus limitaciones climáticas para la producción de flores ornamentales. Esta característica convierte al país en un mercado atractivo para exportadores colombianos. Además, el crecimiento del turismo, la hotelería y la realización de eventos internacionales incrementan continuamente el consumo de flores frescas. El indicador confirma que existe una oportunidad real para ingresar al mercado.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_3",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Importaciones (US$)", "data": [50354898.73, 45899210.25, 64203566.14, 69741088.09, 78773261.98], "backgroundColor": ["#5c8397", "#b85c5c", "#8eb85c", "#945cb8", "#5cb8b4"]}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Importaciones de flores cortadas EAU (2019-2023)"}}}
        }
    },
    {
        "title": "4. Estabilidad política",
        "icon": "account_balance",
        "description": "La estabilidad política de Emiratos Árabes Unidos constituye uno de los principales factores que respaldan la confianza de inversionistas y empresas extranjeras. El país mantiene un entorno institucional sólido, bajos niveles de conflictividad y políticas orientadas al crecimiento económico. Estas condiciones reducen la incertidumbre para las operaciones internacionales, facilitan la planificación de inversiones de largo plazo y fortalecen las relaciones comerciales. Para Dreams Flowers S.A.S., un entorno político estable disminuye el riesgo de interrupciones en la cadena de suministro.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_4",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Índice WGI", "data": [0.65, 0.60, 0.61, 0.73, 0.67], "borderColor": "#3b82f6", "backgroundColor": "#3b82f620"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Estabilidad política (2019-2023)"}}}
        }
    },
    {
        "title": "5. Índice de Libertad Económica",
        "icon": "show_chart",
        "description": "El elevado índice de libertad económica evidencia un entorno favorable para el emprendimiento, la inversión y el comercio internacional. Emiratos Árabes Unidos promueve políticas que facilitan la actividad empresarial, la protección de la inversión y la apertura comercial. Estas características reducen barreras para empresas extranjeras y mejoran la competitividad del mercado. Para Dreams Flowers S.A.S., significa mayores posibilidades de establecer alianzas comerciales, importar productos con mayor facilidad y desarrollar una estrategia de expansión sostenible.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_5",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Índice de Libertad Económica", "data": [77.6, 76.2, 76.9, 70.2, 70.8], "borderColor": "#8b5cf6", "backgroundColor": "#8b5cf620"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Índice de Libertad Económica - Emiratos Árabes Unidos"}}}
        }
    },
    {
        "title": "6. Efectividad del Gobierno",
        "icon": "gavel",
        "description": "La efectividad gubernamental refleja la calidad de las instituciones públicas, la eficiencia administrativa y la capacidad del Estado para implementar políticas económicas. Emiratos Árabes Unidos destaca por contar con procesos ágiles, infraestructura moderna y altos niveles de digitalización. Esto facilita el comercio exterior y reduce costos operativos para las empresas. En el caso de Dreams Flowers S.A.S., un gobierno eficiente contribuye a que los procesos logísticos y regulatorios sean más confiables.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_6",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Índice de efectividad del gobierno", "data": [1.4, 1.3, 1.38, 1.32, 1.6], "borderColor": "#10b981", "backgroundColor": "#10b98120", "tension": 0.4}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Efectividad del Gobierno (2019-2023)"}}}
        }
    },
    {
        "title": "7. Usuarios de Internet",
        "icon": "language",
        "description": "La alta penetración de internet posiciona a Emiratos Árabes Unidos como una economía altamente digitalizada. Esto fortalece el comercio electrónico, las estrategias de marketing digital y la comunicación entre empresas y consumidores. Dreams Flowers S.A.S. puede aprovechar este entorno para promocionar sus productos mediante canales digitales, fortalecer su presencia de marca y establecer relaciones comerciales más eficientes.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_7",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Usuarios de Internet (%)", "data": [99.0, 100, 100, 100, 100], "borderColor": "#0ea5e9", "backgroundColor": "#0ea5e920"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Usuarios de Internet en EAU (2019-2023)"}}}
        }
    },
    {
        "title": "8. Índice Global de Innovación",
        "icon": "lightbulb",
        "description": "El buen desempeño de Emiratos Árabes Unidos en el Índice Global de Innovación demuestra un entorno que impulsa la tecnología, la investigación y la transformación digital. Este contexto favorece la adopción de soluciones logísticas y comerciales avanzadas, incrementando la competitividad del mercado. Para Dreams Flowers S.A.S., ingresar a un país innovador representa oportunidades para implementar estrategias modernas de comercialización y distribución.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_8",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "Posición mundial", "data": [34, 33, 31, 32, 32], "borderColor": "#f59e0b", "backgroundColor": "#f59e0b20"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Ranking del Índice Global de Innovación (EAU)"}}, "scales": {"y": {"reverse": "true"}}}
        }
    },
    {
        "title": "9. Emisiones de CO2",
        "icon": "co2",
        "description": "Aunque Emiratos Árabes Unidos mantiene emisiones elevadas por su estructura económica, la tendencia reciente muestra esfuerzos por reducirlas mediante estrategias de sostenibilidad. Este cambio es relevante porque los consumidores y empresas valoran cada vez más las prácticas responsables con el medio ambiente. Dreams Flowers S.A.S. puede fortalecer su propuesta de valor destacando procesos sostenibles y buenas prácticas ambientales.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_9",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "Emisiones (t CO2e)", "data": [26.66732, 26.56611, 26.66825, 25.36906, 24.25728, 24.04322], "borderColor": "#ef4444", "backgroundColor": "#ef444420"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Emisiones de CO2 per cápita - EAU"}}}
        }
    },
    {
        "title": "10. Comercio (% PIB)",
        "icon": "sync_alt",
        "description": "El elevado porcentaje del comercio sobre el PIB confirma que Emiratos Árabes Unidos posee una economía altamente abierta e integrada al comercio mundial. La importancia del comercio exterior demuestra la eficiencia de su infraestructura logística y la facilidad para importar y exportar bienes. Esto representa una ventaja para Dreams Flowers S.A.S., ya que facilita el ingreso de flores colombianas y mejora la competitividad del proceso exportador.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_10",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Comercio (% del PIB)", "data": [163.8221, 181.2919, 182.9094, 185.7417, 199.045], "borderColor": "#14b8a6", "backgroundColor": "#14b8a620", "fill": "true"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Comercio (% del PIB) - Emiratos Árabes Unidos"}}}
        }
    },
    {
        "title": "11. Importaciones (% PIB)",
        "icon": "download",
        "description": "El crecimiento de las importaciones como porcentaje del PIB evidencia la fuerte dependencia del país respecto a bienes provenientes del exterior. Esta característica convierte a Emiratos Árabes Unidos en un mercado receptivo a proveedores internacionales. Para Dreams Flowers S.A.S., significa una oportunidad para competir en un entorno donde los productos importados forman parte habitual de la oferta comercial.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_11",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Importaciones de bienes y servicios (% del PIB)", "data": [70.52, 83.22, 82.27, 83.69, 92.2], "borderColor": "#6366f1", "backgroundColor": "#6366f120"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Importaciones de bienes y servicios (% del PIB)"}}}
        }
    },
    {
        "title": "12. Exportaciones (% PIB)",
        "icon": "upload",
        "description": "El alto nivel de exportaciones refleja una economía dinámica y con excelente conectividad internacional. La infraestructura portuaria y aeroportuaria facilita el movimiento de mercancías y fortalece la competitividad del país. Estas condiciones benefician indirectamente a las empresas extranjeras que desean establecer relaciones comerciales con Emiratos Árabes Unidos.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_12",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "Exportaciones de bienes y servicios (% del PIB)", "data": [93.30231, 98.0725, 100.6426, 102.052, 106.8461], "borderColor": "#ec4899", "backgroundColor": "#ec489920", "fill": "true"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Exportaciones de bienes y servicios (% del PIB) - EAU"}}}
        }
    },
    {
        "title": "13. IED (% PIB)",
        "icon": "trending_up",
        "description": "La inversión extranjera directa evidencia la confianza que tienen los inversionistas internacionales en la economía emiratí. La estabilidad de los flujos de inversión confirma que el país ofrece condiciones favorables para desarrollar negocios de largo plazo. Para Dreams Flowers S.A.S., este indicador reduce la percepción de riesgo y demuestra que el mercado continúa atrayendo capital internacional.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_13",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023"],
                "datasets": [{"label": "IED neta (% del PIB)", "data": [4.119286, 5.567357, 4.892306, 4.445914, 5.87184], "borderColor": "#84cc16", "backgroundColor": "#84cc1620"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Inversión Extranjera Directa neta (% del PIB)"}}}
        }
    },
    {
        "title": "14. Capitalización bursátil",
        "icon": "candlestick_chart",
        "description": "El notable crecimiento de la capitalización bursátil entre 2019 y 2024 demuestra el fortalecimiento del mercado financiero de Emiratos Árabes Unidos. Un mercado de capitales sólido mejora la disponibilidad de recursos para las empresas, incrementa la confianza de los inversionistas y fortalece el desarrollo económico. Para Dreams Flowers S.A.S., este entorno favorece la estabilidad del mercado y crea mejores condiciones para la expansión internacional.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_14",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "Capitalización bursátil (% del PIB)", "data": [56.88036, 82.54857, 131.3938, 170.8167, 190.2272, 190.8591], "borderColor": "#d946ef", "backgroundColor": "#d946ef20", "fill": "true"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Capitalización bursátil de empresas nacionales cotizadas"}}}
        }
    },
    {
        "title": "15. Valor de acciones negociadas",
        "icon": "swap_horiz",
        "description": "El aumento del valor de las acciones negociadas confirma que el mercado bursátil emiratí mantiene un elevado nivel de liquidez y dinamismo. Aunque se observó una moderación después de 2022, el indicador continúa por encima de los niveles prepandemia, reflejando confianza de los inversionistas y un sistema financiero activo. Este contexto fortalece el atractivo del país para nuevas inversiones y beneficia indirectamente a empresas extranjeras como Dreams Flowers S.A.S.",
        "impact": "Muy alto",
        "rating": 5,
        "chart_id": "chart_eau_15",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2019", "2020", "2021", "2022", "2023", "2024"],
                "datasets": [{"label": "Acciones negociadas (% del PIB)", "data": [6.741077, 10.50203, 28.32565, 28.64126, 21.31852, 21.82124], "borderColor": "#06b6d4", "backgroundColor": "#06b6d420", "tension": 0.4}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Valor total de las acciones negociadas (% del PIB)"}}}
        }
    }
]

japon_indicators = [
    {
        "title": "1. Índice de Percepción de la Corrupción",
        "icon": "policy",
        "description": "Japón es un país que mantiene un bajo nivel de corrupción y una muy buena transparencia institucional por lo que brinda seguridad a las empresas que desean exportar flores al país. Un entorno con una tasa de menor corrupción reduce los riesgos a la hora de hacer trámites aduaneros, permisos sanitarios y procesos de importación. Esto permite que los exportadores colombianos planifiquen sus operaciones con mayor confianza y disminuyan los costos asociados a problemas administrativos. Aunque el puntaje ha disminuido ligeramente en los últimos años, Japón continúa siendo uno de los mercados más confiables para el comercio internacional.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_1",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Puntaje IPC (0-100)", "data": [73, 73, 73, 71, 71], "backgroundColor": "#2563eb"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Puntaje IPC (0-100)"}}, "scales": {"y": {"min": 70, "max": 74}}}
        }
    },
    {
        "title": "2. Estado de Derecho (Rule of Law)",
        "icon": "balance",
        "description": "Japón es un país que cuenta con un sistema legal muy sólido que protege los contratos, la propiedad intelectual y el cumplimiento de las normas comerciales. Para una empresa exportadora de flores esto da mayor seguridad en las negociaciones con distribuidores japoneses y menor riesgo de incumplimientos contractuales. También la estabilidad institucional facilita las relaciones comerciales de largo plazo y genera confianza para realizar inversiones que tengan que ver con la exportación.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_2",
        "chart_config": {
            "type": "pie",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Percentil (%)", "data": [89, 89, 90, 90, 90], "backgroundColor": ["#0ea5e9", "#f97316", "#22c55e", "#ef4444", "#a855f7"]}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Percentil (%) Rule of Law"}}}
        }
    },
    {
        "title": "3. Requisitos Fitosanitarios para Importación de Flores",
        "icon": "eco",
        "description": "Japón exige unos estrictos controles fitosanitarios para la importación de flores con el fin de evitar el ingreso de plagas y enfermedades. Aunque estos requisitos incrementan la preparación documental y los controles de calidad, también garantizan un mercado con altos estándares sanitarios. Para los exportadores colombianos al cumplir estas normas mejora la reputación del producto y facilita el acceso permanente al mercado japonés.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_3",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Certificado fitosanitario", "Inspección sanitaria", "Control de plagas", "Normativa estable"],
                "datasets": [{"label": "Nivel de Exigencia", "data": [100, 100, 90, 100], "backgroundColor": ["#eab308", "#3b82f6", "#ef4444", "#22c55e"]}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Requisitos Fitosanitarios"}}}
        }
    },
    {
        "title": "4. Arancel aplicado a flores importadas",
        "icon": "money_off",
        "description": "Japón aplica aranceles muy bajos o nulos para muchas flores cortadas importadas, favoreciendo la competitividad de los exportadores internacionales lo cual permite que empresas colombianas ofrezcan flores a precios más competitivos sin enfrentar altos costos tributarios al ingresar al mercado japonés ya que la reducción de barreras arancelarias impulsa el comercio y facilita la expansión internacional del sector floricultor.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_4",
        "chart_config": {
            "type": "line",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Arancel promedio (%)", "data": [0, 0, 0, 0, 0], "borderColor": "#06b6d4", "backgroundColor": "#06b6d4", "fill": "false"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Arancel promedio aplicable a flores"}}, "scales": {"y": {"min": 0, "max": 100}}}
        }
    },
    {
        "title": "5. Índice de Desempeño Logístico (LPI)",
        "icon": "local_shipping",
        "description": "Japón posee una de las mejores infraestructuras logísticas del mundo, con puertos, aeropuertos y redes de transporte altamente eficientes. Para una empresa exportadora de flores esto reduce los tiempos de entrega y ayuda a conservar la calidad del producto por lo cual es un aspecto fundamental debido a su naturaleza perecedera, además también facilita la distribución hacia mayoristas y minoristas en diferentes regiones del país.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_5",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2018", "2023"],
                "datasets": [{"label": "Puntaje LPI", "data": [3.99, 4.1], "backgroundColor": "#0284c7"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Índice de Desempeño Logístico"}}}
        }
    },
    {
        "title": "6. Tiempo promedio para el despacho aduanero",
        "icon": "timer",
        "description": "Japón es un país que cuenta con procesos aduaneros modernos y altamente digitalizados, lo que permite que las mercancías sean inspeccionadas y liberadas en tiempos reducidos cuando cumplen con todos los requisitos legales y sanitarios. Para la exportación de flores frescas, un despacho rápido es fundamental, ya que ayuda a conservar su calidad y prolongar su vida útil durante la comercialización.",
        "impact": "Muy favorable",
        "rating": 5,
        "chart_id": "chart_japon_6",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["2021", "2022", "2023", "2024", "2025"],
                "datasets": [{"label": "Tiempo promedio (días)", "data": [1.5, 1.5, 1.5, 1.5, 1.5], "backgroundColor": "#0369a1"}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Tiempo promedio de despacho"}}}
        }
    },
    {
        "title": "7. Regulación fitosanitaria y barreras no arancelarias",
        "icon": "warning",
        "description": "Japón aplica una de las políticas de bioseguridad y protección agrícola más estrictas del planeta a través de la Ley de Protección de Plantas (MAFF). Durante 2023-2024, el entorno regulatorio se volvió aún más restrictivo, comenzando la exigencia estricta de Certificados Fitosanitarios. Cualquier discrepancia resulta en rechazo. Las inspecciones son minuciosas y la detección de un insecto paraliza el lote, requiriendo fumigación con bromuro de metilo que daña la flor. Representa el mayor cuello de botella operativo.",
        "impact": "Riesgo Alto",
        "rating": 2,
        "chart_id": "chart_japon_7",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Control de Plagas", "Documentación", "Inspección Física", "Tolerancia a insectos"],
                "datasets": [{"label": "Nivel de Exigencia / Riesgo", "data": [100, 100, 100, 0], "backgroundColor": ["#ea580c", "#c2410c", "#9a3412", "#ef4444"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Embudo de Riesgo Alto MAFF 2023-2024"}}}
        }
    },
    {
        "title": "8. Estructura de Distribución y Logística",
        "icon": "hub",
        "description": "La comercialización interna de flores en Japón se rige por un canal de distribución tradicional altamente estructurado (Mercados de Flores Kaki, ej. Ota Floriculture Auction). Aunque asegura transparencia de precios, logística de frío impecable y pago garantizado, añade múltiples intermediarios (Importador → Mercado de Subasta → Mayorista secundario → Floristería minorista). Esto encarece el precio final y reduce el margen del exportador. La rigidez dificulta contratos directos con supermercados.",
        "impact": "Riesgo Medio",
        "rating": 3,
        "chart_id": "chart_japon_8",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Subastas autorizadas (Kaki)", "Ventas Directas a minoristas"],
                "datasets": [{"label": "Participación de mercado (%)", "data": [85, 15], "backgroundColor": "#0f766e"}]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura de Distribución (Japón 2025-2026)"}}}
        }
    },
    {
        "title": "9. Canales de Comercialización Digital (E-commerce)",
        "icon": "devices",
        "description": "Durante el periodo 2023-2024, el mercado consolidó una transición digital. El e-commerce de flores alcanzó USD 350 millones. Impulsado por el auge de suscripciones florales (Post-delivery / Flores en el Buzón) como Bloomee, y la integración de IA y logística de última milla. Esto abre una ruta alternativa para saltarse el costoso esquema de subastas físicas y negociar volúmenes estables con agregadores digitales.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_9",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Crecimiento interanual", "Participación del commerce"],
                "datasets": [{"label": "Porcentaje (%)", "data": [12, 22], "backgroundColor": ["#f97316", "#2563eb"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Canales Digitales (Japón 2023-2024)"}}}
        }
    },
    {
        "title": "10. Sostenibilidad, Certificaciones Ambientales",
        "icon": "energy_savings_leaf",
        "description": "El consumidor corporativo incrementó la demanda de flores con certificaciones MPS y Fairtrade. Las grandes corporaciones priorizan proveedores con bajas huellas de carbono y uso responsable de pesticidas. Además, exigen empaque optimizado y libre de plásticos de un solo uso debido a las altas emisiones del transporte aéreo. Esto es una ventaja masiva para exportadores premium pero una barrera de entrada para los que no tienen certificaciones.",
        "impact": "Favorable con condiciones",
        "rating": 4,
        "chart_id": "chart_japon_10",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Demanda certificada MPS/Fairtrade", "Preferencia sin plásticos"],
                "datasets": [
                    {"label": "2023", "data": [45, 30], "backgroundColor": "#1e40af"},
                    {"label": "2024", "data": [65, 55], "backgroundColor": "#f97316"}
                ]
            },
            "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Sostenibilidad y Certificaciones"}}}
        }
    },
    {
        "title": "11. Usuarios de Internet y Conectividad Digital",
        "icon": "wifi",
        "description": "Japón posee uno de los ecosistemas digitales más avanzados, con penetración de internet del 88.2% a inicios de 2025. La adopción de redes sociales abarca el 78.6% de la población. La excelente conectividad facilita estrategias de marketing digital de precisión (pautas hiperlocalizadas), permitiendo a marcas premium conectar directa y rápidamente con un consumidor de alto poder adquisitivo.",
        "impact": "Muy Favorable",
        "rating": 5,
        "chart_id": "chart_japon_11",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Penetración Internet", "Adopción Redes Sociales (18+)", "Adopción Redes Sociales Total"],
                "datasets": [{"label": "Porcentaje (%)", "data": [88.2, 87.0, 78.6], "backgroundColor": ["#1e3a8a", "#3b82f6", "#60a5fa"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Infraestructura Digital y Conectividad (2024-2025)"}}}
        }
    },
    {
        "title": "12. Hábitos de consumo y significación floral",
        "icon": "psychology",
        "description": "La cultura japonesa tiene un lazo espiritual milenario con las flores (Ikebana, Hanakotoba). El consumo está estructurado en torno a un calendario estricto de rituales religiosos, funerales (Obon) y estaciones. Existe una demanda obligatoria y se valora de forma extrema la perfección simétrica y frescura. Los exportadores de variedades raras o altísima calidad estética encuentran nichos de precio sumamente elevados. No se considera un gasto superfluo.",
        "impact": "Muy Favorable",
        "rating": 5,
        "chart_id": "chart_japon_12",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Tradición Espiritual", "Rituales", "Calidad", "Nuevas Tendencias"],
                "datasets": [{"label": "Importancia", "data": [100, 100, 100, 60], "backgroundColor": ["#db2777", "#9d174d", "#15803d", "#0d9488"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura del Consumo Floral"}}}
        }
    },
    {
        "title": "13. Acceso a Tecnología en la Cadena de Suministro",
        "icon": "precision_manufacturing",
        "description": "La logística hortícola japonesa se transforma por tecnologías avanzadas para mitigar escasez de mano de obra. El mercado de la cadena de frío (cold chain) se valoró en USD 18,000 millones, con integración masiva de sensores IoT para monitoreo térmico en tiempo real. Las subastas operan con sistemas robotizados. El uso de refrigeración de última generación y IA en almacenes reduce mermas a <5%, asegurando la preservación de la calidad.",
        "impact": "Muy Favorable",
        "rating": 5,
        "chart_id": "chart_japon_13",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Efectividad de Control IoT (%)", "Mermas de Producto (%)"],
                "datasets": [{"label": "Indicador", "data": [100, 4.9], "backgroundColor": ["#0f766e", "#ef4444"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Acceso a Tecnología e Innovación (2024-2025)"}}}
        }
    },
    {
        "title": "14. Geográficos relevantes y Conectividad de Infraestructura",
        "icon": "map",
        "description": "Con un índice de urbanización del 92.9%, el consumo se concentra en el megacorredor Kanto-Kansai. Los aeropuertos de Narita y Kansai absorben más del 90% de la carga de flor fresca. La altísima concentración poblacional facilita una logística capilar unificada. Las barreras climáticas que limitan la producción local (tifones, inviernos) consolidan la necesidad de un flujo constante de importaciones, aunque representan un riesgo puntual de retraso.",
        "impact": "Favorable",
        "rating": 4,
        "chart_id": "chart_japon_14",
        "chart_config": {
            "type": "bar",
            "data": {
                "labels": ["Índice de Urbanización", "Carga Flor Narita y Kansai"],
                "datasets": [{"label": "Porcentaje (%)", "data": [92.9, 90.0], "backgroundColor": ["#1e3a8a", "#2563eb"]}]
            },
            "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Indicadores Geográficos y Conectividad"}}}
        }
    }
]


def generate_stars(rating):
    stars = ""
    for _ in range(rating):
        stars += '<span class="material-symbols-outlined text-yellow-400" style="font-variation-settings: \'FILL\' 1;">star</span>'
    for _ in range(5 - rating):
        stars += '<span class="material-symbols-outlined text-gray-300" style="font-variation-settings: \'FILL\' 1;">star</span>'
    return stars

def build_html_for_country(indicators, country_name, color):
    html = ""
    for idx, ind in enumerate(indicators):
        html += f'''
                        <!-- Indicador {idx+1} -->
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow">
                            <div class="p-6 md:p-8">
                                <h2 class="font-headline-md text-3xl mb-3 flex items-center gap-4" style="color: {color};">
                                    <div class="icon-circle w-14 h-14 rounded-full flex items-center justify-center shrink-0" style="background-color: {color}20; color: {color};">
                                        <span class="material-symbols-outlined text-3xl" style="font-variation-settings: 'FILL' 1;">{ind["icon"]}</span>
                                    </div>
                                    {ind["title"]}
                                </h2>
                                
                                <div class="grid md:grid-cols-2 gap-8 items-start mt-6">
                                    <!-- Texto -->
                                    <div class="space-y-4">
                                        <div class="prose max-w-none">
                                            <p class="text-base leading-relaxed text-gray-700">{ind["description"]}</p>
                                        </div>
                                        
                                        <div class="bg-gray-50 rounded-xl p-4 mt-6">
                                            <div class="flex items-center justify-between mb-2">
                                                <span class="font-semibold text-gray-700">Impacto en internacionalización:</span>
                                                <span class="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-medium">{ind["impact"]}</span>
                                            </div>
                                            <div class="flex items-center justify-between">
                                                <span class="font-semibold text-gray-700">Calificación:</span>
                                                <div class="flex gap-1">
                                                    {generate_stars(ind["rating"])}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <!-- Gráfica -->
                                    <div class="bg-gray-50 rounded-xl p-4 border border-gray-100 h-full flex flex-col justify-center min-h-[300px]">
                                        <canvas id="{ind["chart_id"]}"></canvas>
                                    </div>
                                </div>
                            </div>
                        </div>
        '''
    return html

def build_js_for_country(indicators):
    js = ""
    for ind in indicators:
        js += f'''
        const ctx_{ind["chart_id"]} = document.getElementById('{ind["chart_id"]}');
        if (ctx_{ind["chart_id"]}) {{
            new Chart(ctx_{ind["chart_id"]}, {json.dumps(ind["chart_config"])});
        }}
        '''
    return js

html_japon = f'''<div id="country-japon" class="country-content hidden">
                    <div class="space-y-12">
{build_html_for_country(japon_indicators, 'Japón', '#d946ef')}
                    </div>
                </div>'''

html_eau = f'''<div id="country-arabia" class="country-content hidden">
                    <div class="space-y-12">
{build_html_for_country(eau_indicators, 'Emiratos Árabes', '#0ea5e9')}
                    </div>
                </div>'''

js_charts = build_js_for_country(japon_indicators) + build_js_for_country(eau_indicators)

with open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace placeholders
content = re.sub(
    r'<div id="country-japon"[^>]*>.*?<!-- Japan indicators will be populated here -->.*?</div>\s*</div>',
    html_japon.replace('\\', '\\\\'),
    content,
    flags=re.DOTALL
)
content = re.sub(
    r'<div id="country-arabia"[^>]*>.*?<!-- UAE indicators will be populated here -->.*?</div>\s*</div>',
    html_eau.replace('\\', '\\\\'),
    content,
    flags=re.DOTALL
)

# Inject JS
js_injection = f'''
        // JS Injected for Japan and UAE
        {js_charts}
    </script>
</body>
'''
content = content.replace('</script>\n</body>', js_injection)

with open('e:\\pagina web aldea global 2\\entregas\\entrega-3\\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Process completed successfully.")
