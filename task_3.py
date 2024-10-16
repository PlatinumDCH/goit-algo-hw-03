import re


def normalize_phone(phone_number: str) -> str:
    normalized = re.sub(r"[^0-9+]", "", phone_number).strip()
    if normalized.startswith("0"):
        normalized = "+38" + normalized
    elif normalized.startswith("380"):
        normalized = "+" + normalized
    elif normalized.isdigit():
        normalized = "+" + normalized
    if len(normalized) != 13:
        normalized = "error number format"
    return normalized
