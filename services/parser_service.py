import re
from typing import Dict, List, Optional


def parse_receipt_text(text: str) -> Dict:
    """
    Input: raw OCR text from receipt.
    Output: structured dict with merchant, date, items, total, currency, tax.
    """
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]

    #1. ==MERCHANT AND DATE==
    merchant = "Unknown Merchant"
    date = None

    for line in lines:
        date_match = re.search(r"\b(\d{2}\.?\s*\d{2}\.?\s*\d{4})\b", line)
        if date_match:
            raw_date = re.sub(r"\s+", "", date_match.group(1))
            date = raw_date.replace(".", "/")
        if merchant == "Unknown Merchant" and not date_match:
            if len(line) > 5 and "|" not in line:
                merchant = line

    #2. ==LINE ITEMS==
    items: List[Dict] = []
    item_pattern = re.compile(
        r"^(?:\d+x|[eI]x)?\s*(.+?)\s+(\d+\.?\d+)\s+([A-Z]{3})\s+(\d+\.?\d+)$"
    )

    for line in lines:
        match =  item_pattern.search(line)
        if match:
            name = match.group(1).strip()
            price = float(match.group(4))
            items.append({"name": name, "price": price})

    #3. == TOTAL, TAX, CURRENCY ==

    total = 0.0
    tax = None
    currency = "CHF"

    for i, line in enumerate(lines):
        total_match = re.search(r"MwSt\s+([\d.]+)\s+CHF", line)
        if total_match:
            total = float(total_match.group(1))

        tax_match = re.search(r"CHF[:\s]+([\d.]+)\s*$", line)
        if tax_match:
            tax = float(tax_match.group(1))

    return {
        "merchant": merchant,
        "date": date,
        "items": items,
        "total": total,
        "currency": currency,
        "tax": tax,
    }

