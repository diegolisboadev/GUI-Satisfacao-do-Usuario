import sys
from cx_Freeze import setup, Executable
import dialog


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("satisfacao.py", base=base, targetName="Satisfacao", icon="sorriso.ico")
]

buildOptions = dict(
        packages = [],
        includes = ['dialog'],
        include_files = ['sorriso.ico', 'ruim.png', 'bom.png', 'regular.png', 'otimo.png',
                         'excelente.png', 'sair.png', 'ajudar.png'],
        excludes = []
)




setup(
    name = "Satisfação",
    version = "1.0",
    description = "Sistema de Satisfação do Usuário",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
