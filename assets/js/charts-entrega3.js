const chartInstances = {};
const C = { primary: "#3d6751", primaryContainer: "#a8d5ba", secondary: "#735664", tertiary: "#6c5777", error: "#ba1a1a" };
const chartDataConfig = {
    "india": {
        1: { 
            type: "line", 
            data: { 
                labels: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"], 
                datasets: [{ 
                    label: "Índice de Demanda Relativa (Base 100)", 
                    data: [350, 400, 100, 100, 100, 100, 100, 100, 150, 300, 400, 350],
                    backgroundColor: "rgba(61, 103, 81, 0.2)",
                    borderColor: C.primary,
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false }, tooltip: { callbacks: { label: function(context) { return 'Demanda: ' + context.raw + ' (Pico Festivo)'; } } } }, scales: { y: { suggestedMin: 0 } } }
        },
        2: { 
            type: "bar", 
            data: { 
                labels: ["Colombia", "India"], 
                datasets: [
                    { label: "Puntaje de Distancia al Poder (Alta Jerarquía)", data: [67, 77], backgroundColor: [C.secondary, C.primary], borderWidth: 1 }
                ] 
            },
            options: { responsive: true, maintainAspectRatio: false, scales: { y: { max: 100, min: 0 } } }
        },
        3: { 
            type: "line", 
            data: { 
                labels: ["Año 1", "Año 2", "Año 3", "Año 4", "Año 5"], 
                datasets: [
                    { label: "Proyección Crecimiento PIB Real (%)", data: [6.1, 6.2, 6.4, 6.5, 6.7], borderColor: C.secondary, borderWidth: 2, tension: 0.2 },
                    { label: "Crecimiento Ingreso Disponible Clase Media (%)", data: [7.0, 7.2, 7.5, 7.8, 8.1], borderColor: C.primary, backgroundColor: C.primaryContainer, borderWidth: 3, fill: true, tension: 0.3 }
                ] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        4: { 
            type: "doughnut", 
            data: { 
                labels: ["Aprobación (Sin Plagas)", "Retención/Fumigación (Errores menores)", "Destrucción (Nematodos)"], 
                datasets: [{ 
                    label: "Probabilidad de Escenarios", 
                    data: [35, 45, 20],
                    backgroundColor: [C.primary, C.tertiary, C.error],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        5: { 
            type: "bar", 
            data: { 
                labels: ["Promedio OCDE", "Colombia", "India"], 
                datasets: [{ 
                    label: "Tiempo de Resolución de Disputas (Días)", 
                    data: [580, 1288, 1400],
                    backgroundColor: [C.primaryContainer, C.tertiary, C.error],
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0 } } }
        },
        6: { 
            type: "line", 
            data: { 
                labels: ["2021", "2022", "2023", "2024"], 
                datasets: [
                    { label: "Arancel India (Dinámico/Proteccionista)", data: [20, 60, 30, 60], backgroundColor: C.error, borderColor: C.error, borderWidth: 3, tension: 0.1 },
                    { label: "Promedio Global (Estable)", data: [10, 10, 10, 10], backgroundColor: C.primary, borderColor: C.primary, borderWidth: 2, borderDash: [5, 5], tension: 0 }
                ] 
            },
            options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0, max: 100 } } }
        },
        7: { 
            type: "bar", 
            data: { 
                labels: ["Tolerancia Máxima (<20m)", "Temp. Verano India"], 
                datasets: [
                    { label: "Temperatura Promedio (°C)", data: [20, 40], backgroundColor: [C.primaryContainer, C.error] }
                ] 
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
        },
        8: { 
            type: "bar", 
            data: { 
                labels: ["Rango Inferior (Horas)", "Rango Superior (Horas)"], 
                datasets: [{ 
                    label: "Despacho Aeroportuario (ICEGATE)", 
                    data: [12, 24],
                    backgroundColor: C.primary, borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y' }
        },
        9: { 
            type: "line", 
            data: { 
                labels: ["Base", "Año 1", "Año 2", "Año 3"], 
                datasets: [{ 
                    label: "Crecimiento E-commerce Bienes Premium (CAGR >20%)", 
                    data: [100, 120, 144, 172],
                    backgroundColor: C.secondary, borderColor: C.secondary, borderWidth: 3, fill: true, tension: 0.4
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        10: { 
            type: "doughnut", 
            data: { 
                labels: ["Valor Aduanero Base (CIF)", "Impacto Punitivo (Arancel BCD)"], 
                datasets: [{ 
                    label: "Impacto del BCD (%)", 
                    data: [100, 60],
                    backgroundColor: [C.primaryContainer, C.error],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        11: { 
            type: "bar", 
            data: { 
                labels: ["Vuelo Directo (Ideal)", "Triangulación Hub Múltiple"], 
                datasets: [{ 
                    label: "Tiempo de Tránsito (Horas)", 
                    data: [24, 72],
                    backgroundColor: [C.primaryContainer, C.error],
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0 } } }
        },
        12: { 
            type: "pie", 
            data: { 
                labels: ["Kenia (Rosas Standard)", "Países Bajos (Genética)", "Otros Orígenes"], 
                datasets: [{ 
                    label: "Dominio de Proveedores en el Mercado", 
                    data: [60, 30, 10],
                    backgroundColor: [C.error, C.tertiary, C.primaryContainer],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        13: { 
            type: "bar", 
            data: { 
                labels: ["2021", "2022", "2023", "2024 (Proy.)"], 
                datasets: [{ 
                    label: "Inversión Extranjera en Cadena de Frío (M USD)", 
                    data: [45, 78, 120, 190],
                    backgroundColor: C.primary,
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 0 } } }
        },
        14: { 
            type: "bar", 
            data: { 
                labels: ["Exportación Simple", "Inversión B2B (Joint Venture)"], 
                datasets: [{ 
                    label: "Amortiguación Estratégica del Arancel del 60%", 
                    data: [20, 80],
                    backgroundColor: [C.tertiary, C.primary],
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
        },
        15: { 
            type: "pie", 
            data: { 
                labels: ["Repatriación Neta", "Retención Impositiva", "Costos de Auditoría"], 
                datasets: [{ 
                    label: "Distribución de Flujos (%)", 
                    data: [75, 20, 5],
                    backgroundColor: [C.primary, C.error, C.tertiary],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        }
    },
    "japon": {"1": {"type": "bar", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Puntaje IPC (0-100)", "data": [73, 73, 73, 71, 71], "backgroundColor": "#735664"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Puntaje IPC (0-100) - Japón"}}, "scales": {"y": {"min": 70, "max": 75}}, "maintainAspectRatio": false}}, "2": {"type": "pie", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Percentil (%)", "data": [89, 89, 90, 90, 90], "backgroundColor": ["#ba1a1a", "#3d6751", "#735664", "#a8d5ba", "#6c5777"]}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Percentil (%) Estado de Derecho"}}, "maintainAspectRatio": false}}, "3": {"type": "bar", "data": {"labels": ["Certificado fitosanitario", "Inspección sanitaria", "Control de plagas", "Normativa estable"], "datasets": [{"label": "Nivel de Exigencia", "data": [100, 100, 90, 100], "backgroundColor": ["#735664", "#735664", "#a8d5ba", "#735664"]}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Requisitos Fitosanitarios de Importación"}}, "maintainAspectRatio": false}}, "4": {"type": "line", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Arancel promedio (%)", "data": [0, 0, 0, 0, 0], "borderColor": "#735664", "backgroundColor": "#73566420", "fill": false}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Arancel Promedio Aplicado a Flores (%)"}}, "scales": {"y": {"min": 0, "max": 10}}, "maintainAspectRatio": false}}, "5": {"type": "bar", "data": {"labels": ["2018", "2023"], "datasets": [{"label": "Puntaje LPI", "data": [3.99, 4.1], "backgroundColor": "#735664"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Índice de Desempeño Logístico (LPI)"}}, "scales": {"y": {"min": 0, "max": 5}}, "maintainAspectRatio": false}}, "6": {"type": "bar", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Tiempo promedio (días)", "data": [1.5, 1.5, 1.5, 1.5, 1.5], "backgroundColor": "#6c5777"}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Tiempo Promedio de Despacho Aduanero (Días)"}}, "scales": {"x": {"min": 0, "max": 3}}, "maintainAspectRatio": false}}, "7": {"type": "bar", "data": {"labels": ["Control de Plagas", "Documentación", "Inspección Física", "Tolerancia a Plagas (insectos)", "Riesgo Pérdida (Fumigación)"], "datasets": [{"label": "Exigencia / Margen de Tolerancia (%)", "data": [100, 100, 100, 0, 10], "backgroundColor": ["#ba1a1a", "#ba1a1a", "#ba1a1a", "#a8d5ba", "#735664"]}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Control Fitosanitario en Aduana de Japón (%)"}}, "maintainAspectRatio": false}}, "8": {"type": "bar", "data": {"labels": ["Subastas Públicas (Kaki / Ota)", "Ventas Directas a Minoristas"], "datasets": [{"label": "Participación de Mercado (%)", "data": [85, 15], "backgroundColor": "#6c5777"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Estructura de Distribución Floral en Japón (%)"}}, "maintainAspectRatio": false}}, "9": {"type": "bar", "data": {"labels": ["Crecimiento interanual", "Participación de mercado e-commerce"], "datasets": [{"label": "2023", "data": [10, 18], "backgroundColor": "#3d6751"}, {"label": "2024", "data": [12, 22], "backgroundColor": "#735664"}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Canales Digitales e-commerce y Suscripciones (%)"}}, "maintainAspectRatio": false}}, "10": {"type": "bar", "data": {"labels": ["Flores Certificadas (MPS/Fairtrade)", "Empaques Ecológicos / Libres de Plástico"], "datasets": [{"label": "2023", "data": [40, 45], "backgroundColor": "#3d6751"}, {"label": "2024", "data": [60, 80], "backgroundColor": "#735664"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Exigencia de Sostenibilidad y Empaques Ecológicos (%)"}}, "maintainAspectRatio": false}}, "11": {"type": "bar", "data": {"labels": ["Penetración Internet (Total)", "Adopción Redes Sociales (Adultos 18+)", "Adopción Redes Sociales (Total)"], "datasets": [{"label": "Porcentaje (%)", "data": [88.2, 87.0, 78.6], "backgroundColor": ["#6c5777", "#735664", "#3d6751"]}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Infraestructura Digital y Conectividad (%)"}}, "maintainAspectRatio": false}}, "12": {"type": "bar", "data": {"labels": ["Tradición Espiritual (Ikebana)", "Rituales Obligatorios (Obon)", "Exigencia Calidad Física", "Tendencias Digitales Urbanas"], "datasets": [{"label": "Nivel de Importancia / Adopción (%)", "data": [100, 100, 100, 80], "backgroundColor": ["#735664", "#a8d5ba", "#3d6751", "#3d6751"]}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Estructura del Consumo Floral en Japón (%)"}}, "maintainAspectRatio": false}}, "13": {"type": "bar", "data": {"labels": ["Inversión Cadena de Frío (B USD)", "Efectividad Monitoreo IoT (%)", "Pérdida/Mermas de Producto (%)"], "datasets": [{"label": "Valor Absoluto / Eficiencia (%)", "data": [18, 100, 5], "backgroundColor": ["#6c5777", "#6c5777", "#a8d5ba"]}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Distribución Logística y Cadena de Frío"}}, "maintainAspectRatio": false}}, "14": {"type": "bar", "data": {"labels": ["Índice de Urbanización Nacional (%)", "Carga en Aeropuertos Narita/Kansai (%)", "Concentración de Consumo Kanto-Kansai (%)"], "datasets": [{"label": "Porcentaje (%)", "data": [92.9, 90.0, 100.0], "backgroundColor": ["#6c5777", "#735664", "#3d6751"]}]}, "options": {"indexAxis": "y", "responsive": true, "plugins": {"title": {"display": "true", "text": "Indicadores Geográficos y Concentración Urbana (%)"}}, "maintainAspectRatio": false}}},
    "arabia": {"1": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Población total", "data": [9445785, 9401038, 9575152, 10074977, 10483751, 10986400], "borderColor": "#3d6751", "backgroundColor": "#3d675120", "fill": "true"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Población total - Emiratos Árabes Unidos (2019-2024)"}}, "maintainAspectRatio": false}}, "2": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "PIB per cápita (US$ corrientes)", "data": [45938.6, 37991.7, 44118.5, 50759.8, 49850.7, 50273.5], "borderColor": "#735664", "backgroundColor": "#73566420", "fill": "true"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "PIB per cápita de Emiratos Árabes Unidos (2019-2024)"}}, "maintainAspectRatio": false}}, "3": {"type": "bar", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Importaciones (US$)", "data": [50354898.73, 45899210.25, 64203566.14, 69741088.09, 78773261.98], "backgroundColor": ["#a8d5ba", "#ba1a1a", "#6c5777", "#735664", "#6c5777"]}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Importaciones de flores cortadas EAU (2019-2023)"}}, "maintainAspectRatio": false}}, "4": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Índice WGI", "data": [0.65, 0.6, 0.61, 0.73, 0.67], "borderColor": "#735664", "backgroundColor": "#ba1a1a20"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Estabilidad política (2019-2023)"}}, "maintainAspectRatio": false}}, "5": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Índice de Libertad Económica", "data": [77.6, 76.2, 76.9, 70.2, 70.8], "borderColor": "#6c5777", "backgroundColor": "#a8d5ba20"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Índice de Libertad Económica - Emiratos Árabes Unidos"}}, "maintainAspectRatio": false}}, "6": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Índice de efectividad del gobierno", "data": [1.4, 1.3, 1.38, 1.32, 1.6], "borderColor": "#a8d5ba", "backgroundColor": "#a8d5ba20", "tension": 0.4}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Efectividad del Gobierno (2019-2023)"}}, "maintainAspectRatio": false}}, "7": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Usuarios de Internet (%)", "data": [99.0, 100, 100, 100, 100], "borderColor": "#ba1a1a", "backgroundColor": "#ba1a1a20"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Usuarios de Internet en EAU (2019-2023)"}}, "maintainAspectRatio": false}}, "8": {"type": "line", "data": {"labels": ["2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Posición mundial", "data": [34, 33, 31, 32, 32], "borderColor": "#ba1a1a", "backgroundColor": "#a8d5ba20"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Ranking del Índice Global de Innovación (EAU)"}}, "scales": {"y": {"reverse": "true"}}, "maintainAspectRatio": false}}, "9": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Emisiones (t CO2e)", "data": [26.66732, 26.56611, 26.66825, 25.36906, 24.25728, 24.04322], "borderColor": "#a8d5ba", "backgroundColor": "#6c577720"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Emisiones de CO2 per cápita - EAU"}}, "maintainAspectRatio": false}}, "10": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Comercio (% del PIB)", "data": [163.8221, 181.2919, 182.9094, 185.7417, 199.045], "borderColor": "#735664", "backgroundColor": "#3d675120", "fill": "true"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Comercio (% del PIB) - Emiratos Árabes Unidos"}}, "maintainAspectRatio": false}}, "11": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Importaciones de bienes y servicios (% del PIB)", "data": [70.52, 83.22, 82.27, 83.69, 92.2], "borderColor": "#ba1a1a", "backgroundColor": "#3d675120"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Importaciones de bienes y servicios (% del PIB)"}}, "maintainAspectRatio": false}}, "12": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Exportaciones de bienes y servicios (% del PIB)", "data": [93.30231, 98.0725, 100.6426, 102.052, 106.8461], "borderColor": "#a8d5ba", "backgroundColor": "#6c577720", "fill": "true"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Exportaciones de bienes y servicios (% del PIB) - EAU"}}, "maintainAspectRatio": false}}, "13": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "IED neta (% del PIB)", "data": [4.119286, 5.567357, 4.892306, 4.445914, 5.87184], "borderColor": "#a8d5ba", "backgroundColor": "#73566420"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Inversión Extranjera Directa neta (% del PIB)"}}, "maintainAspectRatio": false}}, "14": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Capitalización bursátil (% del PIB)", "data": [56.88036, 82.54857, 131.3938, 170.8167, 190.2272, 190.8591], "borderColor": "#a8d5ba", "backgroundColor": "#3d675120", "fill": "true"}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Capitalización bursátil de empresas nacionales cotizadas"}}, "maintainAspectRatio": false}}, "15": {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Acciones negociadas (% del PIB)", "data": [6.741077, 10.50203, 28.32565, 28.64126, 21.31852, 21.82124], "borderColor": "#735664", "backgroundColor": "#73566420", "tension": 0.4}]}, "options": {"responsive": true, "plugins": {"title": {"display": "true", "text": "Valor total de las acciones negociadas (% del PIB)"}}, "maintainAspectRatio": false}}}
};

window.renderChartsForCountry = function(countryId) {
    const configs = chartDataConfig[countryId];
    if(!configs) return;
    for(let i = 1; i <= 15; i++) {
        const canvasId = "chart_" + countryId + "_" + i;
        const canvas = document.getElementById(canvasId);
        if(!canvas) continue;
        if(chartInstances[canvasId]) { chartInstances[canvasId].destroy(); }
        const ctx = canvas.getContext("2d");
        chartInstances[canvasId] = new Chart(ctx, configs[i]);
    }
};
function initCharts() {
    setTimeout(() => {
        window.renderChartsForCountry("india");
    }, 500);
}
if (document.readyState === 'loading') {
    document.addEventListener("DOMContentLoaded", initCharts);
} else {
    initCharts();
}
