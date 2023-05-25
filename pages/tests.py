# Schyler Lowry
# CIS-218
# 5/25/2023

from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    """Methods for testing the Home page"""
    
    def test_url_exists_at_correct_location(self):
        """tests that url exists at the correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """tests that url is available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        """tests that the correct template name is loaded"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """tests that the page loads the template's content"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1 class=\"mt-5\">Home/About Me</h1>")

class ContactpageTest(SimpleTestCase):
    """Methods for testing the Contact page"""
    
    def test_url_exists_at_correct_location(self):
        """tests that url exists at the correct location"""
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """tests that url is available by name"""
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        """tests that the correct template name is loaded"""
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")

    def test_template_content(self):
        """tests that the page loads the template's content"""
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<h1 class=\"mt-5\">Contact Me</h1>")

class ProjectspageTest(SimpleTestCase):
    """Methods for testing the Projects page"""
    
    def test_url_exists_at_correct_location(self):
        """tests that url exists at the correct location"""
        response = self.client.get("/projects/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """tests that url is available by name"""
        response = self.client.get(reverse("projects"))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        """tests that the correct template name is loaded"""
        response = self.client.get(reverse("projects"))
        self.assertTemplateUsed(response, "projects.html")

    def test_template_content(self):
        """tests that the page loads the template's content"""
        response = self.client.get(reverse("projects"))
        self.assertContains(response, "<h1 class=\"mt-5\">My Projects</h1>")