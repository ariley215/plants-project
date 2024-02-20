from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Plant

def test_create_plant_with_required_fields(self):
  user = get_user_model().objects.create(username='testuser')
  plant = Plant.objects.create(owner=user, name='Rose')
  self.assertEqual(plant.owner, user)
  self.assertEqual(plant.name, 'Rose')
# Create your tests here.
# The API should return a list of all plants when a GET request is made.

def test_get_all_plants(self):
    url = reverse("plant_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    plants = response.data
    self.assertEqual(len(plants), Plant.objects.count())


def test_delete_plant_instance(self):
    # Create a new Plant instance
    plant = Plant.objects.create(owner=get_user_model().objects.create(), name="Rose")

    # Delete the Plant instance
    plant.delete()

    # Check if the Plant instance is removed from the database
    self.assertFalse(Plant.objects.filter(name="Rose").exists())


# Updating an existing Plant instance with valid data should be successful
def test_update_existing_plant_with_valid_data(self):
        # Create a new Plant instance
  plant = Plant.objects.create(
      owner=get_user_model().objects.create(username="testuser"),
      name="Rose",
      scientific_name="Rosa",
      flower_color="Red",
      description="A beautiful flower",
      bloom_time="Spring",
        )

        # Update the Plant instance with valid data
  plant.name = "Tulip"
  plant.scientific_name = "Tulipa"
  plant.flower_color = "Yellow"
  plant.description = "A lovely flower"
  plant.bloom_time = "Summer"
  plant.save()

        # Retrieve the updated Plant instance from the database
  updated_plant = Plant.objects.get(id=plant.id)

        # Check if the Plant instance has been updated correctly
  self.assertEqual(updated_plant.name, "Tulip")
  self.assertEqual(updated_plant.scientific_name, "Tulipa")
  self.assertEqual(updated_plant.flower_color, "Yellow")
  self.assertEqual(updated_plant.description, "A lovely flower")
  self.assertEqual(updated_plant.bloom_time, "Summer")
