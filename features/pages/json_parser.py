import json
import os

class JSONParser():
    WORKING_DIR = os.getcwd()

    def get_urls_json_path(self):        
        FILE = "urls.json"
        FILE_TO_PARSE = self.WORKING_DIR + "\\features\\test_data\\" + FILE
        return FILE_TO_PARSE
    
    def get_texts_json_path(self):
        FILE = "texts.json"
        FILE_TO_PARSE = self.WORKING_DIR + "\\features\\test_data\\" + FILE
        return FILE_TO_PARSE

    def get_test_page_url(self, pattern: str) -> str:
        page_url = ""
        file = open(self.get_urls_json_path())
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
            case "portfolio":
                page_url = data["company_site_urls"]["portfolio_page"]
        return page_url
    

    def get_social_media_link(self, pattern: str) -> str:
        social_media_url = ""
        file = open(self.get_urls_json_path())
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


    def get_required_text(self, pattern: str) -> str:
        final_text = ""
        file = open(self.get_texts_json_path())
        data = json.load(file)
        file.close()

        match pattern:
            case "top_whatwedo":
                final_text = data["site_texts"]["top_header_whatwedo"]
            case "sub_top_whatwedo":
                final_text = data["site_texts"]["sub_top_header_whatwedo"]
            case "gamedev_first":
                final_text = data["site_texts"]["game_dev_description_first"]
            case "gamedev_second":
                final_text = data["site_texts"]["game_dev_description_second"]
            case "gameporting":
                final_text = data["site_texts"]["game_porting_description"]
            case "engineering":
                final_text = data["site_texts"]["engineering_description"]
            case "creative":
                final_text = data["site_texts"]["creative_description"]

        return final_text
    