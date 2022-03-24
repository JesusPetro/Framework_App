from logic.person import Person


class Documents(Person):

    def __init__(self, id_document: int, title: str, number_page: int, category: str, name_author: str,
                 name_author2: str):
        Person.__init__(self, id_document, name_author, name_author2)
        self._id_document = id_document
        self._title = title
        self._number_page = number_page
        self._category = category

    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        self._id_document = id_document

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def number_page(self) -> int:
        return self._number_page

    @number_page.setter
    def number_page(self, number_page: str):
        self._number_page = number_page

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4})'.format(self.id_document, self.title, self.number_page,
                                                  self.category, self.name + ' , ' + self.last_name,)


if __name__ == '__main__':
    jesu = Documents(id_document=73577376, title="Hola", number_page=1, category="scary", name_author="Edwin",
                     name_author2="Puertas")
    print(jesu)
