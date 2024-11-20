from main import BooksCollector

name = 'Гордость и предубеждение и зомби'
genre = 'Фантастика'

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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.fixture()
    def add_book(self):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        return collector

    # 2. устанавливаем книге жанр
    def test_set_book_genre_success(self, add_book):
        assert add_book.get_book_genre(name) == genre

    # 3. получаем жанр книги по её имени
    def test_get_book_genre_success(self, add_book):
        assert add_book.get_book_genre(name) == genre

    # 4. выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_success(self, add_book):
        assert len(add_book.get_books_with_specific_genre(genre)) == 1

    # 5. получаем словарь books_genre
    def test_get_books_genre_success(self, add_book):
        assert add_book.books_genre

    # 6. возвращаем книги, подходящие детям
    def test_get_books_for_children_success(self, add_book):
        assert add_book.get_books_for_children()

    # 7. добавляем книгу в Избранное
    def test_add_book_in_favorites_success(self, add_book):
        add_book.add_book_in_favorites(name)
        assert len(add_book.favorites) == 1

    # 8. удаляем книгу из Избранного
    def test_delete_book_from_favorites_success(self, add_book):
        add_book.add_book_in_favorites(name)
        add_book.delete_book_from_favorites(name)
        assert len(add_book.favorites) == 0

    # 9. получаем список Избранных книг
    def test_get_list_of_favorites_books_success(self, add_book):
        add_book.add_book_in_favorites(name)
        assert add_book.favorites
