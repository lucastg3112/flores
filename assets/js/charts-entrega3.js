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
                labels: ["Distancia al Poder (Alta Jerarquía)"], 
                datasets: [
                    { label: "India", data: [77], backgroundColor: C.primary, borderWidth: 1 }
                ] 
            },
            options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', scales: { x: { max: 100 } } }
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
            type: "pie", 
            data: { 
                labels: ["Retención/Cuarentena", "Destrucción Inmediata"], 
                datasets: [{ 
                    label: "Riesgo ante Incumplimiento Documental/Plagas", 
                    data: [50, 50],
                    backgroundColor: [C.tertiary, C.error],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        },
        5: { 
            type: "bar", 
            data: { 
                labels: ["Tribunales Ordinarios Indios"], 
                datasets: [{ 
                    label: "Tiempo de Resolución de Disputas (Días)", 
                    data: [1400],
                    backgroundColor: C.error,
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y', scales: { x: { min: 0, max: 2000 } } }
        },
        6: { 
            type: "line", 
            data: { 
                labels: ["Periodo 1", "Periodo 2", "Periodo 3", "Periodo 4"], 
                datasets: [{ 
                    label: "Incertidumbre: Impacto de Barreras Dinámicas", 
                    data: [10, 40, 20, 60],
                    backgroundColor: C.error, borderColor: C.error, borderWidth: 3, stepped: true
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
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
                labels: ["Triangulación (Hub Múltiple)"], 
                datasets: [{ 
                    label: "Lead Time de Vuelo + Tránsito (Horas >60-72h)", 
                    data: [72],
                    backgroundColor: C.error,
                    borderWidth: 1 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false, indexAxis: 'y' }
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
            type: "doughnut", 
            data: { 
                labels: ["IED Automática Permitida"], 
                datasets: [{ 
                    label: "Inversión Extranjera en Cadena de Frío (%)", 
                    data: [100],
                    backgroundColor: [C.primary],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
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
                labels: ["Repatriación Permitida (Previa Retención/Certificación)"], 
                datasets: [{ 
                    label: "Libre Convertibilidad (%)", 
                    data: [100],
                    backgroundColor: [C.primary],
                    borderWidth: 0 
                }] 
            },
            options: { responsive: true, maintainAspectRatio: false }
        }
    }
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