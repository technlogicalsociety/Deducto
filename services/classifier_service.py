from typing import Dict, List


#1/ ===TAX DEDUCTABLE KEYWORDS==
# Each line item gets checked against a list of keywords
#if the item name contains keyword -->  flag it True
#if not flag  it false
#


# Keywords of tax deductable line items


TAX_DEDUCTIBLE_KEYWORDS = [
    # Technology & Software
    "software",
    "subscription",
    "saas",
    "license",
    "antivirus",
    "cloud",
    "hosting",
    "domain",
    "app",
    "plugin",
    "api",

    # Office & Supplies
    "office",
    "supplies",
    "stationery",
    "printer",
    "ink",
    "toner",
    "paper",
    "desk",
    "chair",
    "furniture",
    "filing",
    "shredder",
    "whiteboard",

    # Hardware & Equipment
    "hardware",
    "equipment",
    "computer",
    "laptop",
    "monitor",
    "keyboard",
    "mouse",
    "headset",
    "webcam",
    "microphone",
    "camera",
    "scanner",
    "projector",
    "server",
    "router",
    "cable",
    "battery",
    "charger",
    "hard drive",
    "usb",
    "storage",

    # Communication
    "phone",
    "mobile",
    "internet",
    "broadband",
    "telecom",
    "postage",
    "courier",
    "delivery",
    "shipping",
    "fax",

    # Travel & Transport
    "travel",
    "transport",
    "fuel",
    "petrol",
    "diesel",
    "parking",
    "toll",
    "taxi",
    "uber",
    "lyft",
    "train",
    "flight",
    "airline",
    "airport",
    "bus",
    "ferry",
    "car hire",
    "car rental",
    "vehicle",
    "mileage",

    # Accommodation
    "accommodation",
    "hotel",
    "motel",
    "airbnb",
    "lodging",
    "hostel",
    "inn",

    # Meals & Entertainment (business)
    "business meal",
    "client dinner",
    "client lunch",
    "conference meal",
    "working lunch",

    # Professional Services
    "consulting",
    "consultant",
    "accountant",
    "accounting",
    "legal",
    "lawyer",
    "solicitor",
    "audit",
    "bookkeeping",
    "payroll",
    "recruitment",
    "contractor",
    "freelance",

    # Marketing & Advertising
    "advertising",
    "marketing",
    "promotion",
    "campaign",
    "branding",
    "design",
    "photography",
    "videography",
    "printing",
    "signage",
    "banner",
    "flyer",

    # Education & Training
    "training",
    "course",
    "workshop",
    "seminar",
    "conference",
    "webinar",
    "certification",
    "books",
    "textbook",
    "journal",
    "magazine",
    "newsletter",
    "membership",

    # Finance & Insurance
    "insurance",
    "premium",
    "bank fee",
    "transaction fee",
    "interest",
    "loan fee",
    "accounting fee",

    # Utilities (business portion)
    "electricity",
    "gas",
    "water",
    "utility",
    "rent",
    "lease",
    "maintenance",
    "repair",
    "cleaning",
    "security",

    # Health & Safety (work related)
    "safety",
    "protective",
    "uniform",
    "workwear",
    "first aid",

    # Miscellaneous Business
    "subscription",
    "annual fee",
    "service fee",
    "processing fee",
    "platform fee",
    "tool",
    "tools",
]



def classify_items(receipt: Dict) ->  Dict:
    """

    Input: parsed receipt dict.
    Output: same dict with tax_deductible flag added to each item.
    """

    flagged_items = []

    for item in receipt["items"]:
        name_lower = item["name"].lower()
        is_deductible = any(
            keyword in name_lower
            for keyword in TAX_DEDUCTIBLE_KEYWORDS
        )
        flagged_items.append({
            **item,
            "tax_deductible": is_deductible
        })

    return {
        **receipt,
         "items": flagged_items
    }
