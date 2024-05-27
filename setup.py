from cx_Freeze import setup, Executable

setup(
    name="Trabajo Estrucutra de Datos",
    version="1.0",
    description="Sistema de archivos en Python",
    executables=[Executable("fileSystem.py", base="Win32GUI")]
)