#!/usr/bin/env python3
"""
Script para probar que Firebase funciona correctamente
"""
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

print("🔥 Probando Firebase...")

try:
    # Inicializar Firebase
    cred = credentials.Certificate('firebase_credentials.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("✅ Firebase inicializado")
    
    # Crear un usuario de prueba
    test_phone = "9999999999"
    test_data = {
        'name': 'TEST',
        'pin': '0000',
        'saldo': '999999',
        'isActive': True,
        'created_by': 'test_script',
        'telegram_username': 'test',
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    print(f"💾 Guardando usuario de prueba: {test_phone}")
    db.collection('users').document(test_phone).set(test_data)
    print("✅ Usuario guardado")
    
    # Verificar que se guardó
    doc = db.collection('users').document(test_phone).get()
    if doc.exists:
        print("✅ Usuario verificado en Firebase")
        print(f"📄 Datos: {doc.to_dict()}")
        
        # Eliminar el usuario de prueba
        db.collection('users').document(test_phone).delete()
        print("✅ Usuario de prueba eliminado")
        
        print("\n" + "="*60)
        print("🎉 FIREBASE FUNCIONA PERFECTAMENTE")
        print("="*60)
    else:
        print("❌ ERROR: Usuario no se guardó")
        
except Exception as e:
    print(f"❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
