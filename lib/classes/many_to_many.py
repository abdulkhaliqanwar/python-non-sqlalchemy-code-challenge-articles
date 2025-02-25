class Article:
    # Class attribute to store all article instances
    all = []

    def __init__(self, author, magazine, title):
        """Initialize an Article with an author, magazine, and title."""
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # Add article instance to the list

    @property
    def title(self):
        """Title property (cannot be changed once set)."""
        return self._title

    @title.setter
    def title(self, new_title):
        """Title setter with validation to ensure it meets length constraints."""
        if hasattr(self, "_title"):  # Prevents modifying the title after setting it
             AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")

    @property
    def author(self):
        """Author property, ensuring it is an instance of Author."""
        return self._author

    @author.setter
    def author(self, new_author):
        """Setter to enforce that the author is an instance of Author."""
        if isinstance(new_author, Author):
            self._author = new_author
        else:
             TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        """Magazine property, ensuring it is an instance of Magazine."""
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        """Setter to enforce that the magazine is an instance of Magazine."""
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
             TypeError("Magazine must be an instance of Magazine")


class Author:
    """Represents an author who writes articles."""

    def __init__(self, name):
        """Initialize an author with a name."""
        self.name = name

    @property
    def name(self):
        """Name property (cannot be changed after being set)."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for name with validation to ensure it's a string."""
        if hasattr(self, "_name"):  # Prevents modifying the name after setting it
             AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name
                else:
                     ValueError("Name must be longer than 0 characters")
            else:
                 TypeError("Name must be a string")

    def articles(self):
        """Returns a list of articles written by this author."""
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        """Returns a list of unique magazines the author has written for."""
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        """Creates and returns a new article for a given magazine."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns a list of unique categories of magazines the author has contributed to."""
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    """Represents a magazine that publishes articles."""

    def __init__(self, name, category):
        """Initialize a magazine with a name and category."""
        self.name = name
        self.category = category

    @property
    def name(self):
        """Name property with constraints on length."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for name with validation on length constraints."""
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
             ValueError("Name must be between 2 and 16 characters")
        else:
             TypeError("Name must be a string")

    @property
    def category(self):
        """Category property ensuring it's a string."""
        return self._category

    @category.setter
    def category(self, new_category):
        """Setter for category ensuring it's not empty."""
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                 ValueError("Category must be longer than 0 characters")
        else:
         TypeError("Category must be a string")

    def articles(self):
        """Returns a list of articles published in this magazine."""
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        """Returns a list of unique authors who have written for this magazine."""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Returns a list of all article titles published in this magazine."""
        article_titles = [article.title for article in self.articles()]
        return article_titles if article_titles else None

    def contributing_authors(self):
        """Returns a list of authors who have written more than one article for this magazine."""
        authors = {}  # Dictionary to count the number of articles per author
        list_of_authors = []  # List of authors who have written multiple articles

        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1

        for author, count in authors.items():
            if count >= 2:
                list_of_authors.append(author)

        return list_of_authors or None
