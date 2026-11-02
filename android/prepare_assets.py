from pathlib import Path

from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ICON = (
    PROJECT_ROOT
    / "assets"
    / "branding"
    / "KeyMintIcon.png"
)
OUTPUT_DIR = Path(__file__).resolve().parent / "assets"
OUTPUT_ICON = OUTPUT_DIR / "KeyMintIcon.png"


def main():
    if not SOURCE_ICON.exists():
        raise FileNotFoundError(
            f"No se encontró el icono fuente: {SOURCE_ICON}"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with Image.open(SOURCE_ICON) as image:
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
            OUTPUT_ICON,
            format="PNG",
            optimize=True,
        )

    print(
        f"Icono Android preparado: {OUTPUT_ICON}"
    )


if __name__ == "__main__":
    main()
