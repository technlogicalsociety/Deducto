from services.ingest_service import extract_text_from_image

text = extract_text_from_image("test_receipt.jpg")
print(text)
