favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

for name in friends:
    if name in favorite_languages:
        print(name + " 喜欢的编程语言是: " + favorite_languages[name])