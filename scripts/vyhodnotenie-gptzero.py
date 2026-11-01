#!/usr/bin/env python3
"""Lokalne vyhodnotenie rucne zaznamenanych GPTZero klasifikacii (bez API)."""

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

ALLOWED = {"human", "ai", "mixed", "uncertain"}
GROUND_TRUTH = {"human", "ai", "mixed"}


def read_rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        expected = {"id", "skutocny_povod", "predikcia"}
        if not reader.fieldnames or not expected.issubset(reader.fieldnames):
            raise ValueError("CSV musi mat stlpce: id, skutocny_povod, predikcia")
        return list(reader)


def main():
    parser = argparse.ArgumentParser(
        description="Porovnaj znamy povod textu s manualnymi vysledkami GPTZero."
    )
    parser.add_argument(
        "--input", default="data/vysledky-vzor.csv", help="Vstupny CSV subor."
    )
    args = parser.parse_args()

    try:
        rows = read_rows(Path(args.input))
    except (OSError, ValueError) as exc:
        print(f"Chyba: {exc}", file=sys.stderr)
        return 2

    finished = []
    skipped = 0
    errors = []
    for number, row in enumerate(rows, start=2):
        actual = (row.get("skutocny_povod") or "").strip().casefold()
        predicted = (row.get("predikcia") or "").strip().casefold()
        if not predicted:
            skipped += 1
            continue
        if actual not in GROUND_TRUTH or predicted not in ALLOWED:
            errors.append((number, actual, predicted))
            continue
        finished.append(((row.get("id") or "").strip(), actual, predicted))

    print("GPTZero - vyhodnotenie rucne zaznamenanych vysledkov")
    print(f"Zaznamov v CSV: {len(rows)}")
    print(f"Bez predikcie: {skipped}")
    print(f"Platne vyhodnotenych: {len(finished)}")
    if errors:
        print("Neplatne riadky:")
        for number, actual, pred in errors:
            print(f"  {number}: povod={actual!r}, predikcia={pred!r}")
        return 2

    if not finished:
        print(
            "Zatial nemame realne vysledky. "
            "Najprv vyplnte stlpec predikcia po skenovani v GPTZero."
        )
        return 0

    matrix = Counter((actual, predicted) for _, actual, predicted in finished)
    correct = sum(1 for _, actual, pred in finished if actual == pred)
    print(f"Zhodna klasifikacia: {correct}/{len(finished)}")
    print(f"Pozorovana zhoda: {100.0 * correct / len(finished):.1f}%")
    print("Matica: skutocny povod -> vysledok")
    for actual in ("human", "ai", "mixed"):
        values = [matrix[(actual, pred)] for pred in ("human", "ai", "mixed", "uncertain")]
        print(f"  {actual:<6}: Human={values[0]} AI={values[1]} Mixed={values[2]} Uncertain={values[3]}")
    print(f"False positives (Human -> AI): {matrix[('human', 'ai')]}")
    print(f"False negatives (AI -> Human): {matrix[('ai', 'human')]}")
    print(
        "Poznamka: Mixed a Uncertain evidujeme osobitne. "
        "Zhoda na malej vzorke nie je zovseobecnitelna presnost detektora."
    )
    print("Skript nedeteguje AI a nikam neposiela text.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
