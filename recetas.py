# recetas.py
# Base de datos con MACROS para NutriPlan 2.0
# Macros calculados para la porción base estándar.

RECETARIO = {
    "Desayunos": [
        {
            "nombre": "Arepa Reina Pepiada (Fit)",
            "descripcion": "Relleno cremoso usando yogurt griego en lugar de mayonesa.",
            "macros": {"cal": 450, "prot": 28, "carb": 45, "fat": 18},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga Desmechada", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Palta (Aguacate)", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego Vakimu", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cilantro/Cebolla", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Asar arepa.\n2. Mezclar pollo, palta triturada, yogurt y cilantro.\n3. Rellenar."
        },
        {
            "nombre": "Arepa con Perico",
            "descripcion": "Huevos revueltos con vegetales, alto volumen y saciedad.",
            "macros": {"cal": 420, "prot": 22, "carb": 42, "fat": 18},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevos Enteros", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate y Cebolla", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Aceite de Oliva", "cantidad": 5, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír tomate y cebolla.\n2. Agregar huevos batidos con sal.\n3. Servir con arepa."
        },
        {
            "nombre": "Cachapas de Avena (Sin Harina)",
            "descripcion": "Sabor a maíz dulce pero con fibra.",
            "macros": {"cal": 380, "prot": 18, "carb": 55, "fat": 12},
            "ingredientes": [
                {"item": "Maíz Dulce (Lata/Grano)", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Avena en Hojuelas", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevo", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Llanero/Fresco", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Licuar maíz, avena y huevo.\n2. Cocinar en sartén como panqueca.\n3. Rellenar con queso."
        },
        {
            "nombre": "Panquecas Proteicas Bluhealth",
            "descripcion": "Para días de entrenamiento de pierna.",
            "macros": {"cal": 350, "prot": 35, "carb": 40, "fat": 6},
            "ingredientes": [
                {"item": "Avena", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Scoop Proteína", "cantidad": 1, "unidad": "und", "pasillo": "💊 Suplementos"},
                {"item": "Claras de Huevo", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Polvo Hornear", "cantidad": 2, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Fresas", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Licuar todo (menos fresas).\n2. Hacer panquecas.\n3. Servir con fruta."
        },
        {
            "nombre": "Bowl de Yogurt Power",
            "descripcion": "Sin cocinar, solo mezclar.",
            "macros": {"cal": 320, "prot": 25, "carb": 35, "fat": 10},
            "ingredientes": [
                {"item": "Yogurt Griego Vakimu", "cantidad": 200, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Nueces/Almendras", "cantidad": 15, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Arándanos", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Miel", "cantidad": 10, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Servir yogurt en bowl.\n2. Decorar con toppings."
        },
        {
            "nombre": "Tostadas Vital con Palta y Huevo",
            "descripcion": "Clásico desayuno nutritivo.",
            "macros": {"cal": 410, "prot": 20, "carb": 35, "fat": 22},
            "ingredientes": [
                {"item": "Pan Multicereal Vital", "cantidad": 2, "unidad": "rebanadas", "pasillo": "🍞 Panadería"},
                {"item": "Huevos", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Palta", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Semillas de Chía", "cantidad": 5, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Tostar pan.\n2. Poner palta machacada y huevo (sancochado o revuelto) encima."
        },
        {
            "nombre": "Sándwich de Atún Express",
            "descripcion": "Rápido y alto en proteína.",
            "macros": {"cal": 380, "prot": 32, "carb": 45, "fat": 8},
            "ingredientes": [
                {"item": "Pan Árabe / Integral", "cantidad": 2, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Atún en Agua", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Yogurt Griego (Sustituye Mayo)", "cantidad": 20, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cebolla picada", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar atún escurrido con yogurt y cebolla.\n2. Armar sándwich."
        }
    ],

    "Almuerzos": [
        {
            "nombre": "Arroz con Pollo (Integral/Quinua)",
            "descripcion": "Con mucho culantro y verduras.",
            "macros": {"cal": 550, "prot": 45, "carb": 60, "fat": 15},
            "ingredientes": [
                {"item": "Presa de Pollo (Sin Piel)", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Arroz Integral / Quinua", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Culantro Licuado", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Zanahoria/Arvejas/Choclo", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pimiento Tiras", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Sellar pollo.\n2. Sofreír culantro.\n3. Cocinar arroz/quinua en esa base con las verduras y el pollo."
        },
        {
            "nombre": "Pollo Saltado (Poca Papa)",
            "descripcion": "Full verduras al wok.",
            "macros": {"cal": 480, "prot": 42, "carb": 40, "fat": 16},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Cebolla Roja (Gruesa)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Tomate (Gajos)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Sancochada (Dorada)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao y Vinagre", "cantidad": 20, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Wokear pollo a fuego alto.\n2. Saltar vegetales rápido.\n3. Mezclar."
        },
        {
            "nombre": "Carapulcra de Pollo",
            "descripcion": "Usando pechuga o chancho magro y papa seca.",
            "macros": {"cal": 520, "prot": 38, "carb": 55, "fat": 18},
            "ingredientes": [
                {"item": "Papa Seca (Hidratada)", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga/Chancho Magro", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Ají Panca", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Maní Tostado (Poco)", "cantidad": 10, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Yuca Sancochada", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Aderezo de ají panca.\n2. Cocinar papa seca con caldo.\n3. Agregar carne y maní al final."
        },
        {
            "nombre": "Ají de Pollo Saludable",
            "descripcion": "Espesado con quinua o pan integral y leche light.",
            "macros": {"cal": 510, "prot": 40, "carb": 45, "fat": 18},
            "ingredientes": [
                {"item": "Pechuga Deshilachada", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Crema Ají Amarillo", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 50, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Quinua Cocida (Espesar)", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pecan/Huevo/Aceituna", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Aderezo amarillo.\n2. Licuar quinua/pan con leche.\n3. Mezclar con pollo."
        },
        {
            "nombre": "Aguadito de Pollo",
            "descripcion": "Sopa espesa, reconfortante y llena de verduras.",
            "macros": {"cal": 450, "prot": 35, "carb": 50, "fat": 12},
            "ingredientes": [
                {"item": "Presa de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Arroz", "cantidad": 60, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Culantro Licuado", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Zapallo/Zanahoria/Pimiento", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arvejas", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Base de aguadito (culantro).\n2. Hervir pollo y arroz.\n3. Agregar verduras al final."
        },
        {
            "nombre": "Picante de Quinua con Carne",
            "descripcion": "Guiso potente de quinua con ají panca.",
            "macros": {"cal": 500, "prot": 38, "carb": 55, "fat": 15},
            "ingredientes": [
                {"item": "Quinua Perlada (Cruda)", "cantidad": 60, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Carne Picada/Molida", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Ají Panca", "cantidad": 15, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Queso Fresco", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Papa (Cubos)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Aderezo rojo.\n2. Cocinar quinua y papa con caldo.\n3. Agregar carne y queso."
        },
        {
            "nombre": "Lentejas con Chuleta Ahumada",
            "descripcion": "Retirar grasa visible de la chuleta.",
            "macros": {"cal": 560, "prot": 45, "carb": 55, "fat": 18},
            "ingredientes": [
                {"item": "Lentejas Guisadas", "cantidad": 200, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Chuleta Ahumada (Magra)", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Ensalada Fresca", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Arroz Blanco", "cantidad": 60, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Lentejas guisadas clásicas.\n2. Dorar chuleta.\n3. Servir con porción controlada de arroz."
        },
        {
            "nombre": "Pabellón Criollo Fit",
            "descripcion": "Carne mechada, caraotas, arroz y plátano al horno.",
            "macros": {"cal": 600, "prot": 42, "carb": 70, "fat": 16},
            "ingredientes": [
                {"item": "Carne Mechada", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Caraotas Negras", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Arroz Integral", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Plátano Maduro (Horno)", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Carne sudada con tomate.\n2. Caraotas sin azúcar.\n3. Plátano en Airfryer/Horno."
        },
        {
            "nombre": "Berenjenas Rellenas de Carne",
            "descripcion": "Bajo en carbohidratos, alto volumen.",
            "macros": {"cal": 400, "prot": 35, "carb": 15, "fat": 20},
            "ingredientes": [
                {"item": "Berenjena Grande", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Pasta de Tomate", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Queso Mozzarella", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Vaciar berenjena y picar pulpa.\n2. Sofreír carne con pulpa.\n3. Rellenar y gratinar."
        },
        {
            "nombre": "Calabacines (Zapallito) Rellenos",
            "descripcion": "Similar a la berenjena pero más suave.",
            "macros": {"cal": 380, "prot": 32, "carb": 12, "fat": 20},
            "ingredientes": [
                {"item": "Calabacín Italiano", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pollo en Cubos", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Choclo Desgranado", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Fresco", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Hervir zapallitos 5 min.\n2. Ahuecar y rellenar con salteado de pollo.\n3. Gratinar."
        },
        {
            "nombre": "Caigua Rellena",
            "descripcion": "Clásico peruano ligero.",
            "macros": {"cal": 350, "prot": 32, "carb": 20, "fat": 15},
            "ingredientes": [
                {"item": "Caigua", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo Duro / Pasas", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pan remojado (poco)", "cantidad": 10, "unidad": "g", "pasillo": "🍞 Panadería"}
            ],
            "instrucciones": "1. Relleno de carne guisada.\n2. Cocinar caiguas en vapor o salsa."
        },
        {
            "nombre": "Pollo al Horno con Lentejas",
            "descripcion": "Proteína fácil al horno.",
            "macros": {"cal": 550, "prot": 50, "carb": 40, "fat": 20},
            "ingredientes": [
                {"item": "Pierna con Muslo (sin piel)", "cantidad": 200, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Lentejas Guisadas", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Ensalada Rusa (Yogurt)", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Limón/Orégano", "cantidad": 5, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Marinar pollo y hornear 45 min.\n2. Servir con lentejas."
        },
        {
            "nombre": "Chaufa de Quinua",
            "descripcion": "Fusión chifa usando quinua.",
            "macros": {"cal": 500, "prot": 40, "carb": 45, "fat": 16},
            "ingredientes": [
                {"item": "Quinua Cocida", "cantidad": 150, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pollo/Chancho (Cubos)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo (Tortilla)", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Cebolla China/Kion", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao", "cantidad": 10, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Saltear carnes.\n2. Agregar quinua y tortilla picada.\n3. Sazonar con sillao."
        },
        {
            "nombre": "Adobo de Chancho",
            "descripcion": "Lomo de cerdo marinado.",
            "macros": {"cal": 510, "prot": 45, "carb": 40, "fat": 18},
            "ingredientes": [
                {"item": "Lomo de Cerdo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Ají Panca/Vinagre", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Camote Sancochado", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Cebolla (Pluma)", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Marinar cerdo noche anterior.\n2. Sudar con cebolla.\n3. Acompañar con camote."
        }
    ],

    "Cenas": [
        {
            "nombre": "Crema de Zapallo con Pollo",
            "descripcion": "Ligera y digestiva. Espesada con papa.",
            "macros": {"cal": 300, "prot": 30, "carb": 30, "fat": 8},
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pechuga Pollo (Desmechada)", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Papa Amarilla", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 30, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Fresco (Topping)", "cantidad": 20, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Hervir zapallo y papa. Licuar con leche.\n2. Servir con pollo y queso."
        },
        {
            "nombre": "Sopa de Menudencias",
            "descripcion": "Aprovechando el pollo entero. Alta en colágeno.",
            "macros": {"cal": 320, "prot": 35, "carb": 25, "fat": 10},
            "ingredientes": [
                {"item": "Menudencia (Hígado/Molleja)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Fideo Cabello Ángel", "cantidad": 25, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo/Apio/Zanahoria", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Kion (Jengibre)", "cantidad": 5, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir menudencias y kion.\n2. Agregar verduras picadas.\n3. Fideos al final."
        },
        {
            "nombre": "Tortilla de Espinacas",
            "descripcion": "Cena rápida low-carb.",
            "macros": {"cal": 280, "prot": 22, "carb": 8, "fat": 18},
            "ingredientes": [
                {"item": "Huevos (2 claras 1 yema)", "cantidad": 3, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Espinaca", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Queso Fresco", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Champiñones (Opcional)", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Saltear espinaca.\n2. Batir huevos y agregar.\n3. Cuajar en sartén."
        },
        {
            "nombre": "Torrejas de Coliflor",
            "descripcion": "Manera deliciosa de comer vegetales.",
            "macros": {"cal": 250, "prot": 15, "carb": 18, "fat": 12},
            "ingredientes": [
                {"item": "Coliflor (Hervida/Picada)", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Huevo", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Harina/Avena (Ligante)", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Cebollita China", "cantidad": 10, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar coliflor picada con huevo y harina.\n2. Freír en sartén con poco aceite (o Airfryer)."
        },
        {
            "nombre": "Ensalada Rusa con Pollo (Fit)",
            "descripcion": "Beterraga y zanahoria con dressing de yogurt.",
            "macros": {"cal": 350, "prot": 35, "carb": 30, "fat": 8},
            "ingredientes": [
                {"item": "Pechuga Plancha", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Beterraga (Cubos)", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Zanahoria/Vainita", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego (Aderezo)", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Mezclar verduras cocidas con yogurt, sal y limón.\n2. Acompañar con el pollo."
        },
        {
            "nombre": "Ensalada de Atún Vakimu",
            "descripcion": "Fresco y rápido.",
            "macros": {"cal": 320, "prot": 35, "carb": 15, "fat": 12},
            "ingredientes": [
                {"item": "Atún en Agua", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Lechuga/Pepino/Tomate", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Palta", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Mezclar todo en un bowl."
        },
        {
            "nombre": "Pan Árabe Pizza",
            "descripcion": "Mata el antojo.",
            "macros": {"cal": 380, "prot": 22, "carb": 40, "fat": 14},
            "ingredientes": [
                {"item": "Pan Árabe Delgado", "cantidad": 1, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Queso Mozzarella/Fresco", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Jamón Pavo", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Pasta Tomate/Orégano", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Armar pizza.\n2. Calentar hasta derretir queso."
        },
        {
            "nombre": "Wrap de Lechuga (Tacos)",
            "descripcion": "Usando lechuga como tortilla.",
            "macros": {"cal": 310, "prot": 30, "carb": 12, "fat": 18},
            "ingredientes": [
                {"item": "Carne Molida Guisada", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Lechuga Americana", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Palta", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pico de Gallo", "cantidad": 50, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Servir carne sobre hojas de lechuga.\n2. Agregar toppings."
        },
        {
            "nombre": "Pastelón de Coliflor",
            "descripcion": "Como un pastel de papa, pero de coliflor.",
            "macros": {"cal": 290, "prot": 25, "carb": 15, "fat": 15},
            "ingredientes": [
                {"item": "Coliflor (Puré)", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida (Relleno)", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Huevo (Para pintar)", "cantidad": 1, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Queso Parmesano (Poco)", "cantidad": 10, "unidad": "g", "pasillo": "🧀 Charcutería"}
            ],
            "instrucciones": "1. Hacer puré de coliflor (sin mucha agua).\n2. Poner capa de carne y cubrir con puré.\n3. Gratinar."
        },
        {
            "nombre": "Spaghetti de Calabacín con Atún",
            "descripcion": "Zoodles bajos en calorías.",
            "macros": {"cal": 280, "prot": 30, "carb": 12, "fat": 10},
            "ingredientes": [
                {"item": "Calabacín (Tiras/Espiral)", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Atún en Agua", "cantidad": 120, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Salsa de Tomate Casera", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Aceitunas", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Saltear calabacín 2 min.\n2. Mezclar con salsa y atún."
        }
    ]
}
