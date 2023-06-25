import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Добавление одной и той же книги 2 раза
    def test_add_new_book_add_the_same_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    #параметризация
    @pytest.mark.parametrize('rating',[-1,0,11]) # Установка некорректного рейтинга - рейтинг не изменен
    def test_set_book_rating_incorrect_rating(self, rating):
        collector = BooksCollector()
        name='Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_book_rating(name) == 1

    # Установка корректного рейтинга - рейтинг изменен
    def test_set_book_rating_changing_correct_rating(self):
        collector = BooksCollector()
        first_name='Гордость и предубеждение'
        collector.add_new_book(first_name)
        collector.set_book_rating(first_name,8)
        assert collector.get_book_rating(first_name) == 8

    # Установка рейтинга несуществующей книге
    def test_set_book_rating_empty_book_rating(self):
        collector = BooksCollector()
        collector.set_book_rating('Ежик в тумане',5)
        assert collector.get_book_rating('Ежик в тумане') == None

    # вывести книги с определенным рейтингом
    def test_get_books_with_specific_rating_get_one_book(self):
        collector = BooksCollector()
        name='Золушка'
        collector.add_new_book(name)
        collector.set_book_rating(name,5)
        assert collector.get_books_with_specific_rating(5)==[name]

    # вывести словарь books_rating
    def test_get_books_rating_one_book(self):
        collector = BooksCollector()
        name = 'Beauty and the Beast'
        collector.add_new_book(name)
        collector.set_book_rating(name, 9)
        assert collector.get_books_rating() == {'Beauty and the Beast': 9}


    # Добавить книгу в избранное не из списка
    def test_add_book_in_favorites_not_from_list(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('1488')
        assert len(collector.get_list_of_favorites_books()) == 0


    # Добавить книгу в избранное
    def test_add_book_in_favorites_correct_add(self):
        collector = BooksCollector()
        collector.add_new_book('Принцесса на горошине')
        collector.add_book_in_favorites('Принцесса на горошине')
        assert collector.get_list_of_favorites_books() == ['Принцесса на горошине']


    # Удаление из избранного
    def test_delete_book_from_favorites_correct_deletion(self):
        collector = BooksCollector()
        tale='Rapunzel'
        collector.add_new_book(tale)
        collector.add_book_in_favorites(tale)
        assert len(collector.get_list_of_favorites_books()) == 1
        collector.delete_book_from_favorites(tale)
        assert len(collector.get_list_of_favorites_books()) == 0


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()