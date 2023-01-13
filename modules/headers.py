class Headers:
    def __init__(
            self,
            PATH : str,
            METHOD : str,
            URL : str,
            HEADERS : dict
            ) -> None:
        self.PATH = PATH
        self.URL = URL
        self.METHOD = METHOD
        self.headers = HEADERS
        self.create_start_header()
    
    def create_start_header(self) -> None:
        if self.PATH == "":
            self.PATH = "/"
        elif self.PATH != "/":
            self.PATH = self.PATH[1:]
            self.temp = "/"
            last_elm = self.PATH[-1]
            for i in self.PATH:
                if i != last_elm:
                    self.temp += f"{i}/"
                else:
                    self.temp += i
            self.PATH = self.temp
        if self.PATH == "//":
            self.PATH = "/"

    def create_headers(self) -> str:
        self.headers["Host"] = self.URL.strip("://")
        header_str = "{} {} HTTP/1.1\r\n".format(self.METHOD,self.PATH)

        for key, value in self.headers.items():
            header_str += "{}: {}\r\n".format(key, value)
        header_str += "\r\n"
        return header_str