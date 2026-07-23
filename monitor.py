import requests
from datetime import datetime

URL = "https://bilety.laczynaspilka.pl/pzpn"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    )
}

print(f"[{datetime.now()}] Rozpoczynam sprawdzanie strony PZPN...")
print(f"URL: {URL}")

try:
    response = requests.get(
        URL,
        headers=headers,
        timeout=30,
        allow_redirects=True
    )

    print(f"Status HTTP: {response.status_code}")
    print(f"Adres końcowy: {response.url}")
    print(f"Długość odpowiedzi: {len(response.text)} znaków")

    if response.status_code == 200:
        print("OK: Strona została pobrana poprawnie.")

        if "kup bilet" in response.text.lower():
            print("INFO: Znaleziono tekst 'Kup bilet'.")
        else:
            print("INFO: Nie znaleziono tekstu 'Kup bilet'.")

    elif response.status_code == 403:
        print("BŁĄD: Serwer PZPN odrzucił żądanie (403 Forbidden).")

    else:
        print(f"BŁĄD: Serwer zwrócił kod HTTP {response.status_code}.")

except requests.RequestException as e:
    print(f"BŁĄD POŁĄCZENIA: {e}")
