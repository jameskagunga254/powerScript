import requests
import re
import urlparse




print("[+]The program is starting.........")

print("\t")


print("\t")


print("[+] note that the tool is made to do web crawling on the real websites")

print("[+] to discover the hidden directories in websites that might be hidden '\n'by administrator")

print("\t")


print("\t")



print("[+]a tool by JAMES M KAGUNGA")

print("\t")

print("\t")



print("[+]please use the tool on the legal side")


print('\t')

print('\t')
target_list=[]


target_url=raw_input("Enter url >>>")



def crawler(url):
    
    response=requests.get(target_url)


    return re.findall('(?:href=")(.*?)"',response.content)




try:

    def crawl(url):

        crawler_response=crawler(url)




        for links in crawler_response :

            links=urlparse.urljoin(url,links)


            if "#" in links:

                links = links.split("#")[0]

            if target_url in links and links not in target_list:

                target_list.append(links)

                print(links)

                crawl(links)
except Exception:

    print("[-] error found on the input please try again and input full url")


crawl(target_url)
    