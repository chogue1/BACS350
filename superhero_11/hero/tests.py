# hero/tests.py
from django.test import TestCase
from .models import Superhero

class HeroModelTest(TestCase):
    
    def setUp(self):
        Superhero.objects.create(name='Slim-Jim Hero',
                                identity='Macho-Man Randy Savage',
                                description='ooh yeah',
                                strength='has a slim jim',
                                weakness='doesnt have more',
                                )
        
    def test_hero_name(self):
        hero = Superhero.objects.get(id=1)
        expected_object_name = f'{hero.name}'
        self.assertEqual(expected_object_name, 'Slim-Jim Hero')
        
    def test_hero_identity(self):
        hero = Superhero.objects.get(id=1)
        expected_object_identity = f'{hero.identity}'
        self.assertEqual(expected_object_identity, 'Macho-Man Randy Savage')

    def test_hero_description(self):
        hero = Superhero.objects.get(id=1)
        expected_object_description = f'{hero.description}'
        self.assertEqual(expected_object_description, 'ooh yeah')

    def test_hero_strength(self):
        hero = Superhero.objects.get(id=1)
        expected_object_strength = f'{hero.strength}'
        self.assertEqual(expected_object_strength, 'has a slim jim')

    def test_hero_weakness(self):
        hero = Superhero.objects.get(id=1)
        expected_object_weakness = f'{hero.weakness}'
        self.assertEqual(expected_object_weakness, 'doesnt have more')

    def test_hero_image(self):
        hero = Superhero.objects.get(id=1)
        expected_object_image = f'{hero.image}'
        self.assertEqual(expected_object_image, null)

