from django.core.management.base import BaseCommand
from flocs.data import instructions, levels, tasks, blocks, categories, toolboxes
from tasks.models import Instruction, Level, Block, Toolbox, Category, Task


class Command(BaseCommand):
    help = "Loads static data into the database, if it has not been done yet."

    def handle(self, *args, **options):
        self.load_model(Instruction, instructions)
        self.load_model(Level, levels)
        self.load_model(Block, blocks)
        self.load_model(Toolbox, toolboxes)
        self.load_model(Category, categories)
        self.load_model(Task, tasks)

    def load_model(self, model, data):
        name = model.__name__.lower()
        self.stdout.write('------------------------------')
        self.stdout.write('Loading {name} entities'.format(name=name))
        self.stdout.write('------------------------------')
        for entity in data:
            db_entity = model.import_entity(entity)
            self.stdout.write('+ Loaded {name}: {db_entity}'.format(name=name, db_entity=db_entity))
        self.stdout.write('--> Loaded {n} {name} entities'.format(n=len(data), name=name))
        self.stdout.write('------------------------------')
