import requests
import pytest


class TestUserAgent:
    user_agent = ['Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
                  'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
                  'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
                  'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1']
    values = [{'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
              {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
              {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
              {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
              {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}]

    @pytest.mark.parametrize('user_agent, values', list(zip(user_agent, values)))
    def test_user_agent(self, user_agent, values):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": user_agent}, verify = False)
        print(response.text)
        assert values["platform"] in response.text, f"Platform name {values['platform']} not equal to response {print(response.json()['platform'])}"
        assert values["browser"] in response.text, f"Platform name {values['browser']} not equal to response {print(response.json()['browser'])}"
        assert values["device"] in response.text, f"Platform name {values['device']} not equal to response {print(response.json()['device'])}"
