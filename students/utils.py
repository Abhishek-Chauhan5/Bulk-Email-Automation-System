from openpyxl import Workbook
import os
from django.conf import settings
from datetime import datetime


def create_remark_file(remarks):

    folder = os.path.join(
        settings.MEDIA_ROOT,
        "remarks"
    )


    os.makedirs(
        folder,
        exist_ok=True
    )


    filename = (
        f"upload_remark_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    )


    path = os.path.join(
        folder,
        filename
    )


    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Remark"



    sheet.append([

        "Name",
        "Age",
        "Email",
        "Remark"

    ])



    for item in remarks:

        sheet.append([

            item["name"],
            item["age"],
            item["email"],
            item["remark"]

        ])



    workbook.save(path)


    return path