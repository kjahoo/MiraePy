from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

class Cretop_data:

    def Clogin(self, n):
        self.driver = webdriver.Ie('c:\IEDriverServer.exe')

        self.driver.implicitly_wait(3)
        self.driver.get('http://www.cretop.com')

        self.driver.find_element_by_name('id').send_keys('mdwm'+str(n))
        self.driver.find_element_by_name('pwd').send_keys('miraedw'+str(n)+'+')
        self.driver.find_element_by_id('loginBtn1').click()

    def Cdata(self, c_number):
        self.driver.find_element_by_id('_srchNm').send_keys(c_number)
        self.driver.find_element_by_id('uniSrch').click()
        self.driver.find_element_by_class_name('CMCOM01C1').click()

        #파싱_브리핑 for CEO
        html = self.driver.page_source
        soup_bfc = bs(html, 'html.parser')
        #기업명
        기업명 = soup_bfc.find('ul', {'class': 'stit'}).text
        #기업개황 화면 이동
        self.driver.get('http://www.cretop.com/en/ENINT02R0.do')
        #파싱_기업일반_기업개황 (company overview)
        html = self.driver.page_source
        soup_co = bs(html, 'html.parser')
        #대표자
        대표자 = (soup_co.find('th', id='reper').next_sibling.next_sibling).text
        #대표이사 프로필 화면 이동
        self.driver.get('http://www.cretop.com/en/ENMNG02R0.do')
        #파싱_프로필
        html = self.driver.page_source
        soup_p = bs(html, 'html.parser')
        #출신학교
        출신학교 = (soup_p.find('th', id='origSch').next_sibling.next_sibling).text
        #종업원수
        employee_p = (soup_co.find('th', id='ordnEm').next_sibling.next_sibling).text

        종업원수 = re.findall('\d+', employee_p)
        종업원수 = int("".join(종업원수))
        #설립일자
        설립일자 = (soup_co.find('th', id='estbDt').next_sibling.next_sibling).text
        기업형태 = (soup_co.find('th', id='ipoCdNm').next_sibling.next_sibling).text
        기업규모 = (soup_co.find('th', id='enpSze').next_sibling.next_sibling).text
        전화번호 = (soup_co.find('th', id='telNo').next_sibling.next_sibling).text
        팩스번호 = (soup_co.find('th', id='faxNo').next_sibling.next_sibling).text
        홈페이지 = soup_co.find('a', {'title': '새 창 열림'}).text
        이메일 = (soup_co.find('th', id='email').next_sibling.next_sibling).text
        주소 = (soup_co.find('th', id='locRdnmZip').next_sibling.next_sibling).text
        주소 = 주소.replace("\n", "").replace("\t", "")
        업종 = soup_co.find('th', {"colspan": "2"}, {'scope': 'row'}, '업종(10차)').next_sibling.next_sibling.text
        업종 = 업종.replace("\n", "").replace("\t", "")
        업종 = 업종.split(')')[1]
        주요제품 = soup_co.find('th', {"colspan": "2"}, {'scope': 'row'}, '주요제품(상품)').next_sibling.next_sibling.text
        주요제품 = 업종.replace("\n", "").replace("\t", "")

        # 실적 테이블 만들기(DataFrame)
        table = soup_co.find('table', {'class': 'tb_type2 v_mid'})

        # 실적 columns 파싱
        col = table.find_all('th')
        실적_col = []
        for i in col:
            실적_col.append(i.text)

        # 변수 준비
        data = table.find_all('td')
        실적_rawdata = []
        실적_data = []
        실적_raw = []

        # 실적 Raw데이터 파싱
        for i in data:
            실적_rawdata.append(i.text)

        # 문자->순자 변환, DataFrame화
        j = 0
        for i in range(int(len(실적_rawdata) / len(실적_col))):
            실적_raw.append(실적_rawdata[j])
            for k in range(j + 1, j + 7):
                실적_rawdata[k] = int(실적_rawdata[k].replace(',', ''))
            실적_data.append(실적_rawdata[j + 1:j + 7])
            j += len(실적_col)
        실적_col.remove('결산기준일자')
        실적테이블 = pd.DataFrame(실적_data, columns=실적_col, index=실적_raw)
        return {'기업명':기업명, '대표자':대표자, '출신학교':출신학교,
               '종업원수':종업원수, '설립일자':설립일자, '기업형태':기업형태,
               '기업규모':기업규모, '전화번호':전화번호, '팩스번호':팩스번호,
               '홈페이지':홈페이지, '이메일':이메일, '주소':주소, '업종':업종,
               '주요제품':주요제품, '실적테이블':실적테이블}


    # print(기업명, 대표자,출신학교, 종업원수, 설립일자, 기업형태, 기업규모, 전화번호, 팩스번호, 홈페이지,
    #       이메일, 주소, 업종, 주요제품, 실적_data)

# a=Cretop()
# a.Clogin(1)
# print(a.Cdata('1201110000464'))
