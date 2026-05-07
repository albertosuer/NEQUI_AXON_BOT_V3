#!/usr/bin/env python3
import sys
sys.path.insert(0, '/root/nequi_bot/venv/lib/python3.12/site-packages')

print("1. Importando firebase_admin...")
import firebase_admin
print("✅ firebase_admin importado")

print("2. Importando credentials y firestore...")
from firebase_admin import credentials, firestore
print("✅ credentials y firestore importados")

print("3. Cargando credenciales...")
cred = credentials.Certificate('/root/nequi_bot/firebase_credentials.json')
print("✅ Credenciales cargadas")

print("4. Inicializando Firebase...")
firebase_admin.initialize_app(cred)
print("✅ Firebase inicializado")

print("5. Creando cliente Firestore...")
db = firestore.client()
print("✅ Cliente Firestore creado")

print("6. Guardando usuario de prueba...")
db.collection('users').document('TEST123').set({
    'name': 'PRUEBA',
    'pin': '1234',
    'saldo': '50000',
    'isActive': True
})
print("✅ Usuario guardado")

print("7. Verificando...")
doc = db.collection('users').document('TEST123').get()
if doc.exists:
    print("✅ Usuario verificado:", doc.to_dict())
    db.collection('users').document('TEST123').delete()
    print("✅ Usuario de prueba eliminado")
    print("\n🎉 FIREBASE FUNCIONA PERFECTAMENTE")
else:
    print("❌ No se pudo verificar")
