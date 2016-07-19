import sublime
import sublime_plugin
import random
import json

class CreativecrocodileCommand(sublime_plugin.TextCommand):

    @classmethod
    def get_adjective(self):
        data_file = sublime.load_resource("Packages/CreativeCrocodile/adjectives.json")
        data = sublime.decode_value(data_file)
        
        random.shuffle(data)
        return data[0]

    @classmethod
    def get_animal(self, adjective):
        data_file = sublime.load_resource("Packages/CreativeCrocodile/animals.json")
        data = sublime.decode_value(data_file)

        letter = adjective[:1].lower()
        matchedAnimals = data[letter]
        random.shuffle(matchedAnimals)
        return matchedAnimals[0]

    def run(self, edit):
        adjective = CreativecrocodileCommand.get_adjective()
        animal = CreativecrocodileCommand.get_animal(adjective)
        out = adjective + " " + animal + " "
        self.view.insert(edit, self.view.sel()[0].begin(), out)