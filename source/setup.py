from cx_Freeze import setup, Executable

base = None

executables = [
    Executable('taocomment.py', base=base)
]

setup(
    name="taocomment",
    version="1.0",
    description="hunterhug",
    executables=executables
)
