import paramiko
import sys
import time

def ssh_command(host, username, password, command, timeout=30):
    """Ejecuta un comando SSH con contraseña"""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(host, username=username, password=password, timeout=10)
        stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
        
        # Leer output en tiempo real
        while True:
            line = stdout.readline()
            if not line:
                break
            print(line, end='')
        
        # Leer errores
        error = stderr.read().decode()
        if error:
            print(error, file=sys.stderr)
        
        return stdout.channel.recv_exit_status()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    finally:
        client.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python ssh_helper.py 'comando'")
        sys.exit(1)
    
    command = sys.argv[1]
    exit_code = ssh_command("109.123.247.248", "root", "Perros1580", command)
    sys.exit(exit_code)
