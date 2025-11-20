"""
Quick Start Script - Digital Twin Health MVP
Run this to set up and start the application
"""
import os
import sys
import subprocess


def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def check_env_file():
    """Check if .env file exists"""
    if not os.path.exists('.env'):
        print("⚠️  No se encontró archivo .env")
        print("\nPor favor:")
        print("1. Copia .env.example a .env")
        print("2. Edita .env y agrega tu OPENAI_API_KEY")
        print("\nEjemplo:")
        print("  cp .env.example .env")
        print("  # Luego edita .env con tu API key de OpenAI")
        return False
    return True


def check_database():
    """Check database configuration"""
    print("📊 Verificando configuración de base de datos...")

    # Import here to avoid errors if dependencies not installed
    try:
        from app.config import settings
        print(f"✅ Base de datos: {settings.database_url.split('@')[-1] if '@' in settings.database_url else 'configurada'}")
        return True
    except Exception as e:
        print(f"❌ Error en configuración de base de datos: {e}")
        return False


def init_database():
    """Initialize database"""
    print_header("Inicializando Base de Datos")

    try:
        print("🔧 Creando tablas...")
        subprocess.run([sys.executable, "db/init_db.py"], check=True)

        print("\n🌱 Generando 300 pacientes sintéticos...")
        subprocess.run([sys.executable, "db/seed_synthetic_data.py"], check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error inicializando base de datos: {e}")
        return False


def start_server():
    """Start the FastAPI server"""
    print_header("Iniciando Servidor")

    print("🚀 Iniciando FastAPI en http://localhost:8000")
    print("\n📱 Frontends disponibles:")
    print("   - Chat 'Yo del Futuro':    http://localhost:8000/chat-ui")
    print("   - Dashboard Paciente:      http://localhost:8000/patient-dashboard")
    print("   - Plataforma Asegurador:   http://localhost:8000/insurer-platform")
    print("\n📚 Documentación API:         http://localhost:8000/docs")
    print("\n⏹️  Para detener: Ctrl+C\n")

    try:
        subprocess.run(["uvicorn", "app.main:app", "--reload"])
    except KeyboardInterrupt:
        print("\n\n👋 Servidor detenido. ¡Hasta luego!")


def main():
    """Main setup and start process"""
    print_header("🏥 Digital Twin Health MVP - Quick Start")

    # Step 1: Check environment
    if not check_env_file():
        sys.exit(1)

    # Step 2: Check database config
    if not check_database():
        print("\n💡 Tip: Asegúrate de tener PostgreSQL corriendo y configurado en .env")
        sys.exit(1)

    # Step 3: Ask if user wants to initialize database
    print("\n¿Deseas inicializar la base de datos?")
    print("(Solo necesario la primera vez o si quieres regenerar datos)")
    choice = input("Inicializar base de datos? (s/N): ").strip().lower()

    if choice == 's':
        if not init_database():
            sys.exit(1)
    else:
        print("⏭️  Saltando inicialización de base de datos")

    # Step 4: Start server
    start_server()


if __name__ == "__main__":
    main()
