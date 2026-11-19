import requests
import re
from datetime import datetime
import time


def waliduj_nip(nip):
    return bool(re.fullmatch(r'\d{10}', nip))


def waliduj_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def sprawdz_status_vat(nip, date):
    if not waliduj_nip(nip) or not waliduj_date(date):
        print("Wymagane poprawne dane. NIP musi mieć 10 cyfr, data format RRRR-MM-DD.")
        return

    url = f'https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={date}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        with requests.Session() as session:
            response = session.get(url, headers=headers)
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Wystąpił błąd: {e}")
        return

    if 'result' not in data or not isinstance(data['result'], list):
        print("Niepoprawna struktura odpowiedzi API.")
        return

    for entry in data['result']:
        subject = entry.get('subject', {})
        status = subject.get('statusVat')
        nip_val = entry.get('nip')
        if status == 'Czynny':
            print(f"NIP {nip_val} jest czynnym płatnikiem VAT na dzień {date}.")
        else:
            print(f"NIP {nip_val} nie jest czynnym płatnikiem VAT na dzień {date}.")


if __name__ == "__main__":
    nip = input('Podaj numer NIP do sprawdzenia: ')
    date = input('Podaj datę w formacie RRRR-MM-DD: ')
    sprawdz_status_vat(nip, date)
