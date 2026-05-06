#!/usr/bin/env python3
"""
Script para probar que el bot está respondiendo correctamente
"""
import requests
import sys

BOT_TOKEN = "8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def test_bot():
    """Prueba que el bot esté activo"""
    print("🔍 Probando bot de Telegram...")
    print(f"Token: {BOT_TOKEN[:20]}...")
    
    # 1. Verificar que el bot existe
    print("\n[1/3] Verificando bot...")
    response = requests.get(f"{BASE_URL}/getMe")
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            bot_info = data['result']
            print(f"✅ Bot encontrado: @{bot_info['username']}")
            print(f"   Nombre: {bot_info['first_name']}")
            print(f"   ID: {bot_info['id']}")
        else:
            print(f"❌ Error: {data}")
            return False
    else:
        print(f"❌ Error HTTP {response.status_code}")
        return False
    
    # 2. Verificar webhook
    print("\n[2/3] Verificando webhook...")
    response = requests.get(f"{BASE_URL}/getWebhookInfo")
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            webhook_info = data['result']
            if webhook_info['url']:
                print(f"⚠️ WEBHOOK ACTIVO: {webhook_info['url']}")
                print(f"   Esto puede causar conflictos con polling!")
                print(f"   Pending updates: {webhook_info.get('pending_update_count', 0)}")
                return False
            else:
                print(f"✅ No hay webhook configurado (correcto para polling)")
        else:
            print(f"❌ Error: {data}")
            return False
    else:
        print(f"❌ Error HTTP {response.status_code}")
        return False
    
    # 3. Ver últimas actualizaciones
    print("\n[3/3] Verificando actualizaciones...")
    response = requests.get(f"{BASE_URL}/getUpdates?limit=1")
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            updates = data['result']
            if updates:
                print(f"✅ Hay {len(updates)} actualización(es) pendiente(s)")
                last_update = updates[-1]
                print(f"   Última actualización ID: {last_update['update_id']}")
            else:
                print(f"✅ No hay actualizaciones pendientes")
        else:
            print(f"❌ Error: {data}")
            return False
    else:
        print(f"❌ Error HTTP {response.status_code}")
        return False
    
    print("\n" + "=" * 60)
    print("✅ TODAS LAS VERIFICACIONES PASARON")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_bot()
    sys.exit(0 if success else 1)
