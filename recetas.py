# recetas.py
# Base de datos de recetas para NutriPlan 2.0
# Cantidades Base calculadas para un adulto promedio (~2000 kcal).
# La app ajustará esto automáticamente según el peso de Edimar y Carlos.

RECETARIO = {
    "Desayunos": [
        {
            "nombre": "Arepa Reina Pepiada (Fit)",
            "descripcion": "La clásica venezolana, pero usando yogurt griego en lugar de mayonesa para sumar proteína.",
            "imagen": "reina_pepiada",
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga Desmechada", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Palta (Aguacate)", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego Vakimu", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cilantro/Cebolla", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar harina con agua y sal, asar la arepa.\n2. Mezclar el pollo desmechado con el yogurt, la palta triturada, cilantro y cebollita picada.\n3. Rellenar."
        },
        {
            "nombre": "Perico Venezolano con Arepa",
            "descripcion": "Huevos revueltos con tomate y cebolla, alto en saciedad.",
            "imagen": "perico",
            "ingredientes": [
                {"item": "Huevos Enteros", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Claras de Huevo", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate y Cebolla", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Harina P.A.N", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Aceite de Oliva", "cantidad": 5, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír tomate y cebolla en el aceite.\n2. Agregar los huevos y claras batidos.\n3. Servir con arepa asada delgada."
        },
        {
            "nombre": "Panquecas de Avena y Proteína",
            "descripcion": "Ideales para días de entrenamiento pesado.",
            "imagen": "panquecas",
            "ingredientes": [
                {"item": "Avena en hojuelas", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Scoop Proteína (Bluhealth)", "cantidad": 1, "unidad": "und", "pasillo": "💊 Suplementos"},
                {"item": "Claras de Huevo", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Polvo de hornear", "cantidad": 2, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Fresas", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Licuar avena, proteína, claras y polvo de hornear.\n2. Hacer en sartén antiadherente.\n3. Servir con fresas."
        },
        {
            "nombre": "Tostadas Multicereal con Palta y Huevo",
            "descripcion": "Desayuno rápido y equilibrado.",
            "imagen": "tostadas",
            "ingredientes": [
                {"item": "Pan Multicereal Vital", "cantidad": 2, "unidad": "rebanadas", "pasillo": "🍞 Panadería"},
                {"item": "Huevos", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Palta", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Semillas de Chía", "cantidad": 5, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Tostar el pan.\n2. Hacer huevos revueltos o sancochados.\n3. Machacar la palta sobre el pan y poner el huevo encima."
        },
        {
            "nombre": "Sándwich de Atún Express",
            "descripcion": "Cuando no hay tiempo de cocinar.",
            "imagen": "sandwich_atun",
            "ingredientes": [
                {"item": "Pan Árabe / Integral", "cantidad": 2, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Atún en Agua", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Yogurt Griego (como mayo)", "cantidad": 20, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cebolla picada", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar atún escurrido con yogurt y cebolla.\n2. Rellenar el pan."
        },
        {
            "nombre": "Cachapas de Avena (Falsas Cachapas)",
            "descripcion": "Sabor a maíz pero con fibra de la avena.",
            "imagen": "cachapa_fit",
            "ingredientes": [
                {"item": "Maíz dulce (lata/grano)", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Avena", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevo", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Llanero/Fresco", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Licuar maíz, avena y huevo.\n2. Cocinar como panqueca.\n3. Rellenar con el queso."
        },
        {
            "nombre": "Bowl de Yogurt Power",
            "descripcion": "Fresco y sin cocinar.",
            "imagen": "bowl_yogurt",
            "ingredientes": [
                {"item": "Yogurt Griego Vakimu", "cantidad": 200, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Nueces/Almendras", "cantidad": 15, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Frutos rojos", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Miel", "cantidad": 10, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Servir yogurt.\n2. Agregar toppings."
        }
    ],
    "Almuerzos": [
        {
            "nombre": "Pollo Saltado (Estilo Fit)",
            "descripcion": "Menos papa, más vegetales crujientes. Usamos el wok.",
            "imagen": "pollo_saltado",
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Cebolla Roja (Gajos)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Tomate (Gajos)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao y Vinagre", "cantidad": 20, "unidad": "ml", "pasillo": "🥫 Abarrotes"},
                {"item": "Papa Sancochada (Dorada)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Cortar pollo en tiras y sellar a fuego muy alto.\n2. Retirar pollo, saltear cebolla y tomate (30 seg).\n3. Mezclar todo, agregar sillao/vinagre.\n4. Servir con la papa cocida aparte."
        },
        {
            "nombre": "Pabellón Criollo Saludable",
            "descripcion": "Carne magra, arroz integral/quinua y plátano al horno (no frito).",
            "imagen": "pabellon",
            "ingredientes": [
                {"item": "Carne Desmechada Magra", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Frijoles Negros (Caraotas)", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Arroz Integral / Quinua", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Plátano Maduro (Horno)", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pimiento/Cebolla (Sofrito)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Carne: Cocinar con poco aceite.\n2. Plátano: Hornear o usar Airfryer en vez de freír.\n3. Caraotas: Sin azúcar añadida."
        },
        {
            "nombre": "Chaufa de Quinua y Pollo",
            "descripcion": "Reemplazamos arroz por quinua para más fibra.",
            "imagen": "chaufa_quinua",
            "ingredientes": [
                {"item": "Quinua Cocida (Graneada)", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga de Pollo (Cubos)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevos (Tortilla picada)", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Cebolla China (Verdeo)", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pimiento Rojo", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao/Kion", "cantidad": 10, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Tener la quinua lista y fría.\n2. Saltear pollo y verduras.\n3. Agregar quinua y tortilla picada, mezclar con sillao."
        },
        {
            "nombre": "Lentejas con Chuleta Ahumada",
            "descripcion": "Plato alto en hierro. Retirar grasa visible de la chuleta.",
            "imagen": "lentejas",
            "ingredientes": [
                {"item": "Lentejas Guisadas", "cantidad": 200, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Chuleta Ahumada (Magra)", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Zanahoria y Papa (cubitos)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz Blanco", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Ensalada Fresca (Lado)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Guisar lentejas con verduras.\n2. Dorar chuleta en su propia grasa (retirar excesos).\n3. Acompañar con porción pequeña de arroz."
        },
        {
            "nombre": "Estofado de Pollo Casero",
            "descripcion": "Reconfortante y fácil de hacer en cantidad.",
            "imagen": "estofado",
            "ingredientes": [
                {"item": "Presa de Pollo (Sin piel)", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa Sancochada", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Zanahoria / Arvejas", "cantidad": 60, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Salsa de Tomate Natural", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Hongos y Laurel", "cantidad": 5, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sellar pollo.\n2. Hacer aderezo rojo.\n3. Cocinar todo junto con las verduras hasta que la papa esté lista."
        },
        {
            "nombre": "Carne Molida con Vegetales (A la Jardinera)",
            "descripcion": "Muy rendidora para batch cooking.",
            "imagen": "molida_vegetales",
            "ingredientes": [
                {"item": "Carne Molida Especial", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Zanahoria/Vainitas/Choclo", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa en cuadritos", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír carne molida.\n2. Agregar verduras picadas chiquitas.\n3. Cocinar tapado para que suelte jugo."
        },
        {
            "nombre": "Seco de Pollo con Quinua",
            "descripcion": "Salsa verde de cilantro, reemplazando arroz con quinua.",
            "imagen": "seco_pollo",
            "ingredientes": [
                {"item": "Pollo (Presa)", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Culantro Licuado", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arvejas y Zanahoria", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Quinua Cocida", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo Loche (Rallado)", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Macerar pollo en culantro.\n2. Cocinar a fuego lento con zapallo loche para espesar sin harina."
        },
        {
            "nombre": "Ají de Pollo Saludable",
            "descripcion": "Usamos leche light y quinua o pan integral para espesar.",
            "imagen": "aji_pollo",
            "ingredientes": [
                {"item": "Pechuga Deshilachada", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Crema de Ají Amarillo", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Gloria Light", "cantidad": 50, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Pan Integral (para espesar)", "cantidad": 20, "unidad": "g", "pasillo": "🍞 Panadería"},
                {"item": "Pecan, Huevo, Aceituna", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Hacer aderezo de ají.\n2. Licuar pan remojado en leche light.\n3. Mezclar con pollo."
        },
        {
            "nombre": "Caigua Rellena de Carne",
            "descripcion": "Bajo en carbohidratos, alto en volumen.",
            "imagen": "caigua",
            "ingredientes": [
                {"item": "Caigua", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo Duro / Pasas", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Arroz (Guarnición)", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Limpiar caiguas.\n2. Rellenar con carne guisada con huevo y pasas.\n3. Cocinar al vapor o en salsa."
        },
        {
            "nombre": "Adobo de Cerdo (Lomo)",
            "descripcion": "Usar parte magra del chancho. Mucho sabor.",
            "imagen": "adobo",
            "ingredientes": [
                {"item": "Lomo de Cerdo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Ají Panca / Vinagre", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Camote Sancochado", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Cebolla Roja (Gruesa)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Marinar cerdo desde la noche anterior.\n2. Cocinar a fuego fuerte.\n3. Servir con camote."
        }
    ],
    "Cenas": [
        {
            "nombre": "Crema de Zapallo con Pollo",
            "descripcion": "La cena estrella. Ligera y nutritiva.",
            "imagen": "crema_zapallo",
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pechuga Pollo (Trozo o Desme.)", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa Amarilla (Espesante)", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 30, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Fresco (Cubo)", "cantidad": 20, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Hervir zapallo y papa. Licuar con leche.\n2. Agregar el pollo cocido y trozos de queso al final."
        },
        {
            "nombre": "Tortilla de Espinacas y Vegetales",
            "descripcion": "Cena Low-Carb para cerrar el día.",
            "imagen": "tortilla_espinaca",
            "ingredientes": [
                {"item": "Huevos (2 claras 1 yema)", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Espinaca Picada", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Champiñones/Pimiento", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Fresco Rallado", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Saltear vegetales.\n2. Batir huevos y verter sobre vegetales.\n3. Cocinar tapado a fuego lento."
        },
        {
            "nombre": "Pan Árabe Pizza Fit",
            "descripcion": "Mata el antojo de pizza de forma saludable.",
            "imagen": "pizza_arabe",
            "ingredientes": [
                {"item": "Pan Árabe Delgado", "cantidad": 1, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Pasta de Tomate", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Queso Mozzarella/Fresco", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Jamón de Pavo", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Orégano", "cantidad": 2, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Armar la pizza sobre el pan.\n2. Llevar al horno o sartén tapada hasta derretir queso."
        },
        {
            "nombre": "Ensalada de Atún Vakimu",
            "descripcion": "Fresca, alta en proteína.",
            "imagen": "ensalada_atun",
            "ingredientes": [
                {"item": "Atún en Agua", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Yogurt Griego (Aderezo)", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Lechuga/Tomate/Pepino", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Choclo Desgranado", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Palta", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar todo en un bowl grande."
        },
        {
            "nombre": "Pollo a la Plancha con Ensalada Rusa",
            "descripcion": "Versión ligera de la rusa con yogurt.",
            "imagen": "pollo_rusa",
            "ingredientes": [
                {"item": "Filete de Pechuga", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Beterraga y Zanahoria (Cubos)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Vainitas", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego (Sustituye Mayo)", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Papa (Poca cantidad)", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Cocinar verduras y mezclar con yogurt, sal y limón.\n2. Planchar el pollo con orégano."
        },
        {
            "nombre": "Sopa de Menudencia (Sustanciosa)",
            "descripcion": "Aprovechando lo que viene con el pollo entero.",
            "imagen": "sopa_menudencia",
            "ingredientes": [
                {"item": "Menudencia (Hígado/Molleja)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Cabello de Ángel (Fideos)", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo/Zanahoria/Apio", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Kion (Jengibre)", "cantidad": 5, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Amarilla", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir menudencias con kion.\n2. Agregar verduras y al final el fideo."
        },
        {
            "nombre": "Wrap de Lechuga con Carne",
            "descripcion": "Tacos sin masa, usando lechuga.",
            "imagen": "wrap_lechuga",
            "ingredientes": [
                {"item": "Carne Molida Guisada", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Lechuga Americana (Hojas)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pico de Gallo (Tomate/Cebolla)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Palta", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Rallado", "cantidad": 20, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Usar la hoja de lechuga como tortilla.\n2. Rellenar con carne y toppings."
        }
    ]
}
