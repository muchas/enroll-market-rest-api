from .base import ResourceTestCase
from .factories import TermFactory, OfferFactory, StudentFactory


class TermResourceTest(ResourceTestCase):
    """
    Remember about checking offer with existing plan

    """
    pass


class TermListResourceTest(ResourceTestCase):
    def setUp(self):
        super(TermListResourceTest, self).setUp()
        self.url = '/api/terms'

    def test_empty_list(self):
        response = self.client.get(self.url)
        self.assert200(response)
        self.assertEquals(response.json, [])

    def test_list(self):
        terms = TermFactory.create_batch(3)
        self.session.commit()

        response = self.client.get(self.url)

        self.assert200(response)
        self.assertEquals(len(response.json), 3)
        self.assertSetEqual({x.id for x in terms}, {x['id'] for x in response.json})


class MyTermListResourceTest(ResourceTestCase):
    def setUp(self):
        super(MyTermListResourceTest, self).setUp()
        self.url = '/api/me/terms'

    def test_empty_list(self):
        response = self.client.get(self.url)
        self.assert200(response)
        self.assertEquals(response.json, {})

    def test_list(self):
        terms = TermFactory.create_batch(3)

        response = self.client.get(self.url)
        self.assert200(response)
        self.assertEquals(len(response.json), 3)


class OfferListResourceTest(ResourceTestCase):
    def setUp(self):
        super(OfferListResourceTest, self).setUp()
        self.url = '/api/offers'

    def test_empty_list(self):
        response = self.client.get(self.url)
        self.assert200(response)
        self.assertEquals(response.json, {})

    def test_list(self):
        offers = OfferFactory.create_batch(3)
        self.session.commit()

        response = self.client.get(self.url)
        self.assert200(response)
        self.assertEquals(len(response.json), 3)

    def test_valid_creation(self):
        student = StudentFactory()
        term = TermFactory()
        self.session.commit()

        response = self.client.post(self.url, data={
            'student_id': student.id,
            'term_id': term.id
        })

        self.assert_status(response, 201)
