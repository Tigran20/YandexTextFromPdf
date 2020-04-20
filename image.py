import base64
import json
import os
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter


def encode_file(file):
    with open(file, 'rb') as f:
        file_content = f.read()
    return base64.b64encode(file_content).decode('utf-8')

outfile = encode_file('text2.pdf')


out = {
    "folderId": "b1gah3b0s98i5term047",
    "analyze_specs": [{
        "content": outfile,
        "mime_type": "application/pdf",
        "features": [{
            "type": "TEXT_DETECTION",
            "text_detection_config": {
                "language_codes": ["*"]
            }
        }]
    }],
}

with open('body.json', 'w') as f:
    json.dump(out, f)


# REAL IAM_TOKEN is REQUARED
os.system(
    "export IAM_TOKEN=CggVAgAAABoBMxKABBwFP5GNXSziBbBs_XKNqWix2sAqqxx9J19WYoJhVgaHXP_bQxBB3CJ95SLwJSz-BYYELXX8c5WdGiOw5LR4q_Ug4x2BBhiOinYkM0chyEFoVMy6xNFLSKTkPJI3vzL_6Ze_M42aiSaem_iq6mqsjJrd6HzCO4Yn5FWCplSGG2O_lUV9OjT-AZM1H4uy1LXyoaFdRKLaPq8sO5alnMP33Xh9j-w1nGQmSikvxiGI6qFiIPpIZ4q5SldheBSDU8O65UEraRLsNbgaY9NgDCUkI5oZ05N2pZkmOCXlnTmCyFQKuntUCUza-AMyqBLJztRO0efgeTxXG2hYHCdauU7VX-4ac1Q2kjXiKkyN7l3A3BDvPWxyN8mBSQhaEWQri34Wre6vpNKw8MiFHz-excrukZdm4ET2Qzb-BM02JXA2RY_65Kp2EFc2wiXD_hYosuwcrlkUm_jwhlxYmFeL8PE9dTAOhV_fxnnIPVX5AIvtUWMiusscpe5f3weRikzSVbTU3OUuVJF9lU3OkrGHafHR_sUHR0fs3lgy4Dl5EWmlKJN_FEINmo6467SYmJCBRWzDLwp0H8E2EJq2hAiT8buYL2OZV07ZDlN-V-cwbWl2rFmoxtdO7_HPQzG8Vxw-nM6mo-tOnayB9S0cKrbSgdwMtan9MLxqxE9NUrXS3BYx3cCoGiQQsYX39AUY8db59AUiFgoUYWplbWl0MG1wMjZybzNsZDh2a2s=")
os.system(
    "curl -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer CggVAgAAABoBMxKABBwFP5GNXSziBbBs_XKNqWix2sAqqxx9J19WYoJhVgaHXP_bQxBB3CJ95SLwJSz-BYYELXX8c5WdGiOw5LR4q_Ug4x2BBhiOinYkM0chyEFoVMy6xNFLSKTkPJI3vzL_6Ze_M42aiSaem_iq6mqsjJrd6HzCO4Yn5FWCplSGG2O_lUV9OjT-AZM1H4uy1LXyoaFdRKLaPq8sO5alnMP33Xh9j-w1nGQmSikvxiGI6qFiIPpIZ4q5SldheBSDU8O65UEraRLsNbgaY9NgDCUkI5oZ05N2pZkmOCXlnTmCyFQKuntUCUza-AMyqBLJztRO0efgeTxXG2hYHCdauU7VX-4ac1Q2kjXiKkyN7l3A3BDvPWxyN8mBSQhaEWQri34Wre6vpNKw8MiFHz-excrukZdm4ET2Qzb-BM02JXA2RY_65Kp2EFc2wiXD_hYosuwcrlkUm_jwhlxYmFeL8PE9dTAOhV_fxnnIPVX5AIvtUWMiusscpe5f3weRikzSVbTU3OUuVJF9lU3OkrGHafHR_sUHR0fs3lgy4Dl5EWmlKJN_FEINmo6467SYmJCBRWzDLwp0H8E2EJq2hAiT8buYL2OZV07ZDlN-V-cwbWl2rFmoxtdO7_HPQzG8Vxw-nM6mo-tOnayB9S0cKrbSgdwMtan9MLxqxE9NUrXS3BYx3cCoGiQQsYX39AUY8db59AUiFgoUYWplbWl0MG1wMjZybzNsZDh2a2s=\" -d @body.json https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze > output.json")

# YandexVisions answer in output.json
