import json
import os

class JSONParser():
    WORKING_DIR = os.getcwd()
    FILE = "urls.json"
    FILE_TO_PARSE = WORKING_DIR + "\\features\\test_data\\" + FILE

    def get_test_page_url(self, pattern: str) -> str:
        page_url = ""
        file = open(self.FILE_TO_PARSE)
        data = json.load(file)
        file.close()

        match pattern:
            case "main":
                page_url = data["company_site_urls"]["main_page"]
            case "whatwedo":
                page_url = data["company_site_urls"]["what_we_do_page"]
            case "solutions":
                page_url = data["company_site_urls"]["solutions_page"]
            case "games":
                page_url = data["company_site_urls"]["games_page"]
            case "about":
                page_url = data["company_site_urls"]["about_page"]
            case "news":
                page_url = data["company_site_urls"]["news_page"]
            case "careers":
                page_url = data["company_site_urls"]["careers_page"]
            case "bootcamps":
                page_url = data["company_site_urls"]["bootcamps_page"]
            case "article":
                page_url = data["company_site_urls"]["test_article_page"]
        return page_url
    

    def get_social_media_link(self, pattern: str) -> str:
        social_media_url = ""
        file = open(self.FILE_TO_PARSE)
        data = json.load(file)
        file.close()

        match pattern:
            case "facebook":
                social_media_url = data["social_media_company_links"]["facebook"]
            case "twitter":
                social_media_url = data["social_media_company_links"]["twitter"]
            case "instagram":
                social_media_url = data["social_media_company_links"]["instagram"]
            case "linkedin":
                social_media_url = data["social_media_company_links"]["linkedin"]

        return social_media_url
