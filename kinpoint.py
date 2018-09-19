import requests

class auth():
    serverHost = 'https://kinpoint.com'
    def __init__(self, username, password):
        self.username=username
        self.password=password
        r = requests.post('https://ident.familysearch.org/cis-web/oauth2/v3/token',
                          data = {'grant_type': 'password',
                                  'client_id': 'a02j0000009a4KKAAY',
                                  'username': username,
                                  'password': password})
        token= r.json()['token']
        r = requests.get(self.serverHost + f'/data/mobile/session/create?token={token}')
        sessid = r.json()['sessid']
        self.sessid=sessid
    #b,c
    def help(self):
        s = """
        Hey there user! The options are as follows:

        For target, just pass an integer which is the number of names you want to find.

        For Gender, pass either 'm', 'f', or 'm,f' depending on if you want to find just male names,
        just female names, or both.

        For ordinances, pass either 'b,c', 'i,e,s', or 'b,c,i,e,s' depending how you want to filter
        ordinances.

        The method options are:
        get_crawl_status()
        start_crawl(target, gender, ordinances)
        reserve(id)
        unreserve(id)
        read_person(id)
        (where id is in format FS-****-***)
        get_crawl_results()
        reserve_all()
        unreserve_all()
        """

        print(s)

    def get_crawl_status(self):
        self.crawl_status = requests.get(self.serverHost + f'/data/mobile/crawl/status?sessid={self.sessid}')
        return self.crawl_status


    def start_crawl(self, target, gender, ordinances):
        self.crawl = requests.get(self.serverHost+
                             f'/data/mobile/crawl?'
                             f'target={str(target)}&'
                             f'gender={gender}&'
                             f'ordinances={ordinances}&'
                             f'sessid={self.sessid}')
        return self.crawl

    def reserve(self, id):
        self.p = requests.get(self.serverHost+
            f'/data/mobile/ordinance/reserve?'
            f'id={id}&'
            f'sessid={self.sessid}')
        return self.p

    def unreserve(self, id):
        self.p = requests.get(self.serverHost+
            f'/data/mobile/ordinance/unreserve?'
            f'id={id}&'
            f'sessid={self.sessid}')
        return self.p

    def read_person(self, id):
        self.person = requests.get(self.serverHost+
            f'/data/persons/'
            f'{id}?'
            f'force=true&'
            f'sessid={self.sessid}')
        return self.person

    def get_crawl_results(self):
        self.results = requests.get(self.serverHost+
            f'/data/mobile/crawl/results?'
            f'sessid={self.sessid}')
        return self.results

    def reserve_all(self):
        r=self.get_crawl_results()
        for name in r.json()['results']:
            self.reserve(name['id'])
        r = self.get_crawl_results()
        return r

    def unreserve_all(self):
        r=self.get_crawl_results()
        for name in r.json()['results']:
            self.unreserve(name['id'])
        r = self.get_crawl_results()
        return r


# urls.startPrintCards = serverHost + '/data/mobile/ordinance/print?id=';
# urls.startReadPerson = serverHost + '/data/persons/';
# urls.endReadPerson = "?force=true";
# urls.crawlRefresh = serverHost + '/data/mobile/crawl/refresh';x
# urls.personRefresh = serverHost + '/data/mobile/crawl/refresh?type=person&id=';
# urls.startReserve = serverHost + '/data/mobile/ordinance/reserve?id=';
# urls.startUnreserve = serverHost + '/data/mobile/ordinance/unreserve?id=';
# urls.startUnshare = serverHost + '/data/mobile/ordinance/unshare?id=';
# urls.crawlResults = serverHost + '/data/mobile/crawl/results';
# urls.crawlStart = serverHost + '/data/mobile/crawl';
# urls.crawlStartTemplate = urls.crawlStart + '?target={{TARGET}}&gender={{GENDER}}&ordinances={{ORDINANCES}}';
# urls.crawlStatus = serverHost + '/data/mobile/crawl/status';
# urls.createSession = serverHost + '/data/mobile/session/create';
# urls.startPlaces = serverHost + '/data/places/search?place=';
# urls.startRedirectPersonTemplate = serverHost + '/data/mobile/person/redirect/fs?sessid={{SESSID}}&person_id={{PERSON_ID}}';
# //"https://www.familysearch.org/platform/ordinances/policy"
# urls.startOrdinancePolicy = serverHost + '/data/mobile/ordinance/policy?lang=';
# urls.getMessage = serverHost + '/data/mobile/message?code={{CODE}}&lang={{LANGUAGE}}';
# urls.getPurchaseText = serverHost + '/data/mobile/message/purchase?demo={{DEMOGRAPHICS}}&lang={{LANGUAGE}}{{VERSION}}{{REFRESH}}';
