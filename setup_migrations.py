#!/usr/bin/env python
import subprocess

print("Iniciando configuración de migraciones...")
subprocess.call(['flask', 'db', 'init'])
subprocess.call(['flask', 'db', 'migrate', '-m', '"Migración inicial"'])
subprocess.call(['flask', 'db', 'upgrade'])
print("Migraciones aplicadas correctamente.")