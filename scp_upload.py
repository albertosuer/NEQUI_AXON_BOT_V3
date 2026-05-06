import paramiko
import sys

def scp_upload(local_file, remote_path, host="109.123.247.248", username="root", password="Perros1580"):
    """Sube un archivo usando SCP"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(host, username=username, password=password, timeout=10)
        sftp = client.open_sftp()
        sftp.put(local_file, remote_path)
        sftp.close()
        print(f"✅ Archivo {local_file} subido a {remote_path}")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1
    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python scp_upload.py archivo_local ruta_remota")
        sys.exit(1)
    
    exit_code = scp_upload(sys.argv[1], sys.argv[2])
    sys.exit(exit_code)
