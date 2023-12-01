from cx_Freeze import setup, Executable

setup(
    name="multitela",
    version="0.1",
    description="Descrição do executável",
    executables=[Executable("main_multitela.py")],
)