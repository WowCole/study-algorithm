class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.replace(","," ")
        paragraph=paragraph.replace("  "," ")
        paragraph=paragraph.lower()
        paragraph=paragraph.split(" ")
        word=[]

        for i in paragraph:
            new_string=''.join(char for char in i if char.isalnum())
            if not new_string in banned:
                word.append(new_string)

        return max(word,key=word.count)