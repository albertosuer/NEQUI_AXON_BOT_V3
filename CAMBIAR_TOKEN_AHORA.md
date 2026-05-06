# 🔧 CAMBIAR TOKEN DEL BOT - PASO A PASO

## ⚠️ PROBLEMA
Hay OTRA instancia del bot corriendo (Railway/Zeabur) con el mismo token.
Telegram NO permite 2 instancias con el mismo token.

## ✅ SOLUCIÓN: CAMBIAR EL TOKEN (5 MINUTOS)

### PASO 1: Generar nuevo token en Telegram

1. Abre Telegram
2. Busca: **@BotFather**
3. Envía: `/mybots`
4. Selecciona: **NEQUI VIPS ORG**
5. Haz clic en: **API Token**
6. Haz clic en: **Revoke current token**
7. Confirma: **Yes, I'm sure**
8. **COPIA EL NUEVO TOKEN** (algo como: `8712440774:AAH...`)

### PASO 2: Actualizar token en la VPS

Ejecuta este comando en tu computadora:

```bash
python ssh_helper.py "nano /root/nequi_bot/.env"
```

Se abrirá el editor. Verás algo como:
```
TOKEN=8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI
```

**Cambia** esa línea con el nuevo token que copiaste:
```
TOKEN=TU_NUEVO_TOKEN_AQUI
```

**Guardar:**
1. Presiona: `Ctrl + O` (guardar)
2. Presiona: `Enter` (confirmar)
3. Presiona: `Ctrl + X` (salir)

### PASO 3: Reiniciar el bot

```bash
python ssh_helper.py "systemctl restart nequi_bot"
```

### PASO 4: Verificar que funciona

```bash
python test_bot.py
```

O envía `/start` al bot en Telegram.

## 🎉 LISTO

El bot responderá INMEDIATAMENTE porque ya no habrá conflicto.

---

## 📝 ALTERNATIVA: Detener Railway

Si prefieres NO cambiar el token:

1. Ve a https://railway.app
2. Inicia sesión
3. Busca tu proyecto del bot
4. Haz clic en el proyecto
5. Ve a "Settings"
6. Haz clic en "Pause Deployment" o "Delete Service"

Luego reinicia el bot en la VPS:
```bash
python ssh_helper.py "systemctl restart nequi_bot"
```

---

**ELIGE UNA OPCIÓN Y HAZLO AHORA** ⚡
