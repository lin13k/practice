class Codec:

    referTable = ('abcdefghijklmnopqrstuvwxyz' +
                  'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
                  '0123456789')

    def __init__(self):
        self.data = {}
        self.counter = 0
        # just random key
        self.key = 8451236

    def genHash(self):
        seed = self.counter ^ self.key
        result = ''
        n = len(Codec.referTable)
        while seed > 0:
            result += Codec.referTable[seed % n]
            seed = seed // n
        self.counter += 1
        return result

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        h = self.genHash()
        self.data[h] = longUrl
        return h

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if shortUrl not in self.data:
            raise Exception('url key not found')
        return self.data[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == '__main__':
    c = Codec()
    # print(c.genHash())
    # print(c.genHash())
    print(c.decode(c.encode('url1')))
    print(c.decode(c.encode('url2')))
    print(c.decode(c.encode('url3')))
    print(c.decode(c.encode('url4')))