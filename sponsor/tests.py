from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class SponsorTests(APITestCase):
    fixtures = ["sponsor.json"]

    def test_sponsor_list(self):
        expecting_data = [
            {
                "id": 1,
                "fullname": "string",
                "phone_number": "+998940362036",
                "payment_amount": "-6960.00",
                "created_at": "2023-09-28",
                "status": "",
            },
            {
                "id": 2,
                "fullname": "Diyorbek",
                "phone_number": "string",
                "payment_amount": "-8951901.99",
                "created_at": "2023-09-28",
                "status": "yangi",

            }
        ]
        url = reverse("sponsor-list")
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_sponsor_create(self):
        sponsor_name = "Ali"
        expecting_data = {
            "id": 3,
            "fullname": sponsor_name,
            "payment_type": "naqd",
        }
        url = reverse("sponsor-list")
        data = {
            "fullname": sponsor_name,
            "payment_type": "naqd",
        }
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expecting_data)

    def test_sponsor_detail(self):
        expecting_data = {
            "id" : 1,
            "fullname" : "string",
            "phone_number" : '+998940362036',
            "payment_amount": "-6960.00",
            "company_name": "Pdp",
            "status": "",
            "created_at":"2023-09-28"
        }
        url = reverse("sponsor-detail", kwargs={"pk": 1})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)


    def test_sponsor_update(self):
        sponsor_name = "Diyorbek"
        expecting_data = {
            "id": 1,
            "fullname": sponsor_name,
            "payment_type": "karta"
        }
        url = reverse("sponsor-detail", kwargs={"pk": 1})
        data = {
            "fullname": sponsor_name,
            "payment_type": "karta"

        }
        response = self.client.put(path=url, data=data)
        print(response.data)
        print(expecting_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    # def test_sponsor_partial_update(self):
    #     sponsor_name = "Diyorbek"
    #     expecting_data = {
    #         "id": 1,
    #         "fullname": sponsor_name
    #     }
    #     url = reverse("sponsor-detail", kwargs={"pk": 1})
    #     data = {
    #         "fullname": sponsor_name
    #     }
    #     response = self.client.patch(path=url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, expecting_data)

    # def test_sponsor_delete(self):
    #     url = reverse("sponsors-detail", kwargs={"pk": 2})
    #     response = self.client.delete(path=url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
