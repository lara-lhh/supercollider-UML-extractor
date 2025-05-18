
import subprocess
import sys
import tempfile
from pathlib import Path
import shutil

def get_sclang_path():
    path = shutil.which("sclang")
    if not path:
        print("   No se encontró 'sclang' en tu sistema.")
        print("   Asegúrate de tener SuperCollider instalado y 'sclang' en tu PATH.")
        print("   Puedes descargarlo desde: https://supercollider.github.io/")
        sys.exit(1)
    return path

def get_descendants_from_sclang(root_class, sclang_path):
    sc_code = f"""
(
var printTree;
printTree = {{ |cls|
    cls.subclasses.do {{ |sub|
        (sub.name ++ " --|> " ++ cls.name).postln;
        printTree.(sub);
    }};
}};
printTree.({root_class});
0.exit;
)
"""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".scd", mode="w", encoding="utf-8") as tmpfile:
        tmpfile.write(sc_code)
        sc_file_path = tmpfile.name

    try:
        result = subprocess.run(
            [sclang_path, sc_file_path],
            capture_output=True,
            timeout=60
        )
        if result.returncode != 0:
            print("Error ejecutando sclang:")
            print(result.stderr.decode())
            sys.exit(1)
        output = result.stdout.decode()
        return [line.strip() for line in output.splitlines() if "--|>" in line]
    finally:
        Path(sc_file_path).unlink(missing_ok=True)

def generate_puml(lines, output_file, root_class):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("@startuml\n")
        f.write("skinparam classAttributeIconSize 0\n\n")
        f.write(f"class {root_class}\n")
        for line in lines:
            child, parent = [part.strip() for part in line.split("--|>")]
            f.write(f"class {child}\n")
            f.write(f"class {parent}\n")
            f.write(f"{child} --|> {parent}\n")
        f.write("@enduml\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python sclang_hierarchy.py <ClaseRaíz>")
        sys.exit(1)

    sclang_path = get_sclang_path()
    root = sys.argv[1]
    relations = get_descendants_from_sclang(root, sclang_path)
    generate_puml(relations, f"{root}_sclang_uml.puml", root)
    print(f"Diagrama generado: {root}_sclang_uml.puml")
