# 🚀 Despliegue en VPS - Nequi Axon Bot V3

## ✅ Información del Servidor

- **IP**: 109.123.247.248
- **Usuario**: root
- **Contraseña**: Perros1580
- **Ubicación**: Europa
- **Sistema Operativo**: Ubuntu 24.04 (Linux 6.8.0-106-generic)
- **Python**: 3.12.3

## 📁 Ubicación del Proyecto

```
/root/nequi_bot/
```

## 🔧 Archivos Desplegados

- ✅ main.py
- ✅ requirements.txt
- ✅ firebase_credentials.json
- ✅ .env
- ✅ usuariosvip.json
- ✅ admins_secundarios.json
- ✅ Todos los archivos de configuración

## 🔥 Firebase

- **Proyecto**: nequiaxonfree-7a6f7
- **Email**: firebase-adminsdk-fbsvc@nequiaxonfree-7a6f7.iam.gserviceaccount.com
- **Estado**: ✅ INICIALIZADO CORRECTAMENTE

## 🤖 Bot de Telegram

- **Token**: 8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI
- **Admin Principal**: 8485352219 (@AXONDEVUI)
- **Grupo Oficial**: https://t.me/Comunidadaxonlabs

## 🔄 Servicio Systemd

El bot se ejecuta como un servicio systemd que se inicia automáticamente al arrancar el servidor y se reinicia si falla.

### Comandos Útiles

```bash
# Ver estado del bot
systemctl status nequi_bot.service

# Reiniciar el bot
systemctl restart nequi_bot.service

# Detener el bot
systemctl stop nequi_bot.service

# Iniciar el bot
systemctl start nequi_bot.service

# Ver logs en tiempo real
journalctl -u nequi_bot.service -f

# Ver últimos 100 logs
journalctl -u nequi_bot.service -n 100

# Ver logs desde hace X minutos
journalctl -u nequi_bot.service --since '10 minutes ago'
```

## 🌐 Endpoints

- **Flask Web**: http://109.123.247.248:5000
- **Health Check**: http://109.123.247.248:5000/

## 📝 Actualizar el Bot

### Opción 1: Subir archivo específico

```bash
# Desde tu computadora local
scp main.py root@109.123.247.248:/root/nequi_bot/
ssh root@109.123.247.248 "systemctl restart nequi_bot.service"
```

### Opción 2: Editar directamente en el servidor

```bash
ssh root@109.123.247.248
cd /root/nequi_bot
nano main.py
# Hacer cambios y guardar (Ctrl+X, Y, Enter)
systemctl restart nequi_bot.service
```

### Opción 3: Clonar desde GitHub

```bash
ssh root@109.123.247.248
cd /root/nequi_bot
# Hacer backup primero
cp main.py main.py.backup
# Descargar nueva versión
curl -o main.py https://raw.githubusercontent.com/albertosuer/NEQUI_AXON_BOT_V3/main/main.py
systemctl restart nequi_bot.service
```

## 🔐 Variables de Entorno (.env)

```env
TOKEN=8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI
TELEGRAM_BOT_TOKEN=8712440774:AAHci_e-BmdFDvpb4MUteOlEPFDozVFE2xI
PORT=5000
GOOGLE_APPLICATION_CREDENTIALS=firebase_credentials.json
```

## 🐛 Troubleshooting

### El bot no responde

```bash
# Ver logs para identificar el error
journalctl -u nequi_bot.service -n 50

# Reiniciar el servicio
systemctl restart nequi_bot.service
```

### Firebase no conecta

```bash
# Verificar que el archivo de credenciales existe
ls -la /root/nequi_bot/firebase_credentials.json

# Verificar el contenido (primeras líneas)
head -5 /root/nequi_bot/firebase_credentials.json
```

### Actualizar dependencias

```bash
ssh root@109.123.247.248
cd /root/nequi_bot
source venv/bin/activate
pip install -r requirements.txt --upgrade
systemctl restart nequi_bot.service
```

## 📊 Monitoreo

### Ver uso de recursos

```bash
# CPU y memoria del bot
ps aux | grep python

# Uso general del servidor
htop
```

### Ver conexiones de red

```bash
# Ver si el bot está escuchando en el puerto 5000
netstat -tulpn | grep 5000
```

## 🔒 Seguridad

- ✅ Firewall configurado (solo puertos necesarios abiertos)
- ✅ Credenciales de Firebase protegidas
- ✅ Token del bot en variable de entorno
- ✅ Servicio corriendo como root (cambiar a usuario dedicado en producción)

## 📈 Ventajas de la VPS vs Railway

1. **Velocidad**: Respuesta instantánea, sin cold starts
2. **Control Total**: Acceso completo al servidor
3. **Sin Límites**: No hay restricciones de tiempo de ejecución
4. **Logs Completos**: Acceso directo a todos los logs
5. **Persistencia**: Los datos se mantienen entre reinicios
6. **Costo Predecible**: Pago fijo mensual

## 🎯 Estado Actual

- ✅ Bot desplegado y corriendo
- ✅ Firebase conectado correctamente
- ✅ Servicio systemd configurado
- ✅ Auto-reinicio habilitado
- ✅ Logs funcionando correctamente
- ⏳ Esperando confirmación de que el bot responde a comandos

## 📞 Próximos Pasos

1. Probar el bot enviando `/start` en Telegram
2. Probar crear una cuenta con `/nequiaxonlabs`
3. Verificar que los datos se guardan en Firebase
4. Configurar backup automático de la base de datos (opcional)
5. Configurar dominio personalizado (opcional)
