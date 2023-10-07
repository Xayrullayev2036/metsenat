from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken


class StudentsTest(APITestCase):
    # access_token = None
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
                "student_type": "bachelors",
                "institute": 1,
                "contract_amount": 12000000.0,

            },
        ]
        url = reverse('students-list')
        response = self.client.get(path=url)
        self.assertEqual(response.data, expecting_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_student_detail(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
#         expecting_data = {
#             "id": 1,
#             "sponsors": [],
#             "created_at": "2023-10-06T18:12:11.263151Z",
#             "updated_at": "2023-10-06T18:12:11.263222Z",
#             "full_name": "string",
#             "phone_number": "333304711",
#             "type": "bachelor",
#             "contract_amount": 120,
#             "institute": 1
#         }
#         url = reverse('students-detail', kwargs={'pk': 1})
#         response = self.client.get(path=url)
#         # self.assertEqual(response.data, expecting_data) todo created_at & updated_at !=
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_student_create(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
#         expecting_data = {
#             "id": 4,
#             "created_at": "2023-10-06T18:59:35.146099Z",
#             "updated_at": "2023-10-06T18:59:35.146250Z",
#             "full_name": "Shavkat",
#             "phone_number": "990283723",
#             "type": "master",
#             "contract_amount": 300,
#             "institute": 1,
#             "sponsors": []
#         }
#         data = {
#             "full_name": "string",
#             "phone_number": "888328372",
#             "type": "master",
#             "contract_amount": 300,
#             "institute": 1
#         }
#         url = reverse('students-list')
#         response = self.client.post(path=url, data=data)
#         # self.assertEqual(response.data, expecting_data) todo created_at & updated_at !=
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_student_partial_update(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
#         expecting_data = {
#             "id": 1,
#             "created_at": "2023-10-06T18:12:11.263151Z",
#             "updated_at": "2023-10-07T06:27:03.810741Z",
#             "full_name": "string",
#             "phone_number": "333304777",
#             "type": "bachelor",
#             "contract_amount": 120,
#             "institute": 1,
#             "sponsors": []
#         }
#         data = {'phone_number': '777777777'}
#         url = reverse('students-detail', kwargs={'pk': 1})
#         response = self.client.patch(path=url, data=data)
#         # self.assertEqual(response.data, expecting_data) todo created_at & updated_at !=
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_student_update(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
#         expecting_data = {
#             "id": 1,
#             "created_at": "2023-10-06T18:12:11.263151Z",
#             "updated_at": "2023-10-07T06:49:12.554478Z",
#             "full_name": "string",
#             "phone_number": "333304711",
#             "type": "bachelor",
#             "contract_amount": 100,
#             "institute": 1,
#             "sponsors": []
#         }
#         data = {
#             "full_name": "string",
#             "phone_number": "333304711",
#             "type": "bachelor",
#             "contract_amount": 100,
#             "institute": 1
#         }
#         url = reverse('students-detail', kwargs={'pk': 1})
#         response = self.client.put(path=url, data=data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # self.assertEqual(response.data, expecting_data) todo created_at & updated_at !=
#
#     def test_student_delete(self):
#         self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
#         url = reverse('students-detail', kwargs={'pk': 2})
#         response = self.client.delete(path=url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# class StudentSponsorTest(APITestCase):
#     fixtures = ['studentsponsor2.json']
#
#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.create(
#             username='zokir',
#             password='1',
#             is_superuser=True
#         )
#         token = AccessToken.for_user(user)
#         cls.access_token = f"Bearer {str(token)}"

    def test_student_sponsor_create(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.access_token)
        expecting_data = {
            "id": 3,
            "allocated_amount": 100,
            "created_at": "2023-10-07T08:59:37.391058Z",
            "student": 2,
            "sponsor": 2
        }
        data = {
            "allocated_amount": 100,
            "student": 2,
            "sponsor": 2
        }
        url = reverse('students_sponsors-list')
        response = self.client.post(path=url, data=data)
        # self.assertEqual(response.data, expecting_data)  todo created_at & updated_at !=
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


