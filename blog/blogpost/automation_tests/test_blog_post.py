from datetime import datetime
from django.test import LiveServerTestCase
from selenium import webdriver
from blogpost.models import Blogpost

class BlogpostDetailCase(LiveServerTestCase):
    def setUp(self):
        Blogpost.objects.create(
            title='hello',
            author='admin',
            slug='this_is_a_test',
            body='This is a blog',
            posted=datetime.now
        )

        self.selenium = webdriver.Chrome("/Users/gye200/Downloads/chromedriver")
        self.selenium.maximize_window()
        super(BlogpostDetailCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(BlogpostDetailCase, self).tearDown()

    def test_visit_blog_post(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url,  "/blog/this_is_a_test.html")
        )

        self.assertIn("hello", self.selenium.title)
