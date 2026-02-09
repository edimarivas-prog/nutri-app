# recetas.py - VERSIÓN ESTANDARIZADA (SIN DUPLICADOS)

RECETARIO = {
    "Desayunos": [
        {
            "nombre": "Arepa Reina Pepiada (Fit)",
            "descripcion": "Relleno cremoso fit.",
            "macros": {"cal": 450, "prot": 28, "carb": 45, "fat": 18},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pechuga de Pollo", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Palta (Aguacate)", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego Vakimu", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"},
                {"item": "Cilantro/Cebolla", "cantidad": 20, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Asar arepa. Mezclar pollo desmechado con yogurt y palta."
        },
        {
            "nombre": "Arepa con Perico",
            "descripcion": "Huevos revueltos.",
            "macros": {"cal": 420, "prot": 22, "carb": 42, "fat": 18},
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Huevos", "cantidad": 2, "unidad": "und", "pasillo": "🥛 Lácteos"},
                {"item": "Tomate y Cebolla", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Aceite de Oliva", "cantidad": 5, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Sofreír vegetales, agregar huevos."
        },
        {
            "nombre": "Panquecas Proteicas",
            "descripcion": "Con avena y proteína.",
            "macros": {"cal": 350, "prot": 35, "carb": 40, "fat": 6},
            "ingredientes": [
                {"item": "Avena", "cantidad": 40, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Scoop Proteína", "cantidad": 1, "unidad": "und", "pasillo": "💊 Suplementos"},
                {"item": "Huevos", "cantidad": 3, "unidad": "claras", "pasillo": "🥛 Lácteos"},
                {"item": "Fresas", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Licuar y cocinar en sartén."
        }
    ],

    "Almuerzos": [
        {
            "nombre": "Arroz con Pollo Fit",
            "descripcion": "Integral y mucho culantro.",
            "macros": {"cal": 550, "prot": 45, "carb": 60, "fat": 15},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Arroz Integral", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Culantro/Verduras", "cantidad": 130, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Guisar pollo con culantro y arroz."
        },
        {
            "nombre": "Pollo Saltado",
            "descripcion": "Al wok.",
            "macros": {"cal": 480, "prot": 42, "carb": 40, "fat": 16},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Cebolla y Tomate", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Papa Sancochada", "cantidad": 100, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao", "cantidad": 20, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Saltear pollo y verduras a fuego alto."
        },
        {
            "nombre": "Carapulcra de Pollo",
            "descripcion": "Con papa seca.",
            "macros": {"cal": 520, "prot": 38, "carb": 55, "fat": 18},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Papa Seca", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Ají Panca", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Guisar papa seca con ají y pollo."
        },
        {
            "nombre": "Ají de Pollo Saludable",
            "descripcion": "Con leche light.",
            "macros": {"cal": 510, "prot": 40, "carb": 45, "fat": 18},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Crema Ají Amarillo", "cantidad": 30, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 50, "unidad": "ml", "pasillo": "🥛 Lácteos"},
                {"item": "Quinua Cocida", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Deshilachar pollo cocido. Mezclar con salsa."
        },
        {
            "nombre": "Aguadito de Pollo",
            "descripcion": "Sopa espesa.",
            "macros": {"cal": 450, "prot": 35, "carb": 50, "fat": 12},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Arroz", "cantidad": 60, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Culantro/Verduras", "cantidad": 140, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir todo junto."
        },
        {
            "nombre": "Pabellón Criollo Fit",
            "descripcion": "Carne mechada.",
            "macros": {"cal": 600, "prot": 42, "carb": 70, "fat": 16},
            "ingredientes": [
                {"item": "Carne Molida Magra", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Caraotas Negras", "cantidad": 100, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Arroz Integral", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Plátano Maduro", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Usar carne magra en lugar de falda grasosa."
        },
         {
            "nombre": "Caigua Rellena",
            "descripcion": "Rellena de carne.",
            "macros": {"cal": 350, "prot": 32, "carb": 20, "fat": 15},
            "ingredientes": [
                {"item": "Caigua", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Carne Molida Magra", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Huevo Duro", "cantidad": 30, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Rellenar y guisar."
        }
    ],

    "Cenas": [
        {
            "nombre": "Crema de Zapallo con Pollo",
            "descripcion": "Ligera.",
            "macros": {"cal": 300, "prot": 30, "carb": 30, "fat": 8},
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 250, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pechuga de Pollo", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Papa Amarilla", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Leche Light", "cantidad": 30, "unidad": "ml", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Licuar zapallo cocido con leche. Agregar pollo."
        },
        {
            "nombre": "Ensalada Rusa con Pollo",
            "descripcion": "Con yogurt.",
            "macros": {"cal": 350, "prot": 35, "carb": 30, "fat": 8},
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"}, # Estandarizado
                {"item": "Beterraga y Zanahoria", "cantidad": 160, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego Vakimu", "cantidad": 30, "unidad": "g", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Mezclar verduras con yogurt."
        },
        {
            "nombre": "Sopa de Menudencias",
            "descripcion": "Sustanciosa.",
            "macros": {"cal": 320, "prot": 35, "carb": 25, "fat": 10},
            "ingredientes": [
                {"item": "Menudencia (Hígado/Molleja)", "cantidad": 150, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Fideo Cabello Ángel", "cantidad": 25, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Zapallo Macre", "cantidad": 150, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Hervir menudencias con verduras."
        },
        {
            "nombre": "Pan Árabe Pizza",
            "descripcion": "Rápida.",
            "macros": {"cal": 380, "prot": 22, "carb": 40, "fat": 14},
            "ingredientes": [
                {"item": "Pan Árabe", "cantidad": 1, "unidad": "und", "pasillo": "🍞 Panadería"},
                {"item": "Queso Fresco", "cantidad": 40, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Jamón Pavo", "cantidad": 30, "unidad": "g", "pasillo": "🧀 Charcutería"},
                {"item": "Pasta Tomate", "cantidad": 20, "unidad": "g", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Armar y calentar."
        }
    ]
}
