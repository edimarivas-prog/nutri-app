# recetas.py ACTUALIZADO

RECETARIO = {
    "Almuerzos": [
        {
            "nombre": "Pollo Saltado Fit",
            "descripcion": "Clásico peruano con menos papa y más verduras.",
            "imagen": "https://i.imgur.com/example_pollo.jpg", # Aquí pondremos links reales luego
            "ingredientes": [
                {"item": "Pechuga de Pollo", "cantidad": 180, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Cebolla Roja", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Tomate", "cantidad": 80, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Sillao (Salsa de Soja)", "cantidad": 10, "unidad": "ml", "pasillo": "🥫 Abarrotes"},
                {"item": "Vinagre", "cantidad": 5, "unidad": "ml", "pasillo": "🥫 Abarrotes"}
            ],
            "instrucciones": "1. Cortar pollo en tiras.\n2. Wokear a fuego alto.\n3. Añadir cebolla y tomate al final."
        },
        {
            "nombre": "Lentejas con Chuleta",
            "descripcion": "Potencia de hierro y proteína.",
            "imagen": "https://i.imgur.com/example_lentejas.jpg",
            "ingredientes": [
                {"item": "Lentejas", "cantidad": 80, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Chuleta Ahumada (Magra)", "cantidad": 120, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Zanahoria", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"}
            ],
            "instrucciones": "1. Cocinar lentejas.\n2. Dorar chuleta sin aceite extra."
        }
    ],
    "Desayunos": [
        {
            "nombre": "Arepa Reina Pepiada Light",
            "descripcion": "Relleno cremoso con yogurt en vez de mayonesa.",
            "imagen": "https://i.imgur.com/example_arepa.jpg",
            "ingredientes": [
                {"item": "Harina P.A.N", "cantidad": 50, "unidad": "g", "pasillo": "🥫 Abarrotes"},
                {"item": "Pollo Desmechado", "cantidad": 80, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Palta", "cantidad": 40, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Yogurt Griego", "cantidad": 20, "unidad": "g", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Mezclar pollo, palta y yogurt.\n2. Rellenar arepa asada."
        }
    ],
    "Cenas": [
        {
            "nombre": "Crema de Zapallo Proteica",
            "descripcion": "Cena ligera de digestión rápida.",
            "imagen": "https://i.imgur.com/example_zapallo.jpg",
            "ingredientes": [
                {"item": "Zapallo Macre", "cantidad": 200, "unidad": "g", "pasillo": "🥦 Verdulería"},
                {"item": "Pollo (para licuar o trozos)", "cantidad": 100, "unidad": "g", "pasillo": "🥩 Carnicería"},
                {"item": "Leche Light", "cantidad": 30, "unidad": "ml", "pasillo": "🥛 Lácteos"}
            ],
            "instrucciones": "1. Hervir zapallo.\n2. Licuar con leche.\n3. Agregar pollo."
        }
    ]
}
