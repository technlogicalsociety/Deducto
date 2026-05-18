from services.ingest_service import extract_text_from_image
from services.parser_service import parse_receipt_text
from services.classifier_service import classify_items

text = extract_text_from_image("test_receipt.jpg")
parsed = parse_receipt_text(text)
result = classify_items(parsed)

for item in result["items"]:
    print(item)



fake_receipt = {
    "merchant": "Test Store",
    "date": "01/01/2024",
    "items": [
        {"name": "Office Chair", "price": 299.00},
        {"name": "Laptop", "price": 1499.00},
        {"name": "Coffee", "price": 4.50},
    ],
    "total": 1802.50,
    "currency": "AUD",
    "tax": 180.25
}

flagged = classify_items(fake_receipt)
for item in flagged["items"]:
    print(item)
