class AcademicSubject:
    title: str
    main_page_url: str

    def __init__(self, title: str, main_page_url: str):
        self.title = title
        self.main_page_url = main_page_url


BASIC_MATH = AcademicSubject('Базовая математика', 'https://mathb-ege.sdamgia.ru')
PROFILE_MATH = AcademicSubject('Профильная математика', 'https://math-ege.sdamgia.ru')
COMPUTER_SCIENCE = AcademicSubject('Информатика', 'https://inf-ege.sdamgia.ru')
RUSSIAN_LANGUAGE = AcademicSubject('Русский язык', 'https://rus-ege.sdamgia.ru')
ENGLISH = AcademicSubject('Английский язык', 'https://en-ege.sdamgia.ru')
GERMAN = AcademicSubject('Немецкий язык', 'https://de-ege.sdamgia.ru')
FRENCH = AcademicSubject('Французский язык', 'https://fr-ege.sdamgia.ru')
SPANISH = AcademicSubject('Испанский язык', 'https://sp-ege.sdamgia.ru')
PHYSICS = AcademicSubject('Физика', 'https://phys-ege.sdamgia.ru')
CHEMISTRY = AcademicSubject('Химия', 'https://chem-ege.sdamgia.ru')
BIOLOGY = AcademicSubject('Биология', 'https://bio-ege.sdamgia.ru', )
GEOGRAPHY = AcademicSubject('География', 'https://geo-ege.sdamgia.ru')
SOCIAL_STUDIES = AcademicSubject('Обществознание', 'https://soc-ege.sdamgia.ru')
LITERATURE = AcademicSubject('Литература', 'https://lit-ege.sdamgia.ru')
HISTORY = AcademicSubject('История', 'https://hist-ege.sdamgia.ru')

all_subjects = [
    BASIC_MATH,
    PROFILE_MATH,
    COMPUTER_SCIENCE,
    RUSSIAN_LANGUAGE,
    ENGLISH,
    GERMAN,
    FRENCH,
    SPANISH,
    PHYSICS,
    CHEMISTRY,
    BIOLOGY,
    GEOGRAPHY,
    SOCIAL_STUDIES,
    LITERATURE,
    HISTORY,
]
