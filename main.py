import requests


def sprawdz_status_vat(nip, date):
    url = f'https://wl-api.mf.gov.pl/api/search/nip/{nip}?date={date}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200 and 'result' in data:
            if data['result']['subject']['statusVat'] == 'Czynny':
                print(f'Numer NIP {nip} jest czynnym płatnikiem VAT na dzień {date}.')
            else:
                print(f'Numer NIP {nip} nie jest czynnym płatnikiem VAT na dzień {date}.')
        elif response.status_code == 204:
            print(f'Brak danych dla numeru NIP {nip} na dzień {date}.')
        else:
            print('Wystąpił problem podczas pobierania danych.')
    except requests.exceptions.RequestException as e:
        print('Wystąpił problem podczas nawiązywania połączenia.')
        print(e)


# Przykładowe użycie
nip = input('Podaj numer NIP do sprawdzenia: ')
date = input('Podaj datę w formacie RRRR-MM-DD: ')
sprawdz_status_vat(nip, date)