import os
import csv
import requests
import time
import ast

from dotenv import load_dotenv

load_dotenv()

api_url_dev = os.getenv("WEB_PAYMENT_SERVICE_DEV")
api_url_prod = os.getenv("WEB_PAYMENT_SERVICE_PROD")
plans = os.getenv("PLANS_WITH_TRIAL")


def form_request_body(row):
    subscription_duration = row['duration']
    amplitude_id_vat_suffix = '' if float(row['vat_rate']) == 1.0 else f"_vat_{int(float(row['vat_rate']))}"
    trial_duration = '' if row['trial_duration'] == 'NULL' else row['trial_duration']
    trial_price = '' if float(row['trial_price']) == 0 else format(float(row['trial_price']), ".2f")
    amplitude_id = f"{subscription_duration.replace(' ', '')}_{float(row['price']):.2f}$_with_trial_{trial_duration.replace(' ', '')}_{trial_price}${amplitude_id_vat_suffix}"
    #amplitude_id = row['amplitude_id']
    body = {
        "id": row["id"],
        "project": row['project'],
        "planId": None if row['plan_id'] == '' else row['plan_id'],
        "name": row['name'],
        "price": float(row['price']),
        "currency": row['currency'],
        "provider": row['provider'],
        "type": row['type'],
        "duration": subscription_duration,
        "amplitudeId": amplitude_id,
        "trialPrice": None if row['trial_price'] == '' else float(row['trial_price']),
        "priceVat": float(row['price_vat']),
        "trialPriceVat": None if row['trial_price_vat'] == '' else float(row['trial_price_vat']),
        "paymentPage": None if row['payment_page'] == '' else row['payment_page'],
        "isTest": row['is_test'] == "TRUE",
        "baseId": None if row['base_id'] == '' else row['base_id'],
        "abTestId": None if row['ab_test_id'] == '' else row['ab_test_id'],
        "trialDuration": None if row["trial_duration"] == '' else row["trial_duration"],
        "vatRate": row["vat_rate"],
        "paypalAccount": None if row['paypal_account'] == '' else row['paypal_account'],
        "countries": ast.literal_eval(row["country_codes"])
    }
    return body


def main():
    with open(plans) as f_read:
        with open('error_result.csv', 'w') as f_write:
            f_reader = csv.DictReader(f_read)
            writer = csv.writer(f_write)
            for row in f_reader:
                body = form_request_body(row)
                response = requests.post(api_url_dev, json=body)
                time.sleep(0.5)
                response1 = requests.post(api_url_prod, json=body)
                if "Unexpected error" in response.text:
                    writer.writerow(row.values())
                print(f"response: {response.text}")
                print(f"response: {response1.text}")
                time.sleep(0.5)


if __name__ == '__main__':
    main()