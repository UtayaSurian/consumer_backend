import csv
import logging
import os
from typing import Dict, List


def check_prob(post_data):
    for item in post_data["data"]["preds"]:
        try:
            if float(item["prob"]) < 0.25:
                item["tags"].append("low_prob")
        except KeyError:
            continue


def check_existing_headers(headers):
    file_exists = os.path.isfile("data.csv")
    if file_exists:
        with open("data.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            headers_row = next(reader, [])
            headers_exist = headers_row == headers
            if not headers_exist:
                with open("data.csv", "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(headers)
    else:
        with open("data.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)


def write_row_data(row_data):
    with open("data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for prediction in row_data["data"]["preds"]:
            # Create a row of data for the CSV file
            row = [
                row_data.get("device_id", "NA"),
                row_data.get("client_id", "NA"),
                row_data.get("created_at", "NA"),
                row_data["data"].get("license_id", "NA"),
                prediction.get("image_frame", "NA"),
                float(prediction.get("prob", 0)),
                prediction.get("tags", []),
            ]
            # Write the row to the CSV file
            writer.writerow(row)


def data_validation(data, headers):
    if isinstance(data, dict):
        return len(data.keys()) == 4
    else:
        return False


def write_to_csv(post_request):
    headers = [
        "device_id",
        "client_id",
        "created_at",
        "license_id",
        "image_frame",
        "prob",
        "tags",
    ]

    if not data_validation(post_request, headers):
        logging.info(" [-] Invalid Data!, Please try again")
        return False
    check_existing_headers(headers)
    check_prob(post_request)
    write_row_data(post_request)
