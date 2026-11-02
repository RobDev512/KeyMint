from pathlib import Path
from shutil import copy2

from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ANDROID_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = ANDROID_DIR / "assets"

SOURCE_APP_ICON = (
    PROJECT_ROOT
    / "assets"
    / "branding"
    / "KeyMintIcon.png"
)

ICON_FILES = [
    (
        PROJECT_ROOT / "assets" / "icons" / "theme" / "IconoClaro.png",
        OUTPUT_DIR / "icons" / "theme" / "IconoClaro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "theme" / "IconoOscuro.png",
        OUTPUT_DIR / "icons" / "theme" / "IconoOscuro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "visibility" / "VerAbierto_Claro.png",
        OUTPUT_DIR / "icons" / "visibility" / "VerAbierto_Claro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "visibility" / "VerAbierto_Oscuro.png",
        OUTPUT_DIR / "icons" / "visibility" / "VerAbierto_Oscuro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "visibility" / "VerCerrado_Claro.png",
        OUTPUT_DIR / "icons" / "visibility" / "VerCerrado_Claro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "visibility" / "VerCerrado_Oscuro.png",
        OUTPUT_DIR / "icons" / "visibility" / "VerCerrado_Oscuro.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "ui" / "Claro" / "Copiar.png",
        OUTPUT_DIR / "icons" / "ui" / "Claro" / "Copiar.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "ui" / "Oscuro" / "Copiar.png",
        OUTPUT_DIR / "icons" / "ui" / "Oscuro" / "Copiar.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "ui" / "Claro" / "Cerrar.png",
        OUTPUT_DIR / "icons" / "ui" / "Claro" / "Cerrar.png",
    ),
    (
        PROJECT_ROOT / "assets" / "icons" / "ui" / "Oscuro" / "Cerrar.png",
        OUTPUT_DIR / "icons" / "ui" / "Oscuro" / "Cerrar.png",
    ),
]


def prepare_app_icon():
    if not SOURCE_APP_ICON.exists():
        raise FileNotFoundError(
            f"No se encontró el icono fuente: {SOURCE_APP_ICON}"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_icon = OUTPUT_DIR / "KeyMintIcon.png"

    with Image.open(SOURCE_APP_ICON) as image:
        image = image.convert("RGBA")
        image.thumbnail(
            (512, 512),
            Image.Resampling.LANCZOS,
        )

        canvas = Image.new(
            "RGBA",
            (512, 512),
            (0, 0, 0, 0),
        )

        x = (512 - image.width) // 2
        y = (512 - image.height) // 2

        canvas.alpha_composite(
            image,
            (x, y),
        )

        canvas.save(
            output_icon,
            format="PNG",
            optimize=True,
        )

    return output_icon


def copy_interface_icons():
    copied = []

    for source, destination in ICON_FILES:
        if not source.exists():
            raise FileNotFoundError(
                f"No se encontró el icono fuente: {source}"
            )

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        copy2(source, destination)
        copied.append(destination)

    return copied


def main():
    output_icon = prepare_app_icon()
    copied_icons = copy_interface_icons()

    print(
        f"Icono Android preparado: {output_icon}"
    )
    print(
        f"Iconos de interfaz preparados: {len(copied_icons)}"
    )


if __name__ == "__main__":
    main()
