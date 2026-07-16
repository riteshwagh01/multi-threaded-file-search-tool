import re
from concurrent.futures import ThreadPoolExecutor

files=["poem.txt",
        "eassy.txt",
        "story.txt",
        "chapter.txt",
        "letter.txt"]

keyword=input("enter the word to search : ")


def search(file_name):
    try:
        with open(file_name,"r") as f:
            matches=[]

            for line_no,line in enumerate(f,start=1):
                word=re.search(keyword,line,re.IGNORECASE)

                if word:
                    matches.append(f"line {line_no}:{line.strip()}")

            return{
                file_name:matches
                }
                
    except FileNotFoundError as e:
        print(f"{file_name} : file_not_found")


def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        result=list(executor.map(search,files))
        return result

answer=main()
for ans in answer:
    print(ans)
