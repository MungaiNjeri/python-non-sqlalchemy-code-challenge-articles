class Author:
    def __init__(self, name):  # Use double underscores for __init__
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list({article.magazine for article in self._articles if article.magazine is not None})

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

    @property
    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines if magazine.category is not None})


class Magazine:
    _all_magazines = []

    def __init__(self, name, category):  # Use double underscores for __init__
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string.")
        
        self._articles = []
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    @property
    def articles(self):
        return self._articles

    @property
    def contributors(self):
        return list({article.author for article in self._articles if article.author is not None})

    @property
    def article_titles(self):
        return [article.title for article in self._articles if article.title is not None]

    @property
    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles if article.author is not None)
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not cls._all_magazines:
            return None
        return max(cls._all_magazines, key=lambda mag: len(mag._articles))


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title


    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
