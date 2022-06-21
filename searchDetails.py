"""
Ref: https://github.com/madisonmay/CommonRegex
pip install commonregex
"""
import re
from commonregex import CommonRegex


class ExtractDetails:
    def __init__(self):
        self.patterns_dict = {}
        self.patterns_dict['name'] = "[A-Z][a-z\.]+\s[A-Z][a-z\.]+\s[A-Za-z\.]+"
        self.patterns_dict['email'] = "[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+"
        self.patterns_dict['mobile_number'] = "[\s\+][0-9]{10,12}\s"
        self.patterns_dict['credit_card_number'] = "\s[0-9\-\s]{15,19}"
        self.patterns_dict['social_security_number'] = "[A-Za-z0-9]{3}\-[A-Za-z0-9]{2}\-[A-Za-z0-9]{4}"
        self.patterns_dict['expiration_date'] = "[0-9]{2}\/[0-9]{2}"
        self.patterns_dict['cvv'] = "\s[0-9]{3}\s"
        self.patterns_dict['drivers_license'] = "^[A-Z](?:\d[- ]*){14}$"

    def read_file(self, file_path):
        try:
            return open(file_path, 'r').read()
        except Exception as ee:
            raise ee

    def extract_data_re(self, file_path):
        try:
            file_data = self.read_file(file_path)

            results = {}
            for key, val in self.patterns_dict.items():
                results[key+"s"] = re.findall(val, file_data)

            return results
        except Exception as e:
            raise e

    def extract_data_commonregex(self, file_path):
        try:
            file_data = self.read_file(file_path)
            parsed_text = CommonRegex(file_data)
            results = {}
            results['mobile_numbers']           = parsed_text.phones
            results['emails']                   = parsed_text.emails
            results['credit_cards']             = parsed_text.credit_cards
            results['social_security_number']   = parsed_text.ssn_number
            results['street_address']           = parsed_text.street_addresses
            results['ip_addresses']             = parsed_text.ips
            results['names']                    = re.findall(self.patterns_dict['name'], file_data)

            return results
        except Exception as e:
            raise e

    def report(self, file_path):
        try:
            res = self.extract_data_commonregex(file_path)
            return {key: len(val) for key, val in res.items()}
        except Exception as ee:
            raise ee


if __name__ == '__main__':
    edd = ExtractDetails()
    print(edd.report('testdata.txt'))
