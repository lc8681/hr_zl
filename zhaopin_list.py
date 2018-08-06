# coding=utf-8
import json
import requests
import csv
from tqdm import tqdm
from urllib.parse import quote
from time import sleep


def search_result(page, at_code, csv_filename):
    # url
    url = 'https://rdapi.zhaopin.com/custom/search/resumeListV2?_=1533543771973'
    # postdata部分
    data = json.dumps({
        "start": 0,
        "rows": int(page),
        "S_DISCLOSURE_LEVEL": 2,
        "S_EXCLUSIVE_COMPANY": "天津红日康仁堂药品销售有限公司;北京康仁堂制药有限公司",
        "S_EDUCATION": "4,1",
        "S_GENDER": "1",
        "S_BIRTH_YEAR": "1988,1998",
        "S_MAJOR_NAME_ALL": "中药学;中药资源与开发",
        "S_DATE_MODIFIED": "180506,180806",
        "S_DESIRED_SALARY": "0400106000",
        "S_ENGLISH_RESUME": "1",
        "isrepeat": 1,
        "sort": "complex"
    })
    # header部分的配置
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Host': 'rdapi.zhaopin.com',
        'Referer': 'https://rd5.zhaopin.com/custom/searchv2/result',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Content-Type': 'text/plain',
        'zp-route-meta': 'uid=695933625,orgid=27963463',
        'Origin': 'https://rd5.zhaopin.com',

    }
    # cookies部分的配置
    Login_Data = {}
    Login_Data['at'] = str(at_code)
    # Login_Data['at'] = 'e3010a4515c04a54b05e4fc40db785fc'
    # Login_Data['dywea'] = '95841923.4377223038735873500.1533550091.1533550091.1533550091.1'
    # Login_Data['dywec'] = '95841923'
    # Login_Data['dywez'] = '95841923.1533550091.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined'
    # Login_Data['__utma'] = '269921210.201757410.1533550091.1533550091.1533550091.1'
    # Login_Data['__utmc'] = '269921210; __utmz=269921210.1533550091.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'
    # Login_Data['__utmt'] = '1'
    # Login_Data['rt'] = '0a16482cdaef4637be8dce7539cbb3f6'
    # Login_Data['RDsUserInfo'] = '36672168546b5d75487750714e654471566351655a695e6b4e713b653f7758771365096757685e6b5275477756714365417156635c653b693f6b487146654a77277735655e6757685e6b5275477756714365417156635c6529693f6b48714f655c775377516555675f68586b59754a7724713b654a7155635c653d692a6b48713d653c775c7744655a6756685a6b5d75437750714f654c713063336555695a6b437147654a77367738655e675768526b1'
    # Login_Data['uiioit'] = '3d79306c4d7352655d644264083257684a745a70416450645f77263176645579466c47735d6552644464053252684a7457702'
    # Login_Data['NTKF_T2D_CLIENTID'] = '{uid:kf_9051_ISME9754_27963463,tid:1533550337705339}'
    # Login_Data['nTalk_CACHE_DATA'] = 'e3010a4515c04a54b05e4fc40db785fc'
    # Login_Data['sts_deviceid'] = '1650eb9250616a-0edf5e48965cc-103b6f5d-2073600-1650eb925081ca'
    # Login_Data['sts_sg'] = '1'
    # Login_Data['sts_sid'] = '1650eb925146db-031016d18fb627-103b6f5d-2073600-1650eb9251557'
    # Login_Data['diagnosis'] = '0'
    # Login_Data['sts_evtseq'] = '2'
    # Login_Data['zp-route-meta'] = 'uid=695933625,orgid=27963463'
    # Login_Data['login_point'] = '113329276'
    # Login_Data['__utmb'] = '269921210.10.6.1533550335425'
    res = requests.post(url, data, headers, cookies=Login_Data)
    check_json = json.loads(res.text)
    datalist = check_json['data']['dataList']
    filename = csv_filename + '.csv'
    out = open(filename, 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    csv_header = ['姓名', '学历', '毕业学校', '专业', '目前状况', '链接']
    csv_write.writerow(csv_header)
    for x in datalist:
        sleep(1)
        # resume_name = x['name']
        username = x['userName']
        # jobTitle = x['jobTitle']
        eduLevel = x['eduLevel']
        # gender = x['gender']
        # isFemale = x['isFemale']
        # age = x['age']
        # city = x['city']
        # cityId = x['cityId']
        # modifyDate = x['modifyDate']
        # desiredSalary = x['desiredSalary']
        careerStatus = x['careerStatus']
        # workYears = x['workYears']
        school = x['school']
        # employment = x['employment']
        # jobType = x['jobType']
        # desireCity = x['desireCity']
        major = x['major']
        id = x['id']
        t = x['t']
        k = x['k']
        # beginDate = x['lastJobDetail']['beginDate']
        # endDate = x['lastJobDetail']['endDate']
        # companyName = x['lastJobDetail']['companyName']
        # department = x['lastJobDetail']['department']
        # jobName = x['lastJobDetail']['jobName']
        # salary = x['lastJobDetail']['salary']
        # industry = x['lastJobDetail']['industry']
        # profession = x['lastJobDetail']['profession']
        # companyType = x['lastJobDetail']['companyType']
        # description = x['lastJobDetail']['description']
        # school_beginDate = x['schoolDetail']['beginDate']
        # school_endDate = x['schoolDetail']['endDate']
        # school_schoolName = x['schoolDetail']['schoolName']
        # school_major = x['schoolDetail']['major']
        # school_degree = x['schoolDetail']['degree']
        resume_url = 'https://rd5.zhaopin.com/resume/detail?keyword=&resumeNo=' + quote(id, 'utf-8') + '_1_1%3B' + quote(k, 'utf-8') + '%3B' + quote(t, 'utf-8') + '&openFrom=1'
        information = [username, eduLevel, school, major, careerStatus, resume_url]
        csv_write.writerow(information)


if __name__ == '__main__':
    page = input("要抓取多少条数据？\n")
    at_code = input("输入验证码，需手动登录后用浏览器查看然后输入到这里\n")
    csv_filename = input("输入文件名,文件保存在xx\n")
    search_result(page=page, at_code=at_code, csv_filename=csv_filename)
