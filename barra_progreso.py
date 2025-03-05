#By Claude.ai
import sys
import time

# Simulando una barra de progreso
def barra_progreso(total):
    for i in range(total + 1):
        porcentaje = i * 100 // total
        barra = "=" * (i * 20 // total)
        espacios = " " * (20 - len(barra))
        sys.stdout.write(f"\rProgreso: [{barra}{espacios}] {porcentaje}%")
        sys.stdout.flush()  # Fuerza la escritura inmediata
        time.sleep(0.1)
    sys.stdout.write("\n")

barra_progreso(100)