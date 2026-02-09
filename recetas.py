# recetas.py
# Base de datos ACTUALIZADA para NutriPlan Pro
# Cantidades calculadas para ATLETAS (Alto Rendimiento)
# Objetivo Base: ~2200-2400 kcal (Factor 1.0)

RECETARIO = {
    "Desayunos": [
        {
            "nombre": "Arepa Reina Pepiada (Power)",
            "descripcion": "Relleno contundente de pollo y palta con yogurt.",
            "macros": {"cal": 680, "prot": 45, "carb": 60, "fat": 25},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga de Pollo (Desmechada)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Palta", "cantidad": 60, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego Vakimu", "cantidad": 40, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cilantro/Cebolla", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Masa con sal y agua. Asar arepa grande.\n2. Mezclar pollo, palta triturada y yogurt.\n3. Rellenar a tope."
        },
        {
            "nombre": "Arepa con Perico y Queso",
            "descripcion": "El desayuno clásico venezolano completo.",
            "macros": {"cal": 650, "prot": 35, "carb": 60, "fat": 28},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevos", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate y Cebolla", "cantidad": 120, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Llanero/Fresco", "cantidad": 50, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Aceite (para sofreír)", "cantidad": 5, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír vegetales y hacer huevos revueltos jugosos.\n2. Servir arepa con queso y perico."
        },
        {
            "nombre": "Panquecas Bluhealth (Torre)",
            "descripcion": "Alta en proteína y fibra para recuperar músculo.",
            "macros": {"cal": 590, "prot": 42, "carb": 75, "fat": 12},
            "ingredientes": [
                {"item": "Avena en Hojuelas", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Scoop Proteína Bluhealth", "cantidad": 1, "unidad": "und", "pasillo": "💊 Suplementos"},
                {"item": "Claras de Huevo", "cantidad": 4, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Huevo Entero", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Plátano (Masa)", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Miel (Topping)", "cantidad": 10, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Licuar todo (avena, huevos, prote, plátano).\n2. Hacer panquecas en sartén.\n3. Comer con miel."
        },
        {
            "nombre": "Sandwich Triple Vital",
            "descripcion": "Tres pisos de pan multicereal con mucho relleno.",
            "macros": {"cal": 620, "prot": 38, "carb": 65, "fat": 20},
            "ingredientes": [
                {"item": "Pan Multicereal Vital", "cantidad": 3, "unidad": "rebanadas", "pasillo": "🍞 Panadería"},
                {"item": "Pechuga de Pollo", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Palta", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Huevo Sancochado", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate/Lechuga", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Tostar pan.\n2. Armar pisos: Pollo/Palta y Huevo/Tomate."
        },
        {
            "nombre": "Cachapas de Avena Fit",
            "descripcion": "Sabor a maíz dulce, usando avena para espesar.",
            "macros": {"cal": 580, "prot": 30, "carb": 80, "fat": 18},
            "ingredientes": [
                {"item": "Maíz Dulce (Grano)", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Avena", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevos", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Llanero", "cantidad": 60, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Leche Light", "cantidad": 20, "unidad": "ml", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Licuar maíz, avena, leche y huevo.\n2. Cocinar a fuego medio-bajo.\n3. Rellenar con queso."
        },
        {
            "nombre": "Pan Árabe con Perico",
            "descripcion": "Opción rápida cuando no hay tiempo de hacer arepas.",
            "macros": {"cal": 550, "prot": 32, "carb": 60, "fat": 22},
            "ingredientes": [
                {"item": "Pan Árabe", "cantidad": 2, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Huevos", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate y Cebolla", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Hacer huevos perico.\n2. Rellenar los panes árabes y agregar yogurt."
        },
        {
            "nombre": "Bowl de Yogurt Power (Doble)",
            "descripcion": "Sin cocinar. Mucha proteína y fruta.",
            "macros": {"cal": 500, "prot": 35, "carb": 60, "fat": 15},
            "ingredientes": [
                {"item": "Yogurt Griego Vakimu", "cantidad": 250, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Scoop Proteína Bluhealth", "cantidad": 0.5, "unidad": "und", "pasillo": "💊 Suplementos"},
                {"item": "Avena (Cruda/Tostada)", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Fruta (Fresa/Plátano)", "cantidad": 120, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Nueces/Pecanas", "cantidad": 15, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Mezclar yogurt con medio scoop de proteína.\n2. Agregar toppings."
        }
    ],

    "Almuerzos": [
        {
            "nombre": "Pollo Saltado (Full Papa)",
            "descripcion": "Plato bandera. Cantidades generosas.",
            "macros": {"cal": 820, "prot": 55, "carb": 90, "fat": 20},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Cebolla y Tomate (Gruesos)", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Sancochada/Dorada", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao/Vinagre", "cantidad": 30, "unidad": "ml", "pasillo": "🥫 Abarrotes"},
                {"item": "Arroz Blanco/Integral", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sellar pollo a fuego muy alto.\n2. Saltear verduras (poco tiempo).\n3. Mezclar con papas y jugo."
        },
        {
            "nombre": "Pabellón Fit (Carga de Carbos)",
            "descripcion": "Ideal para recuperar post-bici.",
            "macros": {"cal": 880, "prot": 52, "carb": 110, "fat": 22},
            "ingredientes": [
                {"item": "Carne Molida Magra", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Arroz", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Caraotas Negras", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Plátano Maduro (Horno)", "cantidad": 120, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pimiento/Cebolla", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Carne molida guisada.\n2. Caraotas aliñadas.\n3. Plátano al horno/airfryer."
        },
        {
            "nombre": "Lentejas con Chuleta y Arroz",
            "descripcion": "Hierro y Energía.",
            "macros": {"cal": 800, "prot": 55, "carb": 95, "fat": 20},
            "ingredientes": [
                {"item": "Lentejas Guisadas", "cantidad": 250, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Chuleta Ahumada Magra", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Arroz", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Ensalada Criolla", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Lentejas estofadas.\n2. Chuleta a la plancha (quitar grasa borde).\n3. Arroz graneado."
        },
        {
            "nombre": "Seco de Pollo con Quinua",
            "descripcion": "Guiso verde peruano.",
            "macros": {"cal": 750, "prot": 50, "carb": 75, "fat": 25},
            "ingredientes": [
                {"item": "Presa de Pollo (Sin Piel)", "cantidad": 220, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Culantro Licuado", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Quinua Cocida", "cantidad": 200, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo Loche/Zanahoria", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arvejas", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Macerar pollo.\n2. Cocinar a fuego lento con base de culantro.\n3. Servir sobre quinua."
        },
        {
            "nombre": "Chaufa de Quinua y Pollo",
            "descripcion": "Fusión Chifa ligera pero potente.",
            "macros": {"cal": 700, "prot": 50, "carb": 70, "fat": 20},
            "ingredientes": [
                {"item": "Quinua Cocida", "cantidad": 250, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga de Pollo (Cubos)", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevos (Tortilla)", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Cebolla China/Pimiento", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao/Kion", "cantidad": 20, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Saltear pollo y verduras.\n2. Agregar quinua y huevos.\n3. Terminar con sillao."
        },
        {
            "nombre": "Estofado de Pollo Clásico",
            "descripcion": "Pollo jugoso con salsa roja.",
            "macros": {"cal": 720, "prot": 48, "carb": 80, "fat": 20},
            "ingredientes": [
                {"item": "Presa de Pollo", "cantidad": 220, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa Sancochada", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zanahoria/Arvejas", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pasta de Tomate/Hongos", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sellar pollo.\n2. Guisar con tomate, hongos y laurel.\n3. Agregar verduras."
        },
        {
            "nombre": "Carne Molida a la Jardinera",
            "descripcion": "Rendidora para batch cooking.",
            "macros": {"cal": 780, "prot": 45, "carb": 85, "fat": 25},
            "ingredientes": [
                {"item": "Carne Molida Magra", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa (Cubitos)", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Zanahoria/Vainita/Choclo", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír carne.\n2. Agregar verduras y papa picada.\n3. Cocinar tapado."
        },
        {
            "nombre": "Ají de Pollo (Extra Proteína)",
            "descripcion": "Doble ración de pollo deshilachado.",
            "macros": {"cal": 750, "prot": 55, "carb": 70, "fat": 22},
            "ingredientes": [
                {"item": "Pechuga de Pollo (Desmechada)", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Crema Ají Amarillo", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Sancochada", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Leche Light", "cantidad": 60, "unidad": "ml", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Base de ají amarillo, licuar pan integral/quinua con leche.\n2. Mezclar con pollo."
        },
        {
            "nombre": "Tallarines Rojos con Pollo",
            "descripcion": "Pasta con salsa de tomate y pollo.",
            "macros": {"cal": 800, "prot": 50, "carb": 100, "fat": 18},
            "ingredientes": [
                {"item": "Fideos/Spaghetti", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Presa de Pollo", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Salsa de Tomate (Zanahoria/Hongo)", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Parmesano (Opcional)", "cantidad": 10, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Licuar zanahoria cocida con tomate para la salsa.\n2. Guisar pollo en la salsa.\n3. Mezclar con pasta."
        },
        {
            "nombre": "Aguadito de Pollo Espeso",
            "descripcion": "Con mucho arroz y papa amarilla.",
            "macros": {"cal": 700, "prot": 45, "carb": 80, "fat": 18},
            "ingredientes": [
                {"item": "Presa de Pollo", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Arroz", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Papa Amarilla", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Culantro/Verduras", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir todo junto hasta que espese."
        }
    ],

    "Cenas": [
        {
            "nombre": "Crema de Zapallo con Pollo (XL)",
            "descripcion": "Porción grande de pollo para no perder masa.",
            "macros": {"cal": 500, "prot": 45, "carb": 40, "fat": 12},
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 350, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa Amarilla", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 50, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Fresco", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Crema espesa con leche.\n2. Servir con pollo deshilachado y cubos de queso."
        },
        {
            "nombre": "Ensalada de Atún (2 Latas)",
            "descripcion": "Cena alta en proteína, sin cocinar.",
            "macros": {"cal": 550, "prot": 55, "carb": 25, "fat": 22},
            "ingredientes": [
                {"item": "Atún en Agua", "cantidad": 240, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Palta", "cantidad": 60, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Choclo Desgranado", "cantidad": 60, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Mix Lechugas/Tomate", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego", "cantidad": 40, "unidad": "g", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Usar aprox 1.5 a 2 latas de atún por persona.\n2. Mezclar todo."
        },
        {
            "nombre": "Tortilla de Espinaca Power",
            "descripcion": "Muchos huevos y queso.",
            "macros": {"cal": 480, "prot": 38, "carb": 10, "fat": 30},
            "ingredientes": [
                {"item": "Huevos Enteros", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Claras de Huevo", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Espinaca", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Fresco", "cantidad": 50, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Saltear espinaca.\n2. Batir huevos, mezclar y cuajar."
        },
        {
            "nombre": "Sopa de Menudencias (Con Fideos)",
            "descripcion": "Recuperación y colágeno.",
            "macros": {"cal": 500, "prot": 40, "carb": 45, "fat": 15},
            "ingredientes": [
                {"item": "Menudencia (Hígado/Molleja)", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Fideos Cabello Ángel", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo/Verduras", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Amarilla", "cantidad": 60, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir menudencias.\n2. Agregar verduras y fideo."
        },
        {
            "nombre": "Hamburguesa al Plato",
            "descripcion": "Carne casera con huevo montado.",
            "macros": {"cal": 580, "prot": 48, "carb": 15, "fat": 32},
            "ingredientes": [
                {"item": "Carne Molida Magra", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo (Frito/Plancha)", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Ensalada Fresca", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Palta", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Aliñar carne y hacer hamburguesa gruesa.\n2. Servir con huevo encima."
        },
        {
            "nombre": "Pizza Pan Árabe (Doble)",
            "descripcion": "Dos pizzas personales.",
            "macros": {"cal": 550, "prot": 35, "carb": 60, "fat": 18},
            "ingredientes": [
                {"item": "Pan Árabe", "cantidad": 2, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Queso Mozzarella/Fresco", "cantidad": 60, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Jamón de Pavo", "cantidad": 50, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Pasta de Tomate", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Armar pizzas.\n2. Calentar en sartén tapada."
        },
        {
            "nombre": "Chaufa de Quinua (Cena)",
            "descripcion": "Versión ligera del almuerzo.",
            "macros": {"cal": 520, "prot": 40, "carb": 50, "fat": 16},
            "ingredientes": [
                {"item": "Quinua Cocida", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Verduras Chinas", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Saltear todo rápido."
        },
        {
            "nombre": "Wrap de Lechuga (Tacos)",
            "descripcion": "Relleno abundante de carne.",
            "macros": {"cal": 480, "prot": 40, "carb": 20, "fat": 25},
            "ingredientes": [
                {"item": "Carne Molida Magra", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Lechuga Americana", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Palta", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pico de Gallo", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Usar hojas de lechuga como tortillas.\n2. Rellenar."
        },
        {
            "nombre": "Calabacines Rellenos",
            "descripcion": "Horneados con pollo y queso.",
            "macros": {"cal": 450, "prot": 38, "carb": 25, "fat": 20},
            "ingredientes": [
                {"item": "Calabacín Italiano", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pechuga de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Queso Fresco/Mozzarella", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Choclo", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Ahuecar zapallitos.\n2. Rellenar con pollo salteado y gratinar."
        },
        {
            "nombre": "Berenjenas Rellenas",
            "descripcion": "Con carne molida.",
            "macros": {"cal": 460, "prot": 40, "carb": 20, "fat": 22},
            "ingredientes": [
                {"item": "Berenjena", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida Magra", "cantidad": 160, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Pasta de Tomate", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Queso Mozzarella", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Rellenar berenjenas con carne guisada.\n2. Gratinar."
        }
    ]
}
