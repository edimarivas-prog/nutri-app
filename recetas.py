# recetas.py

# Esta es la base de datos de tu aplicación.
# Las cantidades están calculadas para una "Persona Base" de ~2000 kcal (Tu nivel actual).
# La app ajustará estos números automáticamente si el peso del usuario cambia.

RECETARIO = {
    "Desayunos": [
        {
            "id": "DES_001",
            "nombre": "Arepa Fibra-Power (Relleno Mixto)",
            "descripcion": "Masa alta en fibra con perico y palta.",
            "ingredientes": [
                {"item": "Harina P.A.N.", "cantidad": 50, "unidad": "g", "tipo": "carb"},
                {"item": "Salvado de Trigo", "cantidad": 10, "unidad": "g", "tipo": "fibra"},
                {"item": "Semillas de Chía", "cantidad": 5, "unidad": "g", "tipo": "grasas"},
                {"item": "Huevos (Perico)", "cantidad": 2, "unidad": "und", "tipo": "proteina"},
                {"item": "Tomate y Cebolla", "cantidad": 50, "unidad": "g", "tipo": "vegetal"},
                {"item": "Palta", "cantidad": 30, "unidad": "g", "tipo": "grasas"},
                {"item": "Queso Fresco", "cantidad": 20, "unidad": "g", "tipo": "proteina"}
            ],
            "instrucciones": "Mezclar harinas y chía. Asar la arepa. Hacer perico con poco aceite."
        },
        {
            "id": "DES_002",
            "nombre": "Panquecas Bluhealth",
            "descripcion": "Altas en proteína para recuperación muscular.",
            "ingredientes": [
                {"item": "Avena en hojuelas", "cantidad": 40, "unidad": "g", "tipo": "carb"},
                {"item": "Claras de Huevo", "cantidad": 3, "unidad": "und", "tipo": "proteina"},
                {"item": "Proteína (Scoop)", "cantidad": 1, "unidad": "und", "tipo": "proteina"},
                {"item": "Fresas", "cantidad": 80, "unidad": "g", "tipo": "fibra"},
                {"item": "Miel (Toque)", "cantidad": 5, "unidad": "g", "tipo": "carb"}
            ],
            "instrucciones": "Licuar todo y hacer en sartén antiadherente."
        },
        {
             "id": "DES_003",
            "nombre": "Tostadas Multicereal con Atún",
            "descripcion": "Rápido y práctico.",
            "ingredientes": [
                {"item": "Pan Multicereal Vital", "cantidad": 2, "unidad": "rebanadas", "tipo": "carb"},
                {"item": "Atún en agua", "cantidad": 120, "unidad": "g", "tipo": "proteina"},
                {"item": "Cebolla y Tomate", "cantidad": 50, "unidad": "g", "tipo": "vegetal"},
                {"item": "Yogurt Griego (como mayo)", "cantidad": 20, "unidad": "g", "tipo": "grasas"}
            ],
            "instrucciones": "Mezclar atún con vegetales y yogurt. Servir sobre tostadas."
        }
    ],
    "Almuerzos": [
        {
            "id": "ALM_001",
            "nombre": "Pollo Saltado con Verduras",
            "descripcion": "Clásico peruano versión fit con menos papa.",
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "tipo": "proteina"},
                {"item": "Cebolla y Tomate (Gajos)", "cantidad": 150, "unidad": "g", "tipo": "vegetal"},
                {"item": "Papa Sancochada (Dorada)", "cantidad": 100, "unidad": "g", "tipo": "carb"},
                {"item": "Sillao y Vinagre", "cantidad": 10, "unidad": "ml", "tipo": "salsa"},
                {"item": "Arroz/Quinua", "cantidad": 0, "unidad": "g", "tipo": "carb"} 
            ],
            "instrucciones": "Saltar pollo a fuego alto. Añadir vegetales al final para que queden crocantes. Acompañar con la papa."
        },
        {
            "id": "ALM_002",
            "nombre": "Lentejas con Chuleta Magra",
            "descripcion": "Hierro y proteína potente.",
            "ingredientes": [
                {"item": "Lentejas Cocidas", "cantidad": 200, "unidad": "g", "tipo": "carb-pro"},
                {"item": "Chuleta Ahumada (Sin grasa)", "cantidad": 120, "unidad": "g", "tipo": "proteina"},
                {"item": "Ensalada Repollo/Zanahoria", "cantidad": 150, "unidad": "g", "tipo": "vegetal"},
                {"item": "Arroz", "cantidad": 80, "unidad": "g", "tipo": "carb"}
            ],
            "instrucciones": "Quitar la grasa visible de la chuleta. Servir lentejas con arroz pequeño."
        },
        {
            "id": "ALM_003",
            "nombre": "Chaufa de Quinua",
            "descripcion": "Reemplazo del arroz por quinua para más fibra.",
            "ingredientes": [
                {"item": "Quinua Cocida", "cantidad": 150, "unidad": "g", "tipo": "carb"},
                {"item": "Pollo en cubos", "cantidad": 150, "unidad": "g", "tipo": "proteina"},
                {"item": "Huevos (Tortilla picada)", "cantidad": 2, "unidad": "und", "tipo": "proteina"},
                {"item": "Cebolla China / Kion", "cantidad": 20, "unidad": "g", "tipo": "vegetal"},
                {"item": "Aceite de Ajonjolí", "cantidad": 5, "unidad": "ml", "tipo": "grasas"}
            ],
            "instrucciones": "Saltar quinua fría con el pollo y huevos."
        }
    ],
    "Cenas": [
        {
            "id": "CEN_001",
            "nombre": "Crema de Zapallo Proteica",
            "descripcion": "Ligera para dormir, reforzada con pollo.",
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 200, "unidad": "g", "tipo": "vegetal"},
                {"item": "Papa Amarilla", "cantidad": 50, "unidad": "g", "tipo": "carb"},
                {"item": "Pechuga Deshilachada", "cantidad": 120, "unidad": "g", "tipo": "proteina"},
                {"item": "Leche Gloria Light", "cantidad": 30, "unidad": "ml", "tipo": "liquido"}
            ],
            "instrucciones": "Cocinar verduras, licuar con leche. Servir con el pollo encima."
        },
        {
            "id": "CEN_002",
            "nombre": "Tortilla de Espinacas",
            "descripcion": "Cena ultra baja en carbos.",
            "ingredientes": [
                {"item": "Huevos (2 claras + 1 yema)", "cantidad": 3, "unidad": "und", "tipo": "proteina"},
                {"item": "Espinaca", "cantidad": 100, "unidad": "g", "tipo": "vegetal"},
                {"item": "Queso Fresco", "cantidad": 30, "unidad": "g", "tipo": "proteina"},
                {"item": "Pan Integral (Opcional)", "cantidad": 1, "unidad": "rebanada", "tipo": "carb"}
            ],
            "instrucciones": "Batir huevos con espinaca picada. Cuajar en sartén."
        }
    ],
    "Meriendas": [
         {
            "id": "MER_001",
            "nombre": "Batido Post-Entreno",
            "descripcion": "Recuperación rápida.",
            "ingredientes": [
                {"item": "Proteína (Scoop)", "cantidad": 1, "unidad": "und", "tipo": "proteina"},
                {"item": "Plátano", "cantidad": 100, "unidad": "g", "tipo": "carb"},
                {"item": "Agua/Hielo", "cantidad": 200, "unidad": "ml", "tipo": "liquido"}
            ]
        },
        {
            "id": "MER_002",
            "nombre": "Yogurt con Fruta",
            "descripcion": "Media tarde.",
            "ingredientes": [
                {"item": "Yogurt Griego Vakimu", "cantidad": 150, "unidad": "g", "tipo": "proteina"},
                {"item": "Fresas/Arándanos", "cantidad": 80, "unidad": "g", "tipo": "carb"},
                {"item": "Nueces/Almendras", "cantidad": 10, "unidad": "g", "tipo": "grasas"}
            ]
        }
    ]
}
