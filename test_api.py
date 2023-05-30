import unittest
from app import app


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_random_array_endpoint(self):
        input_sentence = "This is an example sentence"
        expected_length = 500

        # Send a POST request to the random_array endpoint
        response = self.client.post("/random_array",
                                    data={"sentence": input_sentence})

        # Check the response status code
        self.assertEqual(response.status_code, 200)

    def test_random_array_endpoint_result(self):
        # Send a POST request to the random_array endpoint
        response = self.client.post(
            "/random_array",
            data={"sentence": "This is an example sentence"}
        )

        # Check that the response contains a 'result' field
        self.assertIn("result", response.json)

    def test_random_array_length(self):
        # Send a POST request to the random_array endpoint
        response = self.client.post(
            "/random_array",
            data={"sentence": "This is an example sentence"}
        )

        # Check that the length of the returned array is 500
        random_array = response.json["result"]
        self.assertEqual(len(random_array), 500)

    def test_random_array_element_type(self):
        # Send a POST request to the random_array endpoint
        response = self.client.post(
            "/random_array",
            data={"sentence": "This is an example sentence"}
        )

        # Check that each element in the array is a float
        random_array = response.json["result"]
        for element in random_array:
            self.assertIsInstance(element, float)

    def test_sentence_type_integer(self):
        # Send a POST request to the random_array endpoint with sentence as integer 1
        data = {"sentence": 1}
        response = self.client.post("/random_array", data=data)
        self.assertEqual(response.status_code, 400)

    def test_sentence_is_word(self):
        # Send a POST request to the random_array endpoint with sentence as single word
        data = {"sentence": "Word"}
        response = self.client.post("/random_array", data=data)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
