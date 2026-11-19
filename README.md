# 📋 Weryfikator statusu płatnika VAT

Prosty skrypt w Pythonie służący do sprawdzania aktualnego (na podaną datę) statusu płatnika VAT dla danego numeru NIP, korzystając z oficjalnego API Ministerstwa Finansów RP.

## ✨ Co robi ten program?
- Pobiera informacje o płatnikach VAT za pomocą biblioteki `requests` do endpointa: 
 `https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={date}`
- Analizuje odpowiedź JSON i wyświetla komunikat, czy podany NIP jest **czynnym płatnikiem VAT** na dzień wskazanej daty.

## 🚀 Jak działa?
1. Użytkownik dostarcza numer NIP (np. `8042563719`) oraz datę w formacie `RRRR-MM-DD` (np. `2024-01-15`).
2. Skrypt wysyła zapytanie do API MF i parsuje wynik.
3. Jeśli odpowiedź zawiera podmiot o statusie „Czynny” – wyświetla potwierdzenie, w przeciwnym razie informację o braku czynności lub błędzie.

## 📦 Wymagania
- Python 3.x
- Biblioteka `requests` (`pip install requests`)

## 💻 Przykład użycia
python

Skrypt do uruchomienia bezpośrednio:
nip = input('Podaj numer NIP do sprawdzenia: ')
date = input('Podaj datę w formacie RRRR-MM-DD: ')
sprawdz_status_vat(nip, date)

Wpisz np. 8042563719 i 2024-01-01
## 📊 Przykładowy output
Numer NIP 8042563719 jest czynnym płatnikiem VAT na dzień 2024-01-01.

lub
Numer NIP 8042563719 nie jest czynnym płatnikiem VAT na dzień 2024-01-01.

## 🛠️ Możliwości rozbudowy (w planie)
- Obsługa wszystkich podmiotów o tym samym NIP,
- Pełna walidacja formatu NIP i daty,
- Wyższa odporność na błędy parsowania JSON oraz Rate Limit,
- Integracja z bazą danych lub wywoływaniem w procesach automatycznych (cron, systemd).

## 🔧 Uwagi techniczne
- Skrypt nie przechowuje żadnych danych – korzysta wyłącznie z publicznie dostępnego API MF.
- Zalecane jest używanie `requests.Session` dla lepszej wydajności przy wielokrotnych połączeniach.
- W przypadku błędów sieciowych lub niepoprawnych odpowiedzi API – program wyświetla komunikat o problemie.
