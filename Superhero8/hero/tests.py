from django.test import TestCase
from .models import Superhero

class HeroModelTest(TestCase):
    
    def setUp(self):
        Superhero.objects.create(name='Macho-Man Randy Savage',
                                identity='slim_jim_hero',)
        
    def test_hero_name(self):
        hero = Superhero.objects.get(id=1)
        expected_object_name = f'{hero.name}'
        self.assertEqual(expected_object_name, 'Macho-Man Randy Savage')
        
    def test_hero_identity(self):
        hero = Superhero.objects.get(id=1)
        expected_object_identity = f'{hero.identity}'
        self.assertEqual(expected_object_identity, 'slim_jim_hero')

