class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self.__title = title
        self.author = author
        self.magazine = magazine
        Article.all_articles.append(self)

    @property
    def title(self):
        return self.__title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self.__name = name
        self._articles = []

    @property
    def name(self):
        return self.__name

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        contributor_count = {}
        for article in self._articles:
            if article.author in contributor_count:
                contributor_count[article.author] += 1
            else:
                contributor_count[article.author] = 1

        return [author for author, count in contributor_count.items() if count > 2]

    def article_titles(self):
        return [article.title for article in self._articles]
