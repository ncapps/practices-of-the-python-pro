#!/usr/bin/env python3
import os

import commands


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = (
            self.command.execute(data)
            if data else self.command.execute()
        )
        print(message)

    def __str__(self):
        return self.name


def print_options(options):
    print('\n'.join(f'({char}) {descr}'
                    for char, descr in options.items()))


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print(f'Invalid choice: {choice}')
        choice = input('Choose an option: ')
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False)
    }


def get_bookmark_id_for_deletion():
    return get_user_input('Enter a bookmark ID to delete')


def get_import_github_data():
    return {
        'github_username': get_user_input('GitHub username'),
        'preserve_timestamps': get_user_input('Preserve timestamps [Y/n]') in ('Y', 'y', None)
    }

def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def main():
    commands.CreateBookmarksTableCommand().execute()
    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(),
                    get_new_bookmark_data),
        'B': Option('List bookmarks by date',
                    commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title',
                    commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark',
                    commands.DeleteBookmarkCommand(),
                    get_bookmark_id_for_deletion),
        'G': Option('Import GitHub stars', 
                    commands.ImportGitHubStarsCommand(), 
                    get_import_github_data),
        'Q': Option('Quit', commands.QuitCommand())
    }
    
    while True:
        clear_screen()
        print_options(options)
        chosen_option = get_option_choice(options)
        clear_screen()
        chosen_option.choose()
        _ = input('Press ENTER to return to menu')
    

if __name__ == '__main__':
    main()
