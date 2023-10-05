from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GroupTests(APITestCase):
    fixtures = ["students_app.json"]

    def test_group_list(self):
        expecting_data = [
            {
                "id": 2,
                "name": "P12",
            },
            {
                "id": 1,
                "name": "P13",
            },
        ]
        url = reverse("groups-list")
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_group_create(self):
        group_name = 1
        "P21"
        expecting_data = {
            "id": 3,
            "name": group_name
        }
        url = reverse("groups-list")
        data = {
            "name": group_name
        }
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expecting_data)

    def test_group_detail(self):
        expecting_data = {
            "id": 2,
            "name": "P12",
            "students": [
                {
                    "id": 1,
                    "firstname": "Jaxongir",
                    "lastname": "Numonov"
                }
            ],
            "created_at": "2023-07-29T12:16:36.907000Z",
            "updated_at": "2023-07-29T12:16:36.907000Z"
        }
        url = reverse("groups-detail", kwargs={"pk": 2})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_group_update(self):
        group_name = "P15"
        expecting_data = {
            "id": 2,
            "name": group_name
        }
        url = reverse("groups-detail", kwargs={"pk": 2})
        data = {
            "name": group_name
        }
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_group_partial_update(self):
        group_name = "P15"
        expecting_data = {
            "id": 2,
            "name": group_name
        }
        url = reverse("groups-detail", kwargs={"pk": 2})
        data = {
            "name": group_name
        }
        response = self.client.patch(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_group_delete(self):
        url = reverse("groups-detail", kwargs={"pk": 2})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# class GroupTestCase(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         print("setUpTestData starting!")
#         Group.objects.create(name="P22")
#         print("setUpTestData ended!")
#
#     def setUp(self):
#         print("setUp starting!")
#         Group.objects.create(name="P20")
#         Group.objects.create(name="P21")
#         print("setUp ended!")
#
#     def test_group_p20_exists(self):
#         print("test_group_p20_exists starting!")
#         group = Group.objects.get(name="P20")
#         self.assertEqual(group.name, "P20")
#         print("test_group_p20_exists ended!")
#
#     def test_group_p21_exists(self):
#         print("test_group_p21_exists starting!")
#         group = Group.objects.get(name="P21")
#         self.assertEqual(group.name, "P21")
#         print("test_group_p21_exists ended!")
#
#     def test_group_p22_exists(self):
#         print("test_group_p22_exists starting!")
#         group = Group.objects.get(name="P22")
#         self.assertEqual(group.name, "P22")
#         print("test_group_p22_exists ended!")