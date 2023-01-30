class ProcessData:
    def __init__(self, raw_data):
        self.rawData = raw_data
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
        self.article = self.findBetween(self.rawData, self.delimiters['article_start'], self.delimiters['article_end'])
        self.ID = ""
        self.finalArticle = {}

    def formatCurrency(self, input):
        return float(input.replace(".", "").replace(",", "."))

    def findBetween(self, file, first, last):
        start = file.index(first) + len(first)
        end = file.index(last, start)
        return file[start:end]

    def deleteBetween(self):
        start = self.rawData.index(self.delimiters['article_start'])
        end = self.rawData.index(self.delimiters['article_end'], start) + len(self.delimiters['article_end'])
        list1 = list(self.rawData)
        list1[start:end] = ''
        str1 = ''.join(list1)
        self.rawData = str1
        return str1

    def clear_whitespace(self, input_string):
        string = input_string.split()
        clean_string = "".join(string)
        return clean_string

    #method is used for testing only
    def getFile(self):
        with open('../scraped.txt', 'r') as file:
            return file.read()

    def getSingleArticle(self):
        self.article = self.findBetween(self.rawData, self.delimiters['article_start'], self.delimiters['article_end'])

    def getArticleId(self):
        self.ID = self.findBetween(self.article, self.delimiters['id_start'], self.delimiters['id_end'])
        self.finalArticle["ID"] = self.ID
        self.delimiters["link_end"] = self.delimiters["title_start"] = self.ID + '">'

    def getArticleLink(self):
        self.finalArticle['link'] = self.findBetween(self.article, self.delimiters['link_start'], self.delimiters['link_end'])

    def getArticleTitle(self):
        self.finalArticle['title'] = self.findBetween(self.article, self.delimiters['title_start'], self.delimiters['title_end'])

    def getArticlePrice(self):
        price = self.findBetween(self.article, self.delimiters['price_start'], self.delimiters['price_end'])
        self.finalArticle['price_kn'] = round(self.formatCurrency(price) * 7.5345, 2)
        self.finalArticle['price'] = self.clear_whitespace(price)

    def getArticleInfo(self):
        self.getSingleArticle()
        self.getArticleId()
        self.getArticleLink()
        self.getArticleTitle()
        self.getArticlePrice()
        return self.finalArticle
