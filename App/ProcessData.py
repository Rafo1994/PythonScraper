class ProcessData:
    def __init__(self):
        #self.rawData = raw_data
        self.delimiters = {
            'article_start': '<article class="entity-body cf">',
            'article_end': '</article>',
            'id_start': '<a name="',
            'id_end': '" class=',
            'link_start': 'href="',
            'title_end': '</a>',
            'price_start': '<strong class="price price--hrk">',
            'price_end': '&nbsp;'
        }
        self.article = self.findBetween(self.getFile(), self.delimiters['article_start'], self.delimiters['article_end'])
        self.finalArticle = {}

        #run class upon instantiation
        self.getArticleId()
        self.getArticleLink()
        self.getArticleTitle()
        self.getArticlePrice()

        #Get price in KN
        self.finalArticle['price_kn'] = round(self.formatCurrency(self.finalArticle['price']) * 7.5345, 2)

    def formatCurrency(self, input):
        return float(input.replace(".", "").replace(",", "."))

    def findBetween(self, file, first, last):
        start = file.index(first) + len(first)
        end = file.index(last, start)
        return file[start:end]

    def delete_between(self, file, first, last):
        start = file.index(first)
        end = file.index(last, start) + len(last)
        list1 = list(file)
        list1[start:end] = ''
        str1 = ''.join(list1)
        return str1

    def clear_whitespace(self, input_string):
        string = input_string.split()
        clean_string = "".join(string)
        return clean_string

    def getFile(self):
        with open('../scraped.txt', 'r') as file:
            return file.read()

    def getSingleArticle(self):
        return self.findBetween(self.getFile(), self.delimiters['article_start'], self.delimiters['article_end'])

    def getArticleId(self):
        article_id = self.findBetween(self.article, self.delimiters['id_start'], self.delimiters['id_end'])
        self.finalArticle["ID"] = article_id
        self.delimiters["link_end"] = self.delimiters["title_start"] = article_id + '">'

    def getArticleLink(self):
        self.finalArticle['link'] = self.findBetween(self.article, self.delimiters['link_start'], self.delimiters['link_end'])

    def getArticleTitle(self):
        self.finalArticle['title'] = self.findBetween(self.article, self.delimiters['title_start'], self.delimiters['title_end'])

    def getArticlePrice(self):
        price = self.findBetween(self.article, self.delimiters['price_start'], self.delimiters['price_end'])
        self.finalArticle['price'] = self.clear_whitespace(price)

    def getArticleInfo(self):
        self.getArticleId()
        self.getArticleLink()
        self.getArticleTitle()
        self.getArticlePrice()

print(ProcessData().finalArticle)