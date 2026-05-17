from services.ingest_service import extract_text_from_image
from services.parser_service import parse_receipt_text

text = extract_text_from_image("test_receipt.jpg")
result = parse_receipt_text(text)
print(result)
