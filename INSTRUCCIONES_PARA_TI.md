# 📋 INSTRUCCIONES PARA TI - ALBERTO

## 🎯 SITUACIÓN ACTUAL

Tu bot está **100% funcional y corriendo en la VPS**, pero hay un problema:

### ❌ PROBLEMA
Hay **OTRA INSTANCIA** del bot corriendo en algún lugar usando el mismo token. Esto causa un conflicto y el bot no puede responder.

**Error que aparece:**
```
telegram.error.Conflict: terminated by other getUpdates request
```

## ✅ SOLUCIÓN RÁPIDA (ELIGE UNA)

### OPCIÓN 1: Detener Railway (MÁS PROBABLE)
1. Ve a https://railway.app
2. Inicia sesión
3. Busca tu proyecto del bot
4. Haz clic en el proyecto
5. Ve a "Settings" → "Danger Zone"
6. Haz clic en "Pause Deployment" o "Delete Service"
7. **¡LISTO!** El bot en la VPS empezará a funcionar inmediatamente

### OPCIÓN 2: Detener Zeabur
1. Ve a https://zeabur.com
2. Busca tu proyecto
3. Detén o elimina el despliegue

### OPCIÓN 3: Cambiar el Token (SI NO ENCUENTRAS LA OTRA INSTANCIA)
1. Abre Telegram y busca **@BotFather**
2. Envía el comando: `/mybots`
3. Selecciona tu bot: **NEQUI VIPS ORG**
4. Haz clic en "API Token"
5. Haz clic en "Revoke current token"
6. Copia el nuevo token
7. Ejecuta en tu computadora:
   ```bash
   python ssh_helper.py "nano /root/nequi_bot/.env"
   ```
8. Cambia la línea `TOKEN=...` con el nuevo token
9. Guarda (Ctrl+O, Enter, Ctrl+X)
10. Reinicia el bot:
    ```bash
    python ssh_helper.py "systemctl restart nequi_bot"
    ```

## 🧪 CÓMO PROBAR QUE FUNCIONA

### Método 1: Desde tu computadora
```bash
python test_bot.py
```

### Método 2: Desde Telegram
1. Abre Telegram
2. Busca tu bot: **@nequivipsaxonlabsorgbot**
3. Envía: `/start`
4. Si responde = ✅ **¡FUNCIONA!**

## 📊 INFORMACIÓN IMPORTANTE

### Datos del Bot
- **Token actual:** `8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI`
- **Username:** `@nequivipsaxonlabsorgbot`
- **Tu ID (Admin):** `8485352219`

### Datos de la VPS
- **IP:** `109.123.247.248`
- **Usuario:** `root`
- **Contraseña:** `Perros1580`
- **Ubicación del bot:** `/root/nequi_bot/`

### Firebase
- **Proyecto:** `nequiaxonfree-7a6f7`
- **Estado:** ✅ Conectado y funcionando

## 🔧 COMANDOS ÚTILES

### Ver si el bot está corriendo
```bash
python ssh_helper.py "systemctl status nequi_bot"
```

### Ver logs en tiempo real
```bash
python ssh_helper.py "journalctl -u nequi_bot -f --no-pager"
```

### Reiniciar el bot
```bash
python ssh_helper.py "systemctl restart nequi_bot"
```

### Detener el bot
```bash
python ssh_helper.py "systemctl stop nequi_bot"
```

### Iniciar el bot
```bash
python ssh_helper.py "systemctl start nequi_bot"
```

## 📁 ARCHIVOS IMPORTANTES

En tu computadora tienes:
- `ssh_helper.py` - Para ejecutar comandos en la VPS
- `scp_upload.py` - Para subir archivos a la VPS
- `test_bot.py` - Para probar el bot
- `RESUMEN_FINAL.md` - Resumen completo
- `SOLUCION_CONFLICTO.md` - Detalles del problema

## 🚀 DESPUÉS DE RESOLVER EL CONFLICTO

Una vez que detengas la otra instancia:

1. **El bot responderá inmediatamente** ✅
2. Prueba con `/start` en Telegram
3. Crea una cuenta de prueba:
   ```
   /nequiaxonlabs 3001234567 1234 50000 Juan
   ```
4. Verifica que se guardó:
   ```
   /ver 3001234567
   ```

## ❓ SI TIENES PROBLEMAS

### El bot no responde después de detener Railway
Espera 30 segundos y reinicia:
```bash
python ssh_helper.py "systemctl restart nequi_bot"
```

### No puedo conectarme a la VPS
Verifica que tienes instalado `paramiko`:
```bash
pip install paramiko
```

### Olvidé mi contraseña de la VPS
La contraseña es: `Perros1580`

### Quiero ver los logs completos
```bash
python ssh_helper.py "journalctl -u nequi_bot -n 100 --no-pager"
```

## 📞 RESUMEN EN 3 PASOS

1. **Detén Railway/Zeabur** (o cambia el token)
2. **Espera 30 segundos**
3. **Prueba el bot** con `/start` en Telegram

**¡ESO ES TODO!** 🎉

---

**Fecha:** 7 de Mayo de 2026  
**Tu bot está listo y esperando que detengas la otra instancia** ✅
