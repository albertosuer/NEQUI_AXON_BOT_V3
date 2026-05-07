#!/usr/bin/env python3
import firebase_admin
from firebase_admin import credentials, firestore
import sys

print("1. Cargando credenciales...")
cred = credentials.Certificate('/root/nequi_bot/firebase_credentials.json')

print("2. Inicializando Firebase...")
firebase_admin.initialize_app(cred)

print("3. Creando cliente Firestore...")
db = firestore.client()

print("4. Guardando documento de prueba...")
db.collection('users').document('TEST999').set({'test': 'ok', 'timestamp': '2024-01-01'})

print("5. Verificando...")
doc = db.collection('users').document('TEST999').get()
if doc.exists:
    print("✅ FIREBASE FUNCIONA PERFECTAMENTE")
    print(f"Datos: {doc.to_dict()}")
    db.collection('users').document('TEST999').delete()
    print("✅ Test limpiado")
else:
    print("❌ No se guardó")
    sys.exit(1)
