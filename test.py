from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class StudentsTest(APITestCase):
    fixtures = ['students.json']

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username='diyorbek',
            password='15',
            is_superuser=True
        )
        token = AccessToken.for_user(user)
        cls.access_token = f"Bearer {str(token)}"

    def test_student_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)

        expecting_data = [
            {
                "id": 1,
                "fullname": "string",
                "student_student_type": "bachelors",
                "institute": 1,
                "contract_amount": 11000000.0,

            },
        ]
        url = reverse('students-list')
        response = self.client.get(path=url)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 1,
            "created_at": "1013-10-06T18:11:11.163151Z",
            "updated_at": "1013-10-06T18:11:11.163111Z",
            "full_name": "string",
            "student_type": "bachelor",
            "contract_amount": 110,
            "institute": 1
        }
        url = reverse('students-detail', kwargs={'pk': 1})
        response = self.client.get(path=url)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 4,
            "created_at": "1013-10-06T18:59:35.146099Z",
            "updated_at": "1013-10-06T18:59:35.146150Z",
            "full_name": "string",
            "student_type": "master",
            "contract_amount": 300,
            "institute": 1,

        }
        data = {
            "full_name": "string",
            "student_type": "master",
            "contract_amount": 300,
            "institute": 1
        }
        url = reverse('students-list')
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_partial_update(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 1,
            "created_at": "1013-10-06T18:11:11.163151Z",
            "updated_at": "1013-10-07T06:17:03.810741Z",
            "full_name": "string",
            "student_type": "bachelor",
            "contract_amount": 110,
            "institute": 1,

        }
        url = reverse('students-detail', kwargs={'pk': 1})
        response = self.client.patch(path=url)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_update(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 1,
            "created_at": "1013-10-06T18:11:11.163151Z",
            "updated_at": "1013-10-07T06:49:11.554478Z",
            "full_name": "string",
            "student_type": "bachelor",
            "contract_amount": 100,
            "institute": 1,

        }
        data = {
            "full_name": "string",
            "student_type": "bachelor",
            "contract_amount": 100,
            "institute": 1
        }
        url = reverse('students-detail', kwargs={'pk': 1})
        response = self.client.put(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expecting_data)

    def test_student_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        url = reverse('students-detail', kwargs={'pk': 1})
        response = self.client.delete(path=url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class StudentSponsorTest(APITestCase):
    fixtures = ['studentsponsor1.json']

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(
            username='string',
            password='1',
            is_superuser=True
        )
        token = AccessToken.for_user(user)
        cls.access_token = f"Bearer {str(token)}"

    def test_student_sponsor_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 3,
            "allocated_amount": 100,
            "created_at": "1013-10-07T08:59:37.391058Z",
            "student": 1,
        }
        data = {
            "allocated_amount": 100,
            "student": 1,
        }
        url = reverse('students_sponsors-list')
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


