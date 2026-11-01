#!/usr/bin/env python3
"""Generate DOCX copies of GPTZero training TXT samples without modifying their wording."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import argparse
from docx import Document
from docx.shared import Inches, Pt, RGBColor

def main(source_dir: Path):
    txt_files = sorted(source_dir.glob("[0-9][0-9]-ai-*.txt"))
    if len(txt_files) != 10:
        raise RuntimeError(f"Expected 10 text samples, found {len(txt_files)}")
    word_dir = source_dir / "word"
    word_dir.mkdir(exist_ok=True)
    outputs = []
    for src in txt_files:
        text = src.read_text(encoding="utf-8").strip().replace("\r\n", "\n")
        paras = [p.strip() for p in text.split("\n\n") if p.strip()]
        doc = Document()
        section = doc.sections[0]
        section.page_width, section.page_height = Inches(8.5), Inches(11)
        section.top_margin, section.bottom_margin = Inches(0.85), Inches(0.85)
        section.left_margin, section.right_margin = Inches(1), Inches(1)
        normal = doc.styles["Normal"]
        normal.font.name = "Aptos"
        normal.font.size = Pt(11)
        normal.font.color.rgb = RGBColor(36,46,61)
        normal.paragraph_format.space_after = Pt(9)
        normal.paragraph_format.line_spacing = 1.22
        for part in paras:
            p = doc.add_paragraph(part)
            p.paragraph_format.widow_control = True
        dest = word_dir / (src.stem + ".docx")
        doc.save(dest)
        check = Document(dest)
        if "\n\n".join(p.text for p in check.paragraphs) != "\n\n".join(paras):
            raise RuntimeError(f"Content mismatch: {dest}")
        outputs.append(dest)
    archive = source_dir / "gptzero-testovacie-texty-word.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED) as z:
        for path in outputs:
            z.write(path, path.name)
    print(f"Created {len(outputs)} verified DOCX files and {archive}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-dir", default="data/gptzero-testovacie-texty")
    args = ap.parse_args()
    main(Path(args.source_dir))
