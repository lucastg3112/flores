
        function selectCountry(countryId, btnElement) {
            document.querySelectorAll(".country-tab").forEach(btn => {
                btn.classList.remove("active", "bg-primary", "text-white", "border-primary");
                btn.classList.add("bg-white", "text-gray-700");
                btn.style.backgroundColor = ""; btn.style.color = ""; btn.style.borderColor = "";
            });
            btnElement.classList.add("active");
            btnElement.classList.remove("bg-white", "text-gray-700");
            btnElement.style.backgroundColor = "#3d6751"; btnElement.style.color = "white"; btnElement.style.borderColor = "#3d6751";

            document.querySelectorAll(".country-content").forEach(content => {
                content.classList.add("hidden");
                content.classList.remove("animate-fade-in", "block");
            });
            const selected = document.getElementById("country-" + countryId);
            selected.classList.remove("hidden");
            selected.classList.add("animate-fade-in", "block");

            if (window.renderChartsForCountry) {
                window.renderChartsForCountry(countryId);
            }
        }
    
        // JS Injected for Japan and UAE
        
        const ctx_chart_japon_1 = document.getElementById('chart_japon_1');
        if (ctx_chart_japon_1) {
            new Chart(ctx_chart_japon_1, {"type": "bar", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Puntaje IPC (0-100)", "data": [73, 73, 73, 71, 71], "backgroundColor": "#2563eb"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Puntaje IPC (0-100)"}}, "scales": {"y": {"min": 70, "max": 74}}}});
        }
        
        const ctx_chart_japon_2 = document.getElementById('chart_japon_2');
        if (ctx_chart_japon_2) {
            new Chart(ctx_chart_japon_2, {"type": "pie", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Percentil (%)", "data": [89, 89, 90, 90, 90], "backgroundColor": ["#0ea5e9", "#f97316", "#22c55e", "#ef4444", "#a855f7"]}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Percentil (%) Rule of Law"}}}});
        }
        
        const ctx_chart_japon_3 = document.getElementById('chart_japon_3');
        if (ctx_chart_japon_3) {
            new Chart(ctx_chart_japon_3, {"type": "bar", "data": {"labels": ["Certificado fitosanitario", "Inspecci\u00f3n sanitaria", "Control de plagas", "Normativa estable"], "datasets": [{"label": "Nivel de Exigencia", "data": [100, 100, 90, 100], "backgroundColor": ["#eab308", "#3b82f6", "#ef4444", "#22c55e"]}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Requisitos Fitosanitarios"}}}});
        }
        
        const ctx_chart_japon_4 = document.getElementById('chart_japon_4');
        if (ctx_chart_japon_4) {
            new Chart(ctx_chart_japon_4, {"type": "line", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Arancel promedio (%)", "data": [0, 0, 0, 0, 0], "borderColor": "#06b6d4", "backgroundColor": "#06b6d4", "fill": "false"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Arancel promedio aplicable a flores"}}, "scales": {"y": {"min": 0, "max": 100}}}});
        }
        
        const ctx_chart_japon_5 = document.getElementById('chart_japon_5');
        if (ctx_chart_japon_5) {
            new Chart(ctx_chart_japon_5, {"type": "bar", "data": {"labels": ["2018", "2023"], "datasets": [{"label": "Puntaje LPI", "data": [3.99, 4.1], "backgroundColor": "#0284c7"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "\u00cdndice de Desempe\u00f1o Log\u00edstico"}}}});
        }
        
        const ctx_chart_japon_6 = document.getElementById('chart_japon_6');
        if (ctx_chart_japon_6) {
            new Chart(ctx_chart_japon_6, {"type": "bar", "data": {"labels": ["2021", "2022", "2023", "2024", "2025"], "datasets": [{"label": "Tiempo promedio (d\u00edas)", "data": [1.5, 1.5, 1.5, 1.5, 1.5], "backgroundColor": "#0369a1"}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Tiempo promedio de despacho"}}}});
        }
        
        const ctx_chart_japon_7 = document.getElementById('chart_japon_7');
        if (ctx_chart_japon_7) {
            new Chart(ctx_chart_japon_7, {"type": "bar", "data": {"labels": ["Control de Plagas", "Documentaci\u00f3n", "Inspecci\u00f3n F\u00edsica", "Tolerancia a insectos"], "datasets": [{"label": "Nivel de Exigencia / Riesgo", "data": [100, 100, 100, 0], "backgroundColor": ["#ea580c", "#c2410c", "#9a3412", "#ef4444"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Embudo de Riesgo Alto MAFF 2023-2024"}}}});
        }
        
        const ctx_chart_japon_8 = document.getElementById('chart_japon_8');
        if (ctx_chart_japon_8) {
            new Chart(ctx_chart_japon_8, {"type": "bar", "data": {"labels": ["Subastas autorizadas (Kaki)", "Ventas Directas a minoristas"], "datasets": [{"label": "Participaci\u00f3n de mercado (%)", "data": [85, 15], "backgroundColor": "#0f766e"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura de Distribuci\u00f3n (Jap\u00f3n 2025-2026)"}}}});
        }
        
        const ctx_chart_japon_9 = document.getElementById('chart_japon_9');
        if (ctx_chart_japon_9) {
            new Chart(ctx_chart_japon_9, {"type": "bar", "data": {"labels": ["Crecimiento interanual", "Participaci\u00f3n del commerce"], "datasets": [{"label": "Porcentaje (%)", "data": [12, 22], "backgroundColor": ["#f97316", "#2563eb"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Canales Digitales (Jap\u00f3n 2023-2024)"}}}});
        }
        
        const ctx_chart_japon_10 = document.getElementById('chart_japon_10');
        if (ctx_chart_japon_10) {
            new Chart(ctx_chart_japon_10, {"type": "bar", "data": {"labels": ["Demanda certificada MPS/Fairtrade", "Preferencia sin pl\u00e1sticos"], "datasets": [{"label": "2023", "data": [45, 30], "backgroundColor": "#1e40af"}, {"label": "2024", "data": [65, 55], "backgroundColor": "#f97316"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Sostenibilidad y Certificaciones"}}}});
        }
        
        const ctx_chart_japon_11 = document.getElementById('chart_japon_11');
        if (ctx_chart_japon_11) {
            new Chart(ctx_chart_japon_11, {"type": "bar", "data": {"labels": ["Penetraci\u00f3n Internet", "Adopci\u00f3n Redes Sociales (18+)", "Adopci\u00f3n Redes Sociales Total"], "datasets": [{"label": "Porcentaje (%)", "data": [88.2, 87.0, 78.6], "backgroundColor": ["#1e3a8a", "#3b82f6", "#60a5fa"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Infraestructura Digital y Conectividad (2024-2025)"}}}});
        }
        
        const ctx_chart_japon_12 = document.getElementById('chart_japon_12');
        if (ctx_chart_japon_12) {
            new Chart(ctx_chart_japon_12, {"type": "bar", "data": {"labels": ["Tradici\u00f3n Espiritual", "Rituales", "Calidad", "Nuevas Tendencias"], "datasets": [{"label": "Importancia", "data": [100, 100, 100, 60], "backgroundColor": ["#db2777", "#9d174d", "#15803d", "#0d9488"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Estructura del Consumo Floral"}}}});
        }
        
        const ctx_chart_japon_13 = document.getElementById('chart_japon_13');
        if (ctx_chart_japon_13) {
            new Chart(ctx_chart_japon_13, {"type": "bar", "data": {"labels": ["Efectividad de Control IoT (%)", "Mermas de Producto (%)"], "datasets": [{"label": "Indicador", "data": [100, 4.9], "backgroundColor": ["#0f766e", "#ef4444"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Acceso a Tecnolog\u00eda e Innovaci\u00f3n (2024-2025)"}}}});
        }
        
        const ctx_chart_japon_14 = document.getElementById('chart_japon_14');
        if (ctx_chart_japon_14) {
            new Chart(ctx_chart_japon_14, {"type": "bar", "data": {"labels": ["\u00cdndice de Urbanizaci\u00f3n", "Carga Flor Narita y Kansai"], "datasets": [{"label": "Porcentaje (%)", "data": [92.9, 90.0], "backgroundColor": ["#1e3a8a", "#2563eb"]}]}, "options": {"indexAxis": "y", "responsive": "true", "plugins": {"title": {"display": "true", "text": "Indicadores Geogr\u00e1ficos y Conectividad"}}}});
        }
        
        const ctx_chart_eau_1 = document.getElementById('chart_eau_1');
        if (ctx_chart_eau_1) {
            new Chart(ctx_chart_eau_1, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Poblaci\u00f3n total", "data": [9445785, 9401038, 9575152, 10074977, 10483751, 10986400], "borderColor": "#3d6751", "backgroundColor": "#3d675120", "fill": "true"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Poblaci\u00f3n total - Emiratos \u00c1rabes Unidos (2019-2024)"}}}});
        }
        
        const ctx_chart_eau_2 = document.getElementById('chart_eau_2');
        if (ctx_chart_eau_2) {
            new Chart(ctx_chart_eau_2, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "PIB per c\u00e1pita (US$ corrientes)", "data": [45938.6, 37991.7, 44118.5, 50759.8, 49850.7, 50273.5], "borderColor": "#4CAF50", "backgroundColor": "#4CAF5020", "fill": "true"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "PIB per c\u00e1pita de Emiratos \u00c1rabes Unidos (2019-2024)"}}}});
        }
        
        const ctx_chart_eau_3 = document.getElementById('chart_eau_3');
        if (ctx_chart_eau_3) {
            new Chart(ctx_chart_eau_3, {"type": "bar", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Importaciones (US$)", "data": [50354898.73, 45899210.25, 64203566.14, 69741088.09, 78773261.98], "backgroundColor": ["#5c8397", "#b85c5c", "#8eb85c", "#945cb8", "#5cb8b4"]}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Importaciones de flores cortadas EAU (2019-2023)"}}}});
        }
        
        const ctx_chart_eau_4 = document.getElementById('chart_eau_4');
        if (ctx_chart_eau_4) {
            new Chart(ctx_chart_eau_4, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "\u00cdndice WGI", "data": [0.65, 0.6, 0.61, 0.73, 0.67], "borderColor": "#3b82f6", "backgroundColor": "#3b82f620"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Estabilidad pol\u00edtica (2019-2023)"}}}});
        }
        
        const ctx_chart_eau_5 = document.getElementById('chart_eau_5');
        if (ctx_chart_eau_5) {
            new Chart(ctx_chart_eau_5, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "\u00cdndice de Libertad Econ\u00f3mica", "data": [77.6, 76.2, 76.9, 70.2, 70.8], "borderColor": "#8b5cf6", "backgroundColor": "#8b5cf620"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "\u00cdndice de Libertad Econ\u00f3mica - Emiratos \u00c1rabes Unidos"}}}});
        }
        
        const ctx_chart_eau_6 = document.getElementById('chart_eau_6');
        if (ctx_chart_eau_6) {
            new Chart(ctx_chart_eau_6, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "\u00cdndice de efectividad del gobierno", "data": [1.4, 1.3, 1.38, 1.32, 1.6], "borderColor": "#10b981", "backgroundColor": "#10b98120", "tension": 0.4}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Efectividad del Gobierno (2019-2023)"}}}});
        }
        
        const ctx_chart_eau_7 = document.getElementById('chart_eau_7');
        if (ctx_chart_eau_7) {
            new Chart(ctx_chart_eau_7, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Usuarios de Internet (%)", "data": [99.0, 100, 100, 100, 100], "borderColor": "#0ea5e9", "backgroundColor": "#0ea5e920"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Usuarios de Internet en EAU (2019-2023)"}}}});
        }
        
        const ctx_chart_eau_8 = document.getElementById('chart_eau_8');
        if (ctx_chart_eau_8) {
            new Chart(ctx_chart_eau_8, {"type": "line", "data": {"labels": ["2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Posici\u00f3n mundial", "data": [34, 33, 31, 32, 32], "borderColor": "#f59e0b", "backgroundColor": "#f59e0b20"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Ranking del \u00cdndice Global de Innovaci\u00f3n (EAU)"}}, "scales": {"y": {"reverse": "true"}}}});
        }
        
        const ctx_chart_eau_9 = document.getElementById('chart_eau_9');
        if (ctx_chart_eau_9) {
            new Chart(ctx_chart_eau_9, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Emisiones (t CO2e)", "data": [26.66732, 26.56611, 26.66825, 25.36906, 24.25728, 24.04322], "borderColor": "#ef4444", "backgroundColor": "#ef444420"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Emisiones de CO2 per c\u00e1pita - EAU"}}}});
        }
        
        const ctx_chart_eau_10 = document.getElementById('chart_eau_10');
        if (ctx_chart_eau_10) {
            new Chart(ctx_chart_eau_10, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Comercio (% del PIB)", "data": [163.8221, 181.2919, 182.9094, 185.7417, 199.045], "borderColor": "#14b8a6", "backgroundColor": "#14b8a620", "fill": "true"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Comercio (% del PIB) - Emiratos \u00c1rabes Unidos"}}}});
        }
        
        const ctx_chart_eau_11 = document.getElementById('chart_eau_11');
        if (ctx_chart_eau_11) {
            new Chart(ctx_chart_eau_11, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Importaciones de bienes y servicios (% del PIB)", "data": [70.52, 83.22, 82.27, 83.69, 92.2], "borderColor": "#6366f1", "backgroundColor": "#6366f120"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Importaciones de bienes y servicios (% del PIB)"}}}});
        }
        
        const ctx_chart_eau_12 = document.getElementById('chart_eau_12');
        if (ctx_chart_eau_12) {
            new Chart(ctx_chart_eau_12, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "Exportaciones de bienes y servicios (% del PIB)", "data": [93.30231, 98.0725, 100.6426, 102.052, 106.8461], "borderColor": "#ec4899", "backgroundColor": "#ec489920", "fill": "true"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Exportaciones de bienes y servicios (% del PIB) - EAU"}}}});
        }
        
        const ctx_chart_eau_13 = document.getElementById('chart_eau_13');
        if (ctx_chart_eau_13) {
            new Chart(ctx_chart_eau_13, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023"], "datasets": [{"label": "IED neta (% del PIB)", "data": [4.119286, 5.567357, 4.892306, 4.445914, 5.87184], "borderColor": "#84cc16", "backgroundColor": "#84cc1620"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Inversi\u00f3n Extranjera Directa neta (% del PIB)"}}}});
        }
        
        const ctx_chart_eau_14 = document.getElementById('chart_eau_14');
        if (ctx_chart_eau_14) {
            new Chart(ctx_chart_eau_14, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Capitalizaci\u00f3n burs\u00e1til (% del PIB)", "data": [56.88036, 82.54857, 131.3938, 170.8167, 190.2272, 190.8591], "borderColor": "#d946ef", "backgroundColor": "#d946ef20", "fill": "true"}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Capitalizaci\u00f3n burs\u00e1til de empresas nacionales cotizadas"}}}});
        }
        
        const ctx_chart_eau_15 = document.getElementById('chart_eau_15');
        if (ctx_chart_eau_15) {
            new Chart(ctx_chart_eau_15, {"type": "line", "data": {"labels": ["2019", "2020", "2021", "2022", "2023", "2024"], "datasets": [{"label": "Acciones negociadas (% del PIB)", "data": [6.741077, 10.50203, 28.32565, 28.64126, 21.31852, 21.82124], "borderColor": "#06b6d4", "backgroundColor": "#06b6d420", "tension": 0.4}]}, "options": {"responsive": "true", "plugins": {"title": {"display": "true", "text": "Valor total de las acciones negociadas (% del PIB)"}}}});
        }
        
    