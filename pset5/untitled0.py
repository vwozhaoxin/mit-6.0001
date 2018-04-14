#!usr/bin/env python  
#encoding:utf-8  
  
''''' 
__Author__:沂水寒城 
功能：学习使用feedparser模块 
'''  
  
import feedparser  
  
  
def test(url='http://blog.csdn.net/together_cz/article'):  
    ''''' 
    学习使用feedparser 
    输入：url 
    输出：页面信息 
    '''  
    one_page_dict = feedparser.parse(url)  
    ''''' 
    解析得到的是一个字典 
    '''  
    print (one_page_dict  )
    ''''' 
    输出字典中的键值有哪些，一共有10中如下： 
    ['feed', 'status', 'version', 'encoding', 'bozo', 'headers', 'href', 'namespaces', 'entries', 'bozo_exception'] 
    '''  

  
  
  
if __name__ == '__main__':  
    url_list=['https://www.yahoo.com/news/rss/topstories']  
    for one_url in url_list:  
        print ('当前url为--->', one_url ) 
        try:  
            test(one_url)  
        except:  
            print( '***************************************************************')  
        print ('----------------------------------------------------------'  )