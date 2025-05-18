
# SuperCollider UML Extractor

Este proyecto permite generar automáticamente diagramas UML de clases en SuperCollider, 
partiendo de la jerarquía de clases extraída usando el propio lenguaje `sclang`.

## 🚀 Requisitos

- Python 3.8+
- SuperCollider instalado (`sclang` debe estar en tu PATH)
- PlantUML (opcional, para generar imágenes desde archivos `.puml`)

## ⚙️ Instalación

Clona el repositorio:

```bash
git clone https://github.com/tuusuario/supercollider-uml-extractor.git
cd supercollider-uml-extractor
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🧪 Uso

Genera un archivo `.puml` con la jerarquía de subclases de una clase dada:

```bash
python sclang_hierarchy.py NodeProxy
```

Esto generará el archivo `NodeProxy_sclang_hierarchy.puml`.

Puedes convertirlo a una imagen PNG con PlantUML:

```bash
plantuml NodeProxy_sclang_hierarchy.puml
```

## 📄 Licencia

MIT
