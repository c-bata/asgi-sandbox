from django.test import TestCase


class TopPageViewTest(TestCase):
    async def test_top_returns_200(self):
        response = await self.async_client.get('/')
        self.assertEqual(response.status_code, 200)

    async def test_top_returns_expected_content(self):
        response = await self.async_client.get('/')
        self.assertEqual(response.content, b"Hello, async world!")
